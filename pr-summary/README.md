# PR Summary Dashboard

Interactive React dashboard for viewing weekly pull request activity in the BlueRiverTechnology/brt monorepo.

## Prerequisites

- Node.js 18+
- `gh` CLI authenticated with access to BlueRiverTechnology/brt

## Quick Start

```bash
cd dashboard
npm install
npm run dev
```

Open http://localhost:5173 in your browser.

## Generating Fresh Data

Use the **PR Summarizer** Copilot agent (defined in `.github/agents/pr-summarizer.agent.md`) to fetch PR data and generate the JSON file:

1. Open Copilot Chat in VS Code
2. Invoke `@pr-summarizer last 7 days`
3. The agent writes `reports/weekly-summary-YYYY-MM-DD.json`
4. Copy the JSON into the dashboard:
   ```bash
   cp reports/weekly-summary-*.json dashboard/public/data.json
   ```
5. The dev server hot-reloads automatically

## Project Structure

```
pr-summary/
├── .github/
│   ├── agents/pr-summarizer.agent.md   # Copilot custom agent
│   └── skills/fetch-org-prs/SKILL.md   # Reusable fetch skill
├── dashboard/
│   ├── public/data.json                # PR data (generated)
│   ├── src/
│   │   ├── main.jsx                    # Entry point
│   │   ├── App.jsx                     # Dashboard components
│   │   └── index.css                   # Styles (dark/light theme)
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
└── reports/                            # Generated summaries (JSON + Markdown)
```

## Building for Production

```bash
npm run build
npm run preview   # preview the production build locally
```

The built files go to `dashboard/dist/` and can be served from any static host.
