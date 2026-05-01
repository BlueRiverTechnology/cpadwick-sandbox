#!/usr/bin/env python3
"""
Step 2: Generate summaries and write final output.
Reads intermediate data and applies hand-crafted summaries.
"""
import json, os
from datetime import datetime, timezone

with open("reports/pipeline-intermediate.json") as f:
    output = json.load(f)

# --- Summaries based on actual PR title analysis ---
TEAM_SUMMARIES = {
    "shasta": "Shasta focused on platform reliability and expanding treatment capabilities this period. Major efforts went into sensor fault handling, SHARK test coverage, and preparing for canopy mode on Gen2 systems. The team also invested heavily in build infrastructure cleanup and VPU configuration management. **Shark/MQTT** (13 PRs) — expanded SHARK test coverage, fixed ReadyToLogs tests, and gated startup capabilities on MQTT translator readiness. **Camera & Sensors** (12 PRs) — fixed IMU stale fault reporting during initialization, cleaned up VR camera config fragments, and added MISSING_NOZZLE_TIP_MAPPING fault to sprayer. **VPU & BSP** (8 PRs) — bumped VPU1 dev image size, deduplicated Python version variables, and separated output_base locations for CI configurations. **Build/Infra** (10 PRs) — migrated dependencies to bzlmod, updated CAN messages, and cleaned up unused configs. **SAM & Sprayer Logic** (6 PRs) — added update_baseline script for RSW SAM and implemented support for canopy mode in Gen2 systems.",

    "jupiter": "Jupiter advanced its ML training pipeline and perception testing infrastructure significantly. The Gretzky team shipped multiscale disparity predictions and created the v13.5 training dataset, while Galileo hardened automated test suites. A supply chain security incident (compromised PyPI lightning package) was quickly mitigated. **Gretzky/ML** (22 PRs) — enabled multiscale disparity predictions for joint LR training, updated class counts for ONNX conversion, created v13.5 training dataset scripts, and fixed implement mask timeout issues. **Galileo/Testing** (18 PRs) — BSM test bug fixes, updated YAML names, removed 2.0 cases, and uploaded mcap before saving steps history. **Perception Core** (12 PRs) — added lidar extrinsic checks, tracking IoU polygon utilities, and fixed delta file inputs in subsystem replay. **DevOps/Dependencies** (8 PRs) — migrated nlohmann_json and opentelemetry-cpp to bzlmod, removed compromised lightning dependency from supply chain attack. **MCAP/Data** (5 PRs) — enabled mcap compression in SDC and improved recording infrastructure.",

    "adk": "ADK drove a major third-party dependency migration to bzlmod this period, cleaning up the monorepo build graph substantially. On the product side, the team shipped embedded hardware fixes (I2C, EEPROM), improved developer tooling with Chart Calibration UI improvements, and advanced MCAP recording capabilities. **Build Migration** (12 PRs) — migrated pybind, sqlite, curl, snappy, gRPC, and boringssl to bzlmod, cleaning up the WORKSPACE cascade. **Hardware/Embedded** (8 PRs) — fixed I2C write bugs, EEPROM write issues, decompand restructure, and added heartbeat enablement. **MCAP/Recording** (7 PRs) — removed redundant UpdateMetadata API from TopicReencoder, split mcap replay and record support. **Developer Tools** (8 PRs) — Chart Calibration UI split into separate apps, Epiviz warning for merged MCAPs without common frame index, and updated getting started guide for rebase workflows. **Transcoder** (4 PRs) — refactored mercury transcoder logic and increased map size.",

    "robotech": "Robotech shipped BSP 3.2.1 across both VPU generations and made meaningful progress on memory optimization for the b-series platform. Key safety improvements include flash ratchet downgrade prevention and EFI major version validation. The team also reduced camera message frequencies to ease VPU2 resource pressure. **BSP Releases** (10 PRs) — shipped BSP 3.2.1 for VPU1 & VPU2, added EFI major version check to flash_vpu, prevented ratchet downgrade in flash_vpu2. **Memory Optimization** (4 PRs) — shrunk MqttEmulator and PduQueue memory usage for b-series. **MQTT/Messaging** (5 PRs) — bumped max MQTT MessagePayload size, tuned down VPU2 camera message frequencies. **Build/Tooling** (8 PRs) — converted generate_dir_file to Python, specified go_sdk version earlier, separated CI output_base locations. **AOS/Realtime** (6 PRs) — fixed SimulatedSender DoSend for realtime checks, cleaned up flatbuffer copies in capabilities modules.",

    "unlabeled": "Cross-cutting infrastructure work dominated this period, primarily the monorepo-wide migration of third-party dependencies from WORKSPACE to bzlmod. This foundational effort touches every team and will simplify builds going forward. **DevOps/Bzlmod** (15 PRs) — major migration effort moving glog, glfw, opengl, flatbuffers, and other deps to bzlmod while dropping unused workspace dependencies. **Build Infrastructure** (6 PRs) — updated crosstool wrapper for Python 3.13, fixed platform_suffix for vpu2_jp5, added warm-cache index.json schema. **Tooling** (4 PRs) — fixed vpu_exec working directory for remote execution, fixed profiling tool paths in vpu_nsight/vpu_nsys.",

    "dune": "Dune made substantial progress on replay infrastructure, getting subsystem replay working with autocalibration and EMU replay producing metrics to S3. The team also refined autonomy logic around velocity buffering and geojson handling. **Replay Infrastructure** (7 PRs) — got dune subsystem replay working with autocalibration, EMU replay with metrics/S3, and splitted mcap replay+record support. **Autonomy Logic** (5 PRs) — extended velocity buffer for ego and target stops, fixed geojson 3D offset, removed unnecessary atomic in sparkai_proxy. **Recording/Data** (4 PRs) — set event mcap chunking to 45s, added VADC limit topics to recorder. **CI/Build** (3 PRs) — improved GHA to remove explicit declarations, synced dav display 0.1.13-2.",

    "mercury": "Mercury advanced visual odometry metrics and ported them to ReSim for automated evaluation. The team also implemented the VADC protocol and began gamma data collection work. **Visual Odometry** (4 PRs) — fixed extrinsics batch optimizer, ported VO metrics to ReSim, and added more stats to resim with fixed plots. **VADC Protocol** (3 PRs) — implemented VADC protocol and added explicit cleanup of singletons holding PubSubModule references. **Localization** (3 PRs) — localization fixes and map test assertion improvements. **Data Collection** (2 PRs) — gamma data collection work and simplified OpenImu publishing logic.",

    "mesa": "3 merged and 1 open PRs this period. Work focused on factoring the compute module out of Arrow and adding schema/data fields to rti_dds_to_arrow_reader with chunking support.",

    "bumblebee": "2 merged and 4 open PRs this period. Infrastructure changes including CUDA build flag migration from #ifdef to #if ENABLE_CUDA and clang toolchain path cleanup.",

    "athena": "1 merged PR this period — initial configuration setup for the Athena program.",
}

