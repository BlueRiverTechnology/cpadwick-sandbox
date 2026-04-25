import { useState, useEffect, useMemo } from 'react';

const TEAM_COLORS = [
  '#6366f1', '#22c55e', '#3b82f6', '#f97316', '#eab308',
  '#ec4899', '#14b8a6', '#a855f7', '#f43f5e',
];

function PieChart({ teams }) {
  const total = teams.reduce((s, t) => s + t.merged_count + t.open_count, 0);
  let cumulative = 0;

  const slices = teams.map((team, i) => {
    const count = team.merged_count + team.open_count;
    const startAngle = (cumulative / total) * 360;
    cumulative += count;
    const endAngle = (cumulative / total) * 360;
    const pct = ((count / total) * 100).toFixed(0);
    return { ...team, startAngle, endAngle, color: TEAM_COLORS[i % TEAM_COLORS.length], pct, count };
  });

  function arcPath(start, end, r) {
    const s = ((start - 90) * Math.PI) / 180;
    const e = ((end - 90) * Math.PI) / 180;
    const largeArc = end - start > 180 ? 1 : 0;
    return [
      `M ${r + r * Math.cos(s)} ${r + r * Math.sin(s)}`,
      `A ${r} ${r} 0 ${largeArc} 1 ${r + r * Math.cos(e)} ${r + r * Math.sin(e)}`,
      `L ${r} ${r}`,
    ].join(' ');
  }

  const size = 140;
  const r = size / 2;

  return (
    <div className="pie-chart">
      <h2>Distribution</h2>
      <div className="pie-layout">
        <svg viewBox={`0 0 ${size} ${size}`} width={size} height={size}>
          {slices.map((sl) => (
            <path
              key={sl.id}
              d={arcPath(sl.startAngle, sl.endAngle, r)}
              fill={sl.color}
              stroke="var(--bg)"
              strokeWidth="1.5"
            />
          ))}
        </svg>
        <ul className="pie-legend">
          {slices.map((sl) => (
            <li key={sl.id}>
              <span className="pie-swatch" style={{ background: sl.color }} />
              <span className="pie-name">{sl.name}</span>
              <span className="pie-pct">{sl.pct}%</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function groupByAuthor(prs) {
  const map = {};
  for (const pr of prs) {
    if (!map[pr.author]) map[pr.author] = [];
    map[pr.author].push(pr);
  }
  return Object.entries(map)
    .map(([author, items]) => ({ author, items }))
    .sort((a, b) => b.items.length - a.items.length);
}

function AuthorGroup({ author, items, type }) {
  const [open, setOpen] = useState(false);
  const avgDays = type === 'merged' && items.some((pr) => pr.days_open != null)
    ? (items.reduce((s, pr) => s + (pr.days_open || 0), 0) / items.length).toFixed(1)
    : null;
  return (
    <div className="author-group">
      <button className="author-row" onClick={() => setOpen(!open)}>
        <span className={`author-chevron ${open ? 'open' : ''}`}>▸</span>
        <span className="author-name">{author}</span>
        {avgDays && <span className="author-avg">{avgDays}d avg</span>}
        <span className={`badge ${type}`}>{items.length} {type === 'merged' ? 'merged' : 'open'}</span>
      </button>
      {open && (
        <ul className="pr-list author-prs">
          {items.map((pr) => (
            <li key={pr.number} className="pr-item">
              <a href={pr.url} target="_blank" rel="noopener noreferrer" className="pr-number">
                #{pr.number}
              </a>
              <span className="pr-title">{pr.title}</span>
              {pr.days_open != null && (
                <span className="pr-days">{pr.days_open}d</span>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function App() {
  const [data, setData] = useState(null);
  const [selectedTeam, setSelectedTeam] = useState(null);
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light');

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  useEffect(() => {
    fetch('./data.json')
      .then((r) => r.json())
      .then(setData)
      .catch((err) => console.error('Failed to load data:', err));
  }, []);

  if (!data) {
    return <div className="loading">Loading summary data…</div>;
  }

  const { period, summary, teams } = data;
  const maxMerged = Math.max(...teams.map((t) => t.merged_count));
  const activeTeam = teams.find((t) => t.id === selectedTeam);

  return (
    <div className="container">
      <header className="header">
        <div className="header-top">
          <h1>Weekly Engineering Summary</h1>
          <button
            className="theme-toggle"
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
          >
            {theme === 'dark' ? '☀️' : '🌙'}
          </button>
        </div>
        <p className="period">
          {period.start} → {period.end} · BlueRiverTechnology/brt
        </p>
      </header>

      <div className="stats-row">
        <div className="stat-card">
          <div className="label">Merged</div>
          <div className="value green">{summary.total_merged}</div>
        </div>
        <div className="stat-card">
          <div className="label">Open</div>
          <div className="value blue">{summary.total_open}</div>
        </div>
        <div className="stat-card">
          <div className="label">Teams</div>
          <div className="value orange">{summary.team_count}</div>
        </div>
      </div>

      <div className="main-row">
      <div className="highlights">
        <h2>Team Highlights</h2>
        <table className="highlights-table">
          <thead>
            <tr>
              <th>Team</th>
              <th>Summary</th>
              <th>Merged</th>
              <th>Open</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, i) => (
              <tr
                key={team.id}
                className={selectedTeam === team.id ? 'active' : ''}
                onClick={() => setSelectedTeam(selectedTeam === team.id ? null : team.id)}
              >
                <td className="hl-team" style={{ color: TEAM_COLORS[i % TEAM_COLORS.length] }}>{team.name}</td>
                <td className="hl-summary">{team.summary}</td>
                <td className="hl-count"><span className="badge merged">{team.merged_count}</span></td>
                <td className="hl-count"><span className="badge open">{team.open_count}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="side-charts">
      <div className="bar-chart">
        <h2>PRs by Team</h2>
        <div className="duration-legend">
          <span className="duration-legend-item"><span className="swatch merged-swatch" /> merged</span>
          <span className="duration-legend-item"><span className="swatch open-swatch" /> open</span>
        </div>
        {teams.map((team) => (
          <div
            key={team.id}
            className="bar-row"
            onClick={() =>
              setSelectedTeam(selectedTeam === team.id ? null : team.id)
            }
          >
            <span className="bar-label">{team.name}</span>
            <div className="bar-track">
              <div
                className="bar-fill-merged"
                style={{
                  width: `${(team.merged_count / maxMerged) * 100}%`,
                }}
              />
              <div
                className="bar-fill-open"
                style={{
                  width: `${(team.open_count / maxMerged) * 100}%`,
                }}
              />
            </div>
            <span className="bar-count">{team.merged_count}</span>
          </div>
        ))}
      </div>

      <PieChart teams={teams} />
      </div>{/* side-charts */}
      </div>{/* main-row */}

      {activeTeam && (
        <div className="team-detail">
          <div className="detail-header">
            <h2>
              {activeTeam.name}{' '}
              <span style={{ fontWeight: 400, color: 'var(--text-muted)', fontSize: '0.9rem' }}>
                {activeTeam.description}
              </span>
            </h2>
            <button className="close-btn" onClick={() => setSelectedTeam(null)}>
              Close ✕
            </button>
          </div>
          <div className="detail-stats">
            <div className="detail-stat">
              <span className="detail-stat-value green">{activeTeam.merged_count}</span>
              <span className="detail-stat-label">merged</span>
            </div>
            <div className="detail-stat">
              <span className="detail-stat-value blue">{activeTeam.open_count}</span>
              <span className="detail-stat-label">open</span>
            </div>
            {activeTeam.avg_days_to_merge != null && (
              <div className="detail-stat">
                <span className="detail-stat-value orange">{activeTeam.avg_days_to_merge}d</span>
                <span className="detail-stat-label">avg to merge</span>
              </div>
            )}
            {activeTeam.median_days_to_merge != null && (
              <div className="detail-stat">
                <span className="detail-stat-value accent">{activeTeam.median_days_to_merge}d</span>
                <span className="detail-stat-label">median</span>
              </div>
            )}
          </div>
          <p className="detail-summary">{activeTeam.summary}</p>

          {activeTeam.merged.length > 0 && (
            <>
              <div className="pr-section-title">
                Merged ({activeTeam.merged.length})
              </div>
              {groupByAuthor(activeTeam.merged).map((g) => (
                <AuthorGroup key={g.author} author={g.author} items={g.items} type="merged" />
              ))}
            </>
          )}

          {activeTeam.open.length > 0 && (
            <>
              <div className="pr-section-title">
                Open ({activeTeam.open.length})
              </div>
              {groupByAuthor(activeTeam.open).map((g) => (
                <AuthorGroup key={g.author} author={g.author} items={g.items} type="open" />
              ))}
            </>
          )}
        </div>
      )}

      <h3 className="teams-header">Teams</h3>
      <div className="team-grid">
        {teams.map((team) => (
          <div
            key={team.id}
            className={`team-card ${selectedTeam === team.id ? 'active' : ''}`}
            onClick={() =>
              setSelectedTeam(selectedTeam === team.id ? null : team.id)
            }
          >
            <div className="team-name">{team.name}</div>
            <div className="team-desc">{team.description}</div>
            <div className="team-stats">
              <span className="badge merged">{team.merged_count} merged</span>
              <span className="badge open">{team.open_count} open</span>
              {team.median_days_to_merge != null && team.median_days_to_merge > 0 && (
                <span className="badge duration">{team.median_days_to_merge}d median</span>
              )}
            </div>
            <div className="team-summary">{team.summary}</div>
          </div>
        ))}
      </div>

      <footer className="footer">
        Generated {data.generated_at} · Data from GitHub Search API
      </footer>
    </div>
  );
}

export default App;
