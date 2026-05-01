#!/usr/bin/env python3
"""
PR Summary Pipeline - fetches data from GitHub, groups by team, generates summaries.
Writes output to reports/ and dashboard/public/data.json
"""
import json, subprocess, sys, statistics, os
from datetime import datetime, timedelta, timezone

SINCE_DATE = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
END_DATE = datetime.now().strftime("%Y-%m-%d")
REPO = "BlueRiverTechnology/brt"

# --- Config ---
PROGRAMS = {
    "prg:shasta": {"id": "shasta", "name": "Shasta", "description": "See & Spray platform"},
    "prg:jupiter": {"id": "jupiter", "name": "Jupiter", "description": "Perception / autonomy"},
    "prg:adk": {"id": "adk", "name": "ADK", "description": "Application Development Kit"},
    "prg:dune": {"id": "dune", "name": "Dune", "description": "Autonomous operation"},
    "prg:mercury": {"id": "mercury", "name": "Mercury", "description": "Localization / mapping"},
    "prg:bumblebee": {"id": "bumblebee", "name": "Bumblebee", "description": "Harvest automation"},
    "prg:mesa": {"id": "mesa", "name": "Mesa", "description": "Mesa"},
    "prg:athena": {"id": "athena", "name": "Athena", "description": "Athena"},
    "prg:forestry": {"id": "forestry", "name": "Forestry", "description": "Forestry"},
}

ROBOTECH_AUTHORS = {
    "brt-brennan-coslett", "brt-sarah-newman", "jameskuszmaul-brt",
    "omarmanzano-brt", "debbieguo", "sanjaynarayanan-brt", "tamdo-brt", "rajshah-brt"
}

MBT_AUTHORS = {
    "foundation": ["maxwellgumley-brt", "brt-Naman-Gupta", "brian-griglak", "philsc",
        "pallavi-brt", "brt-colleen", "randy-schur-brt", "joshredding-brt", "austinroepke-brt"],
    "expand": ["kevinkreher-brt", "brt-amoagh-gopinath", "brt-brian-smartt", "brt-henry",
        "brt-alexei", "brtdylan", "ajaypbrt", "brt-clare-bagley", "richbiggs"],
    "unlock": ["kiran-mohan-brt", "zwheeler", "brtanuradhachandrashekar", "brt-clare-bagley", "richbiggs"],
    "enabling_tech": ["austinroepke-brt", "kevinkreher-brt", "brt-Yuchun-Liu", "ryancalhoun-brt"],
}

MBT_META = {
    "foundation": {"name": "Foundation", "description": "Common HW/SW platform for S&S"},
    "expand": {"name": "Expand", "description": "New geographies & crops"},
    "unlock": {"name": "Unlock", "description": "Increase S&S value for customers"},
    "enabling_tech": {"name": "Enabling Tech", "description": "Accelerate dev/deploy & quality"},
}

author_to_mbts = {}
for mbt_id, authors in MBT_AUTHORS.items():
    for a in authors:
        author_to_mbts.setdefault(a, []).append(mbt_id)