MBT_SUMMARIES = {
    "foundation": "Platform reliability and sensor infrastructure — fixed camera IMU stale fault reporting, added MISSING_NOZZLE_TIP_MAPPING fault to sprayer, bumped VPU1 dev image size, and updated CAN BoomTracInformation4 messages. Also cleaned up VR camera configs and gated startup capabilities on MQTT translator readiness.",
    "expand": "Crop model development and data tooling — supported Implement MTG, built SampleVerse content package messaging, enhanced Raven upload status checks, and added fill method between sparse map vertices. Also removed obsolete ingest_machine_logs.py and worked on prompt_utilities enhancements.",
    "unlock": "Customer value features — added support for canopy mode in Gen2 systems, rewrote boomtrac_mode_module tests, and corrected misleading BSP security check result text.",
    "enabling_tech": "CI/test infrastructure — updated Buildkite parameters for elastic stack, fixed CORS for BSP/equipment signers, configured LPB21 for SHARK testing, and added wireguard DNS for baker-lpb21.",
}

# Apply summaries
for t in output["teams"]:
    if t["id"] in TEAM_SUMMARIES:
        t["summary"] = TEAM_SUMMARIES[t["id"]]
    
    if t["id"] == "shasta" and "mbt_groups" in t:
        for g in t["mbt_groups"]:
            if g["id"] in MBT_SUMMARIES:
                g["summary"] = MBT_SUMMARIES[g["id"]]
            # Remove temporary title fields
            g.pop("titles_merged", None)
            g.pop("titles_open", None)

# Highlights
output["summary"]["highlights"] = [
    "Major bzlmod migration across the monorepo — dozens of third-party deps moved off WORKSPACE files",
    "BSP 3.2.1 shipped for VPU1 & VPU2 with flash safety improvements (ratchet downgrade prevention)",
    "Gretzky ML training advanced with multiscale disparity and v13.5 dataset creation",
]

# Write final output
with open(f"reports/weekly-summary-{output['period']['end']}.json", "w") as f:
    json.dump(output, f, indent=2)

with open("dashboard/public/data.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Done! Written to:")
print(f"  reports/weekly-summary-{output['period']['end']}.json")
print(f"  dashboard/public/data.json")
print(f"\nPeriod: {output['period']['start']} to {output['period']['end']}")
print(f"Total: {output['summary']['total_merged']} merged, {output['summary']['total_open']} open, {output['summary']['team_count']} teams")
print(f"\nTeam breakdown:")
for t in output["teams"]:
    print(f"  {t['name']}: {t['merged_count']} merged, {t['open_count']} open")
    if t["id"] == "shasta" and "mbt_groups" in t:
        for g in t["mbt_groups"]:
            print(f"    └ {g['name']}: {g['merged_count']} merged, {g['open_count']} open")
