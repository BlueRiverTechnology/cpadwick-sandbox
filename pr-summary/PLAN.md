# GitHub PR Summarizer — Plan

## Problem
Executive leadership wants visibility into what teams are working on without the overhead of recurring sync meetings that inevitably die off. GitHub is the actual record of work — PRs represent what's being built, reviewed, and shipped.

## Goal
A tool that generates a **weekly team-by-team PR summary report** someone can glance at and quickly understand what each team shipped, what's in-flight, and what's under review.

## Approach Options

### Option A: Copilot Prompt/Skills File (agent-driven)
- A `.prompt.md` file that instructs Copilot to use `gh` CLI to fetch PRs and generate a summary
- User runs it on-demand in Copilot Chat: `@workspace /pr-summary`
- **Pros**: Zero code to maintain, AI writes the narrative, easy to tweak format
- **Cons**: Manual trigger only (no automation), requires Copilot Chat context, depends on `gh` CLI auth

### Option B: Python CLI + AI summarization (hybrid)
- Python script that calls GitHub API (via `gh` CLI or `requests`) to fetch PRs
- Feeds raw PR data to an LLM (OpenAI/Anthropic/local) to generate the narrative summary
- Can be run via cron/CI for weekly automation
- **Pros**: Automatable, can email/Slack the report, reproducible
- **Cons**: More code, needs LLM API key for summarization

### Option C: Python CLI only (no AI)
- Python script that fetches PRs and generates a structured report using templates
- **Pros**: Simplest, no LLM dependency, fully deterministic
- **Cons**: Less readable narrative, just formatted data

## Recommended: Start with Option A, evolve to B

1. **Phase 1** — Build as a Copilot prompt file that uses `gh` CLI via terminal
   - Define the repos/orgs to scan
   - Define the report format
   - Test interactively in Copilot Chat
   - Low effort, high learning, immediate feedback

2. **Phase 2** — Extract the `gh` CLI logic into a Python script
   - Codify the data-fetching so it's repeatable
   - Output structured JSON that could feed into any formatter
   - This becomes the "data layer"

3. **Phase 3** — Add automation + distribution
   - GitHub Action or cron job runs the script weekly
   - Optionally pipe through an LLM for narrative polish
   - Post to Slack/email/wiki

## Configuration Needed
- **Org/repos to scan**: Which GitHub org? Which repos (or all repos in an org)?
- **Time window**: Last 7 days? Since last Monday?
- **Team mapping**: How do we group PRs by team? By repo? By GitHub team? By PR label?
- **PR states**: Merged only? Or also open/under review?
- **Report format**: Markdown? HTML email? Slack message?

## Report Structure (Draft)

```
# Weekly PR Summary — Week of April 21, 2026

## Team: LOF Multi-Modal Model
**5 PRs merged, 2 open**

### Merged
- **PR #111**: FurrowFormer pyfunc serving — Added MLflow wrapper for Databricks
  model serving with binary tensor transport and multi-GPU support.
- **PR #110**: Model registration scaffolding — ...
- **PR #109**: ...

### In Review
- **PR #112**: Field dataset normalization — ...

---

## Team: Field Planner
**2 PRs merged, 1 open**
...
```

## Decisions Made
1. **Org**: `github.deere.com/isg-digital-ai-research` (GitHub Enterprise)
2. **Team grouping**: repo == team
3. **PR states**: submitted (opened), open (in review), merged
4. **Audience**: Executive leadership — wants accomplishment-oriented narrative
5. **Approach**: Copilot agent + skill (`.github/agents/` + `.github/skills/`)
6. **Validated**: Search API returns 32 PRs for last 7 days — working

## Project Structure
```
.github/
├── agents/
│   └── pr-summarizer.agent.md    # The agent — invoke via agent picker
└── skills/
    └── fetch-org-prs/
        └── SKILL.md              # Reusable skill for fetching org PRs
```

## How to Use
1. Open the Copilot Chat agent picker and select **PR Summarizer**
2. Type a request like: "Generate the weekly PR summary" or "Summarize PRs from the last 2 weeks"
3. The agent will use `gh` CLI to fetch PRs, group by repo/team, and generate an executive summary

## Future Ideas
- Automation via GitHub Actions (scheduled weekly)
- Slack/email distribution of the report
- PR size/complexity indicators (lines changed, review time)
- Custom team-to-repo mapping (when repo != team)