# --- Fetch functions ---
def gh_api_paginate(query):
    items = []
    page = 1
    while True:
        cmd = ["gh", "api", f"search/issues?q={query}&per_page=100&page={page}", "-q", ".items"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  Error page {page}: {r.stderr[:200]}", file=sys.stderr)
            break
        batch = json.loads(r.stdout) if r.stdout.strip() else []
        if not batch:
            break
        items.extend(batch)
        print(f"  page {page}: {len(batch)} items (total: {len(items)})")
        if len(batch) < 100:
            break
        page += 1
    return items

def gh_pr_list_loc(state, search):
    cmd = ["gh", "pr", "list", "--repo", REPO, "--state", state,
           "--search", search, "--json", "number,additions,deletions,changedFiles", "--limit", "500"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return {}
    data = json.loads(r.stdout) if r.stdout.strip() else []
    return {pr["number"]: pr for pr in data}

# --- Fetch all data ---
print(f"=== PR Summary Pipeline ===")
print(f"Window: {SINCE_DATE} to {END_DATE} (10 days)")
print()

print("Fetching merged PRs...")
merged_raw = gh_api_paginate(f"repo:{REPO}+type:pr+merged:>={SINCE_DATE}")
print(f"  Total: {len(merged_raw)}")

print("Fetching open PRs...")
open_raw = gh_api_paginate(f"repo:{REPO}+type:pr+is:open+created:>={SINCE_DATE}")
print(f"  Total: {len(open_raw)}")

print("Fetching LOC (merged)...")
merged_loc = gh_pr_list_loc("merged", f"merged:>={SINCE_DATE}")
print(f"  Got LOC for {len(merged_loc)}")

print("Fetching LOC (open)...")
open_loc = gh_pr_list_loc("open", f"created:>={SINCE_DATE}")
print(f"  Got LOC for {len(open_loc)}")

# --- Build PR records ---
def make_pr(item, loc_map, is_merged=True):
    number = item["number"]
    pr = {
        "number": number,
        "title": item["title"],
        "author": item["user"]["login"],
        "url": item["html_url"],
        "labels": [l["name"] for l in item.get("labels", [])],
    }
    if is_merged and item.get("closed_at") and item.get("created_at"):
        created = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        closed = datetime.fromisoformat(item["closed_at"].replace("Z", "+00:00"))
        pr["days_open"] = round((closed - created).total_seconds() / 86400, 1)
    loc = loc_map.get(number, {})
    if "additions" in loc:
        pr["additions"] = loc["additions"]
        pr["deletions"] = loc["deletions"]
        pr["changed_files"] = loc["changedFiles"]
    return pr

merged_prs = [make_pr(i, merged_loc, True) for i in merged_raw]
open_prs = [make_pr(i, open_loc, False) for i in open_raw]

# --- Group by team ---
teams = {}
unlabeled_merged = []
unlabeled_open = []

for pr in merged_prs:
    labels = [l for l in pr["labels"] if l.startswith("prg:")]
    if not labels:
        unlabeled_merged.append(pr)
    for label in labels:
        if label in PROGRAMS:
            tid = PROGRAMS[label]["id"]
            teams.setdefault(tid, {"merged": [], "open": []})
            teams[tid]["merged"].append(pr)

for pr in open_prs:
    labels = [l for l in pr["labels"] if l.startswith("prg:")]
    if not labels:
        unlabeled_open.append(pr)
    for label in labels:
        if label in PROGRAMS:
            tid = PROGRAMS[label]["id"]
            teams.setdefault(tid, {"merged": [], "open": []})
            teams[tid]["open"].append(pr)

# --- Split Robotech from Shasta ---
def is_robotech(pr):
    return pr["author"] in ROBOTECH_AUTHORS or pr["title"].lower().startswith("robotech:")

if "shasta" in teams:
    shasta_merged = [p for p in teams["shasta"]["merged"] if not is_robotech(p)]
    shasta_open = [p for p in teams["shasta"]["open"] if not is_robotech(p)]
    robo_merged = [p for p in teams["shasta"]["merged"] if is_robotech(p)]
    robo_open = [p for p in teams["shasta"]["open"] if is_robotech(p)]
    teams["shasta"]["merged"] = shasta_merged
    teams["shasta"]["open"] = shasta_open
    if robo_merged or robo_open:
        teams["robotech"] = {"merged": robo_merged, "open": robo_open}
        PROGRAMS["_robotech"] = {"id": "robotech", "name": "Robotech", "description": "Robotics platform (BSP, VPU, AOS)"}

# --- Compute MBT groups ---
def compute_mbt_groups(merged, opened):
    groups = {mbt_id: {"merged": [], "open": []} for mbt_id in MBT_AUTHORS}
    groups["other"] = {"merged": [], "open": []}
    for pr in merged:
        mbts = author_to_mbts.get(pr["author"])
        if mbts:
            for m in mbts:
                groups[m]["merged"].append(pr)
        else:
            groups["other"]["merged"].append(pr)
    for pr in opened:
        mbts = author_to_mbts.get(pr["author"])
        if mbts:
            for m in mbts:
                groups[m]["open"].append(pr)
        else:
            groups["other"]["open"].append(pr)
    return groups

# --- Stats helpers ---
def calc_avg(prs):
    days = [p["days_open"] for p in prs if "days_open" in p]
    return round(statistics.mean(days), 1) if days else None

def calc_median(prs):
    days = [p["days_open"] for p in prs if "days_open" in p]
    return round(statistics.median(days), 1) if days else None

# --- Write intermediate data for summary generation ---
# Save raw grouped data so we can inspect titles for summary writing
print("\nGrouping complete. Writing intermediate data...")

team_entries = []
for label, info in PROGRAMS.items():
    tid = info["id"]
    if tid in teams:
        team_entries.append({
            "id": tid,
            "name": info["name"],
            "description": info["description"],
            "merged_count": len(teams[tid]["merged"]),
            "open_count": len(teams[tid]["open"]),
            "avg_days_to_merge": calc_avg(teams[tid]["merged"]),
            "median_days_to_merge": calc_median(teams[tid]["merged"]),
            "summary": "__PLACEHOLDER__",
            "merged": teams[tid]["merged"],
            "open": teams[tid]["open"],
        })

if unlabeled_merged or unlabeled_open:
    team_entries.append({
        "id": "unlabeled", "name": "Unlabeled", "description": "No prg: label",
        "merged_count": len(unlabeled_merged), "open_count": len(unlabeled_open),
        "avg_days_to_merge": calc_avg(unlabeled_merged),
        "median_days_to_merge": calc_median(unlabeled_merged),
        "summary": "__PLACEHOLDER__",
        "merged": unlabeled_merged, "open": unlabeled_open,
    })

team_entries.sort(key=lambda t: t["merged_count"], reverse=True)

# Compute MBT groups for Shasta
mbt_groups_data = None
for t in team_entries:
    if t["id"] == "shasta":
        groups = compute_mbt_groups(t["merged"], t["open"])
        mbt_groups_data = []
        for mbt_id, meta in MBT_META.items():
            mg = groups[mbt_id]["merged"]
            og = groups[mbt_id]["open"]
            if mg or og:
                mbt_groups_data.append({
                    "id": mbt_id,
                    "name": meta["name"],
                    "description": meta["description"],
                    "merged_count": len(mg),
                    "open_count": len(og),
                    "summary": "__PLACEHOLDER__",
                    "titles_merged": [pr["title"] for pr in mg],
                    "titles_open": [pr["title"] for pr in og],
                })
        t["mbt_groups"] = mbt_groups_data
        break

# Global stats
all_merged_days = [p["days_open"] for p in merged_prs if "days_open" in p]
global_avg = round(statistics.mean(all_merged_days), 1) if all_merged_days else None

output = {
    "period": {"start": SINCE_DATE, "end": END_DATE},
    "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "repo": REPO,
    "summary": {
        "total_merged": len(merged_prs),
        "total_open": len(open_prs),
        "team_count": len(team_entries),
        "avg_days_to_merge": global_avg,
        "highlights": ["__PLACEHOLDER__"]
    },
    "teams": team_entries,
}

# Write intermediate file with titles for each team (for summary generation)
os.makedirs("reports", exist_ok=True)
with open("reports/pipeline-intermediate.json", "w") as f:
    json.dump(output, f, indent=2)

# Print team breakdown with sample titles for summary generation
print(f"\n=== Results: {len(merged_prs)} merged, {len(open_prs)} open, {len(team_entries)} teams ===\n")
for t in team_entries:
    print(f"--- {t['name']} ({t['merged_count']} merged, {t['open_count']} open) ---")
    titles = [pr["title"] for pr in t["merged"][:15]]
    for title in titles:
        print(f"  {title[:80]}")
    if len(t["merged"]) > 15:
        print(f"  ... and {len(t['merged']) - 15} more")
    print()

if mbt_groups_data:
    print("\n=== MBT Groups (Shasta) ===")
    for g in mbt_groups_data:
        print(f"\n  {g['name']} ({g['merged_count']} merged, {g['open_count']} open):")
        for title in g["titles_merged"][:8]:
            print(f"    {title[:80]}")
        if len(g["titles_merged"]) > 8:
            print(f"    ... and {len(g['titles_merged']) - 8} more")

print("\nIntermediate data written to reports/pipeline-intermediate.json")
print("Next: generate summaries and write final output.")
