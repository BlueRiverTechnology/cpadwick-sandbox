---
name: fetch-prs
description: >
  Fetch pull requests from the BlueRiverTechnology/brt monorepo using the
  gh CLI. Groups PRs by `prg:*` label prefix (each label = a team).
  Returns structured JSON that can be consumed by the summarizer agent.
---

# Fetch BRT Pull Requests

This skill retrieves pull requests from the `BlueRiverTechnology/brt` monorepo
on github.com using the `gh` CLI. Teams are identified by `prg:*` labels.

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth login`)
- Read access to `BlueRiverTechnology/brt`

## Important: use the right date qualifier

The GitHub search API has three date qualifiers for PRs:

- `updated:>=DATE` — PRs touched in the window (includes rebases, comments on
  old PRs). Over-counts.
- `merged:>=DATE` — PRs actually merged in the window. Accurate for "shipped".
- `created:>=DATE` — PRs opened in the window. Accurate for "newly opened".

**Always use `merged:>=DATE` for the merged query and `created:>=DATE` for the
open query. Never rely solely on `updated:>=DATE`.**

---

## Team labels

All PRs live in one repo. Teams are identified by **labels** with the `prg:`
prefix. Known programs:

| Label | Team |
|-------|------|
| `prg:shasta` | Shasta (See & Spray platform) |
| `prg:jupiter` | Jupiter (perception / autonomy) |
| `prg:adk` | ADK (Application Development Kit) |
| `prg:dune` | Dune (autonomous mowing) |
| `prg:mercury` | Mercury (localization / mapping) |
| `prg:bumblebee` | Bumblebee (harvest automation) |
| `prg:mesa` | Mesa |
| `prg:athena` | Athena |
| `prg:forestry` | Forestry |
| (no `prg:` label) | unlabeled |

A PR may have **multiple** `prg:` labels (cross-team work). Count it under each
team it is tagged with.

### Fetch merged PRs

```bash
SINCE_DATE=$(date -d "7 days ago" +%Y-%m-%d)

gh api \
  "search/issues?q=repo:BlueRiverTechnology/brt+type:pr+merged:>=${SINCE_DATE}&per_page=100" \
  --paginate \
  -q '.items[] | {
    number: .number,
    title: .title,
    user: .user.login,
    html_url: .html_url,
    labels: [.labels[].name],
    created_at: .created_at,
    closed_at: .closed_at,
    body: (.body // "" | .[0:200])
  }'
```

### Fetch open PRs (created in window)

```bash
gh api \
  "search/issues?q=repo:BlueRiverTechnology/brt+type:pr+is:open+created:>=${SINCE_DATE}&per_page=100" \
  --paginate \
  -q '.items[] | {
    number: .number,
    title: .title,
    user: .user.login,
    html_url: .html_url,
    labels: [.labels[].name],
    created_at: .created_at,
    body: (.body // "" | .[0:200])
  }'
```

## Group by label

For each PR, extract labels matching `prg:*`. Group PRs by that label. PRs with
no `prg:` label go into the "unlabeled" bucket. Within each team, list merged
and open separately.

## Output format

Present the grouped data as structured JSON or Markdown. Example:

```json
{
  "period": "2026-04-17 to 2026-04-24",
  "source": "BlueRiverTechnology/brt",
  "mode": "monorepo",
  "teams": {
    "shasta": {
      "merged": [
        { "number": 11571, "title": "shark: Handle hanging Active Model AOS calls", "author": "jocelyn-vil" }
      ],
      "open": []
    }
  }
}
```

## Tips

- BRT typically has ~250 merged PRs per week. The search API caps at 1000
  results, so a 7-day window is safe. Narrow the window if needed.
- The search API returns max 1000 results. For very active repos, narrow the
  date window.
- Use `--paginate` to handle large result sets.
- If rate-limited, add a brief pause between queries.
- For the monorepo, run the merged and open queries separately (two API calls
  total) rather than one `updated:` query that requires per-PR merge checks.
- The `body` field is truncated to 300 chars to keep payloads manageable.
