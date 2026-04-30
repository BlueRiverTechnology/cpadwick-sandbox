# Weekly Engineering Summary — Week of 2026-04-20

**Period**: 2026-04-20 to 2026-04-30 | **347 merged, 212 open** across **10 teams** | avg 10.3d to merge

## Highlights

- Infrastructure modernized the build system with 14+ bzlmod migrations (gRPC, protobuf, gtest, and more), advancing Bazel 8 readiness across the monorepo.
- Robotech shipped BSP 3.2.1 for both VPU platforms plus the full Phelps MY27 SOP configuration matrix (14 PRs), now broken out as its own team from Shasta.
- Jupiter advanced the Gretzky depth model with multiscale disparity predictions and a new v13.5 training dataset, while Galileo stabilized its automated test pipeline.

## Team Reports

### Shasta
102 merged | 66 in review | 15.5d avg, 5.8d median

> Shasta focused on five main work-streams this period. **Test infrastructure** (12 PRs): Extensive SHARK test automation — automated ReadyToLogs, CameraFirmwareVersionMismatch, LiveVideo interactive tests, and added new BootstrapCalibration and InstallGrabler tests. **Python/Bazel toolchain** (6 PRs): Migrated default Python version handling, added python3.10 config flag, and deduplicated Python version variables to unblock Python 3.13 upgrade. **Sprayer & diagnostics** (8 PRs): Added MISSING_NOZZLE_TIP_MAPPING fault, disabled weed pressure in Variable Rate mode, fixed realtime malloc in capabilities watcher, and hardened camera IMU stale fault reporting. **Build/CI** (5 PRs): Updated Buildkite git mirrors parameters, fixed PR approval webhook retry, and separated output_base locations for CI. **Cleanup & maintenance** (10+ PRs): Deleted obsolete boomtrac_mode_forwarder, removed ingest_machine_logs.py, extracted MakeDocLog library, and several reverts for stability.

- **shasta**: 59 PRs — [#11781](https://github.com/BlueRiverTechnology/brt/pull/11781) [#11768](https://github.com/BlueRiverTechnology/brt/pull/11768) [#11755](https://github.com/BlueRiverTechnology/brt/pull/11755) [#11748](https://github.com/BlueRiverTechnology/brt/pull/11748) [#11725](https://github.com/BlueRiverTechnology/brt/pull/11725) +54 more
- **shark**: 18 PRs — [#11728](https://github.com/BlueRiverTechnology/brt/pull/11728) [#11683](https://github.com/BlueRiverTechnology/brt/pull/11683) [#11571](https://github.com/BlueRiverTechnology/brt/pull/11571) [#11546](https://github.com/BlueRiverTechnology/brt/pull/11546) [#11537](https://github.com/BlueRiverTechnology/brt/pull/11537) +13 more
- **(other)**: 17 PRs — [#11670](https://github.com/BlueRiverTechnology/brt/pull/11670) [#11642](https://github.com/BlueRiverTechnology/brt/pull/11642) [#11578](https://github.com/BlueRiverTechnology/brt/pull/11578) [#11550](https://github.com/BlueRiverTechnology/brt/pull/11550) [#11520](https://github.com/BlueRiverTechnology/brt/pull/11520) +12 more
- fix: Updating Buildkite parameter (2nd attempt) (ryancalhoun-brt) [#11620](https://github.com/BlueRiverTechnology/brt/pull/11620)
- fix: Bootstrap dl-core-seedling with Artifactory credential (mrmod) [#11491](https://github.com/BlueRiverTechnology/brt/pull/11491)
- fix: CORS for bsp-signer and equipment-signer (ryancalhoun-brt) [#11362](https://github.com/BlueRiverTechnology/brt/pull/11362)
- Revert "shasta: add CombinedSWFaults SHARK test (#10563)" (mrmod) [#11672](https://github.com/BlueRiverTechnology/brt/pull/11672)
- Revert "jupiter: Lidar extrinsic check in (#11545)" (mrmod) [#11669](https://github.com/BlueRiverTechnology/brt/pull/11669)
- buildkite: Git mirrors paramter for elastic stack (ryancalhoun-brt) [#11614](https://github.com/BlueRiverTechnology/brt/pull/11614)
- PRO-19807: Remove obsolete ingest_machine_logs.py (kevinkreher-brt) [#11556](https://github.com/BlueRiverTechnology/brt/pull/11556)
- aerial: rule to push value to AWS secret (brt-alexei) [#10071](https://github.com/BlueRiverTechnology/brt/pull/10071)
- 🔄 Add CloudWatch alarm manager Lambda for image search feature extractor (ajaypbrt) [#11827](https://github.com/BlueRiverTechnology/brt/pull/11827)
- 🔄 shasta: automate USLs_AutoCopy_toNasUponCompletition SHARK test (W7NIIIF-deere) [#11806](https://github.com/BlueRiverTechnology/brt/pull/11806)
- 🔄 shasta: Delete superfluous copy of sashimi code (philsc) [#11798](https://github.com/BlueRiverTechnology/brt/pull/11798)
- 🔄 +63 more open PRs

### Jupiter
76 merged | 45 in review | 10.8d avg, 1.1d median

> Jupiter advanced on four key fronts. **Gretzky depth model** (14 PRs): Enabled multiscale disparity predictions for joint LR training, separated SkySupervisedLoss from stereo consistency loss, fixed implement mask timeout, and created v13.5 training dataset with new annotation tooling. **Galileo automated testing** (8 PRs): Fixed duplicate/invalid YAML steps, refactored BSM tests, increased mcap_io test timeouts, and added exclude-filter support for rerun_failed_github_tests. **Platform & recording** (6 PRs): Enabled mcap compression in SDC, added lidar extrinsic check-in, fixed subsystem replay delta file inputs, and added JQ triggering message recording. **Tracking & perception** (4 PRs): Added IoU polygon utilities for object tracking, fixed single camera replacement bug, and fixed object_locator_metrics steady_clock underflow.

- **gretzky**: 19 PRs — [#11780](https://github.com/BlueRiverTechnology/brt/pull/11780) [#11778](https://github.com/BlueRiverTechnology/brt/pull/11778) [#11723](https://github.com/BlueRiverTechnology/brt/pull/11723) [#11698](https://github.com/BlueRiverTechnology/brt/pull/11698) [#11696](https://github.com/BlueRiverTechnology/brt/pull/11696) +14 more
- **(other)**: 19 PRs — [#11714](https://github.com/BlueRiverTechnology/brt/pull/11714) [#11670](https://github.com/BlueRiverTechnology/brt/pull/11670) [#11573](https://github.com/BlueRiverTechnology/brt/pull/11573) [#11558](https://github.com/BlueRiverTechnology/brt/pull/11558) [#11557](https://github.com/BlueRiverTechnology/brt/pull/11557) +14 more
- **jupiter**: 15 PRs — [#11715](https://github.com/BlueRiverTechnology/brt/pull/11715) [#11713](https://github.com/BlueRiverTechnology/brt/pull/11713) [#11702](https://github.com/BlueRiverTechnology/brt/pull/11702) [#11671](https://github.com/BlueRiverTechnology/brt/pull/11671) [#11624](https://github.com/BlueRiverTechnology/brt/pull/11624) +10 more
- **galileo**: 9 PRs — [#11765](https://github.com/BlueRiverTechnology/brt/pull/11765) [#11681](https://github.com/BlueRiverTechnology/brt/pull/11681) [#11648](https://github.com/BlueRiverTechnology/brt/pull/11648) [#11592](https://github.com/BlueRiverTechnology/brt/pull/11592) [#11448](https://github.com/BlueRiverTechnology/brt/pull/11448) +4 more
- devops: Remove one more compromised lightning dependency (perfinion) [#11808](https://github.com/BlueRiverTechnology/brt/pull/11808)
- devops: Migrate nlohmann_json, opentelemetry-cpp to bzlmod (perfinion) [#11753](https://github.com/BlueRiverTechnology/brt/pull/11753)
- adk: Add BSP Compatibility to APPFS Bundle (gregleonberg-brt) [#11109](https://github.com/BlueRiverTechnology/brt/pull/11109)
- adk: Switch from #ifdef ENABLE_CUDA to #if ENABLE_CUDA (anivegesana) [#8546](https://github.com/BlueRiverTechnology/brt/pull/8546)
- third_party: Disable PyPI lightning compromised in Supply Chain Attack (anivegesana) [#11805](https://github.com/BlueRiverTechnology/brt/pull/11805)
- [JQA-1297]:Fix duplicate and invalid steps in galileo-automated-tests.yaml and refactor BSM tests (pjlorentzBRT) [#11706](https://github.com/BlueRiverTechnology/brt/pull/11706)
- Revert "shasta: add CombinedSWFaults SHARK test (#10563)" (mrmod) [#11672](https://github.com/BlueRiverTechnology/brt/pull/11672)
- Revert "jupiter: Lidar extrinsic check in (#11545)" (mrmod) [#11669](https://github.com/BlueRiverTechnology/brt/pull/11669)
- [ROBOT-4187]: fix object_locator_metrics steady_clock underflow and multi_frame_latency init bug (ziyang-brt) [#11591](https://github.com/BlueRiverTechnology/brt/pull/11591)
- [ROBOT-4161]: detection_filterer - use node clock for replay-aware latency metrics (ziyang-brt) [#11360](https://github.com/BlueRiverTechnology/brt/pull/11360)
- [ROBOT-4160]: object_localizer - use node clock for replay-aware latency metrics (ziyang-brt) [#11359](https://github.com/BlueRiverTechnology/brt/pull/11359)
- [ROBOT-4162]: grid_map_object_aggregator - use replay-aware system clock for latency… (ziyang-brt) [#11358](https://github.com/BlueRiverTechnology/brt/pull/11358)
- [ROBOT-4158]: zone_comparator - use node clock for latency metrics instead of system… (ziyang-brt) [#11355](https://github.com/BlueRiverTechnology/brt/pull/11355)
- [ROBOT-4146]: migrate point_cloud_processor metrics to ADK FrameWindowPublisher pattern (ziyang-brt) [#11236](https://github.com/BlueRiverTechnology/brt/pull/11236)
- 🔄 gretzky: Fix em plotting interpolation (deanb-brt) [#11831](https://github.com/BlueRiverTechnology/brt/pull/11831)
- 🔄 gretzky: Embedded Metrics Telemetry, Debug Dataset, and Dashboard fix (Alex17Li) [#11826](https://github.com/BlueRiverTechnology/brt/pull/11826)
- 🔄 [ADK-4273] Fix flaky jupiter single camera replacement test (rickdynarski-brt) [#11821](https://github.com/BlueRiverTechnology/brt/pull/11821)
- 🔄 +42 more open PRs

### ADK
49 merged | 25 in review | 10.2d avg, 2.0d median

> ADK shipped improvements across five areas. **Epiviz & calibration UI** (8 PRs): Added warning for merged MCAPs without common frame index, rebuilt Chart Calibration UI as separate apps with 3D OpenGL coverage, memory optimizations, and added Jupiter implement VPU delta config. **Hardware interfaces** (6 PRs): Fixed I2C write and EEPROM write bugs, improved dogbone EEPROM handling, added SHA256 model engine file checks, and added large file streaming to autocal. **Bzlmod migration** (5 PRs): Migrated pybind, sqlite, curl, snappy, nlohmann_json, and opentelemetry-cpp to bzlmod as part of Bazel 8 readiness. **Direct-to-Host IoT** (3 PRs): Enabled VPU direct communication with JD AWS Host broker with production cert paths. **COLMAP & 3D** (3 PRs): Parallelized colmap verification/BA, added scale/threading knobs, and refactored cuda_correspondence_test.

- **adk**: 18 PRs — [#11675](https://github.com/BlueRiverTechnology/brt/pull/11675) [#11607](https://github.com/BlueRiverTechnology/brt/pull/11607) [#11606](https://github.com/BlueRiverTechnology/brt/pull/11606) [#11605](https://github.com/BlueRiverTechnology/brt/pull/11605) [#11602](https://github.com/BlueRiverTechnology/brt/pull/11602) +13 more
- **(other)**: 16 PRs — [#11688](https://github.com/BlueRiverTechnology/brt/pull/11688) [#11651](https://github.com/BlueRiverTechnology/brt/pull/11651) [#11621](https://github.com/BlueRiverTechnology/brt/pull/11621) [#11604](https://github.com/BlueRiverTechnology/brt/pull/11604) [#11432](https://github.com/BlueRiverTechnology/brt/pull/11432) +11 more
- devops: Migrate pybind, sqlite, curl, snappy to bzlmod (perfinion) [#11793](https://github.com/BlueRiverTechnology/brt/pull/11793)
- devops: Migrate nlohmann_json, opentelemetry-cpp to bzlmod (perfinion) [#11753](https://github.com/BlueRiverTechnology/brt/pull/11753)
- devops: remove cuda-11.4/include from clang toolchain -isystem path (rickdynarski-brt) [#11647](https://github.com/BlueRiverTechnology/brt/pull/11647)
- mercury: Refactor transcoder logic and increase map size (DanielMovsesyanBRT) [#11720](https://github.com/BlueRiverTechnology/brt/pull/11720)
- mercury: Fix day/night mode logic for sunset crossing midnight UTC (DanielMovsesyanBRT) [#11639](https://github.com/BlueRiverTechnology/brt/pull/11639)
- [ADK-4238]: I2C write fix (#11590) (chuckstanski-brt) [#11677](https://github.com/BlueRiverTechnology/brt/pull/11677)
- [ADK-4238]: I2C write fix (chuckstanski-brt) [#11590](https://github.com/BlueRiverTechnology/brt/pull/11590)
- [ADK-4229]: Bug: EEPROM Write bug (#11499) (pgrice) [#11673](https://github.com/BlueRiverTechnology/brt/pull/11673)
- [ADK-4229]: Bug: EEPROM Write bug (chuckstanski-brt) [#11499](https://github.com/BlueRiverTechnology/brt/pull/11499)
- [ADK-4260] mcap: Remove redundant UpdateMetadata API from TopicReencoder (wingiptam-brt) [#11730](https://github.com/BlueRiverTechnology/brt/pull/11730)
- dune: Replay and Record working with splitted mcaps (LuisIvSandoval) [#11660](https://github.com/BlueRiverTechnology/brt/pull/11660)
- [ADK-4233] Direct to Host: Enable VPU direct communication with JD AWS Host broker (rakeshdugad-brt) [#11586](https://github.com/BlueRiverTechnology/brt/pull/11586)
- [ADK-4232] Update host path for production: rebase, point to prod certs, update thing name to "vpu" (rakeshdugad-brt) [#11577](https://github.com/BlueRiverTechnology/brt/pull/11577)
- gretzky: Uncomment and fix EM integration test (Alex17Li) [#11421](https://github.com/BlueRiverTechnology/brt/pull/11421)
- mesa: Add schema and data fields to rti_dds_to_arrow_reader; add chunking (anivegesana) [#11379](https://github.com/BlueRiverTechnology/brt/pull/11379)
- 🔄 [ADK-4278] Fix flaky rcs_client_test by using OS-assigned ports (rickdynarski-brt) [#11829](https://github.com/BlueRiverTechnology/brt/pull/11829)
- 🔄 [ADK-4271] Add VPU client abstraction (amaharshi) [#11825](https://github.com/BlueRiverTechnology/brt/pull/11825)
- 🔄 [ADK-4290] Add ImGui app harness  (amaharshi) [#11824](https://github.com/BlueRiverTechnology/brt/pull/11824)
- 🔄 +22 more open PRs

### Robotech
43 merged | 24 in review | 6.2d avg, 5.3d median

> Robotech delivered across three main streams. **BSP & VPU flashing** (8 PRs): Shipped BSP 3.2.1 for VPU1 and VPU2, added EFI major version check and ratchet downgrade prevention to flash tools, added rev7 VPU1 support, and switched to dev-signed BSP when available. **Phelps MY27 configurations** (14 PRs): Landed the full matrix of Phelps MY27 SOP configs across 30k/36k/40k row widths and 15e/15i/20e/20i spacing variants. **B-series & AOS** (7 PRs): Shrunk MqttEmulator and PduQueue memory usage for b-series, tuned VPU2 camera message frequencies, bumped max MQTT payload size, cleaned up flatbuffer copies, and fixed realtime checks in SimulatedSender. **JetPack 6 prep** (4 open PRs): Active work on JP6 rootfs config, TensorRT/inference support, model conversion, and L4T version detection — not yet merged.

- **(other)**: 21 PRs — [#11325](https://github.com/BlueRiverTechnology/brt/pull/11325) [#11324](https://github.com/BlueRiverTechnology/brt/pull/11324) [#11323](https://github.com/BlueRiverTechnology/brt/pull/11323) [#11322](https://github.com/BlueRiverTechnology/brt/pull/11322) [#11321](https://github.com/BlueRiverTechnology/brt/pull/11321) +16 more
- **shasta**: 15 PRs — [#11760](https://github.com/BlueRiverTechnology/brt/pull/11760) [#11759](https://github.com/BlueRiverTechnology/brt/pull/11759) [#11528](https://github.com/BlueRiverTechnology/brt/pull/11528) [#11500](https://github.com/BlueRiverTechnology/brt/pull/11500) [#11496](https://github.com/BlueRiverTechnology/brt/pull/11496) +10 more
- **robotech**: 4 PRs — [#11638](https://github.com/BlueRiverTechnology/brt/pull/11638) [#11633](https://github.com/BlueRiverTechnology/brt/pull/11633) [#11405](https://github.com/BlueRiverTechnology/brt/pull/11405) [#11367](https://github.com/BlueRiverTechnology/brt/pull/11367)
- shark: adk: Add basic startup test (brt-brennan-coslett) [#10647](https://github.com/BlueRiverTechnology/brt/pull/10647)
- SHARK: Add B100 health check  (omarmanzano-brt) [#9892](https://github.com/BlueRiverTechnology/brt/pull/9892)
- aos: Make SimulatedSender::DoSend handle realtime checks correctly (jameskuszmaul-brt) [#11479](https://github.com/BlueRiverTechnology/brt/pull/11479)
- 🔄 shasta: add jp6 red flag model (tamdo-brt) [#11828](https://github.com/BlueRiverTechnology/brt/pull/11828)
- 🔄 shasta: add JP6 TensorRT/inference support and JP5 vs JP6 L4T version detection (tamdo-brt) [#11823](https://github.com/BlueRiverTechnology/brt/pull/11823)
- 🔄 shasta: add JP6 rootfs config and handle merged-usr layout via remap_paths (tamdo-brt) [#11822](https://github.com/BlueRiverTechnology/brt/pull/11822)
- 🔄 +21 more open PRs

### Unlabeled
29 merged | 28 in review | 4.0d avg, 0.9d median

> Cross-cutting infrastructure dominated unlabeled PRs. **Bzlmod migration** (14 PRs): Massive Bazel modernization effort by perfinion — migrated gRPC, boringssl, protobuf, glog, gtest, gflags, libjpeg-turbo, libpng, zlib, bazel_latex, rules_m4/bison/flex, glfw, and OpenGL to bzlmod, plus removed dead workspace deps. **DevOps tooling** (5 PRs): Improved vpu_exec remote execution, fixed PR approval dismissal for empty commits, updated crosstool wrapper for python3.13, and added warm-cache index.json schema. **Supply chain security** (2 PRs): Disabled compromised PyPI lightning package after supply chain attack detection.

- **devops**: 16 PRs — [#11786](https://github.com/BlueRiverTechnology/brt/pull/11786) [#11784](https://github.com/BlueRiverTechnology/brt/pull/11784) [#11749](https://github.com/BlueRiverTechnology/brt/pull/11749) [#11727](https://github.com/BlueRiverTechnology/brt/pull/11727) [#11653](https://github.com/BlueRiverTechnology/brt/pull/11653) +11 more
- **(other)**: 6 PRs — [#11626](https://github.com/BlueRiverTechnology/brt/pull/11626) [#11568](https://github.com/BlueRiverTechnology/brt/pull/11568) [#11506](https://github.com/BlueRiverTechnology/brt/pull/11506) [#11392](https://github.com/BlueRiverTechnology/brt/pull/11392) [#11159](https://github.com/BlueRiverTechnology/brt/pull/11159) +1 more
- adk: Fix Open3D debug build, use std::filesystem in FileSystem.cpp (amaharshi) [#11598](https://github.com/BlueRiverTechnology/brt/pull/11598)
- adk: fix profiling tool paths in vpu_nsight, vpu_nsys (alexeyromanovskiy-brt) [#11559](https://github.com/BlueRiverTechnology/brt/pull/11559)
- galileo: upload mcap before saving steps history (pjlorentzBRT) [#11722](https://github.com/BlueRiverTechnology/brt/pull/11722)
- third_party: Migrate glfw and opengl to BzlMod [ADK-4256] (amaharshi) [#11701](https://github.com/BlueRiverTechnology/brt/pull/11701)
- bumblebee: ignore directories not supported on bazel 7.6.1 (AASanchezA) [#11271](https://github.com/BlueRiverTechnology/brt/pull/11271)
- shared: add readme and update documentation for shared stop framework (brt-chris) [#11255](https://github.com/BlueRiverTechnology/brt/pull/11255)
- reprogramming: remove skip-phy-fw-update workaround (tamdo-brt) [#10110](https://github.com/BlueRiverTechnology/brt/pull/10110)
- 🔄 [ROBOT-4061] Create container for warm cache download, will be used as an initContainer (andrewring) [#11830](https://github.com/BlueRiverTechnology/brt/pull/11830)
- 🔄 mercury: Enhance embedded resources generation with aggregate functions for C++ and Python (DanielMovsesyanBRT) [#11814](https://github.com/BlueRiverTechnology/brt/pull/11814)
- 🔄 shasta: system pump pressure on spyglass (cesarcordero25) [#11807](https://github.com/BlueRiverTechnology/brt/pull/11807)
- 🔄 +25 more open PRs

### Dune
25 merged | 15 in review | 3.2d avg, 1.0d median

> Dune progressed on autonomy and simulation. **Replay & metrics** (7 PRs): Major replay overhaul — EMU replay with metrics/S3 upload, split mcap record/replay, auto-generated experiences, and subsystem replay autocalibration. **Safety & motion** (4 PRs): Extended velocity buffer for ego and target stops, added VADC limit topics to recorder, and reworked deceleration message timing. **Simulation** (3 PRs): Reworked sim launching, improved GHA to remove explicit declarations, and sped up safety_bubble/dds_tf2 tests with virtual clocks. **DAV display** (2 PRs): Synced DAV display 0.1.13-2 and added collision checker parameter initialization.

- **dune**: 18 PRs — [#11809](https://github.com/BlueRiverTechnology/brt/pull/11809) [#11767](https://github.com/BlueRiverTechnology/brt/pull/11767) [#11658](https://github.com/BlueRiverTechnology/brt/pull/11658) [#11608](https://github.com/BlueRiverTechnology/brt/pull/11608) [#11585](https://github.com/BlueRiverTechnology/brt/pull/11585) +13 more
- **(other)**: 4 PRs — [#11619](https://github.com/BlueRiverTechnology/brt/pull/11619) [#11418](https://github.com/BlueRiverTechnology/brt/pull/11418) [#11262](https://github.com/BlueRiverTechnology/brt/pull/11262) [#11147](https://github.com/BlueRiverTechnology/brt/pull/11147)
- devops: Migrate nlohmann_json, opentelemetry-cpp to bzlmod (perfinion) [#11753](https://github.com/BlueRiverTechnology/brt/pull/11753)
- adk: (and dune) speed up safety_bubble and dds_tf2 tests with virtual clocks (mattelsey-brt) [#11509](https://github.com/BlueRiverTechnology/brt/pull/11509)
- dune/replay: resolve experience config paths against workspace root s… (RubenMovsesyan) [#11441](https://github.com/BlueRiverTechnology/brt/pull/11441)
- 🔄 dune: Bridging collision checker outputs via mqtt_proxy (brt-nicolas-delima) [#11810](https://github.com/BlueRiverTechnology/brt/pull/11810)
- 🔄 [ADK-4150] Revert QOS changes made with 11147 and 11711 (rickdynarski-brt) [#11800](https://github.com/BlueRiverTechnology/brt/pull/11800)
- 🔄 dune: Adding collision checker parameters initialization (brt-nicolas-delima) [#11790](https://github.com/BlueRiverTechnology/brt/pull/11790)
- 🔄 +12 more open PRs

### Mercury
17 merged | 5 in review | 7.1d avg, 1.3d median

> Mercury made progress on localization and data collection. **Visual odometry & localization** (5 PRs): Fixed VO extrinsics batch optimizer, various localization fixes, ported VO metrics to resim, and added a new shared universal wheel odometer. **VADC protocol** (2 PRs): Implemented VADC protocol and refactored turf-autonomy Domain Participant changes. **Data collection & resim** (4 PRs): Gamma data collection work, added more resim stats with plot fixes, map test assertion handling, and singleton cleanup for PubSubModule references. **Infrastructure** (2 PRs): Pre-commit script for ENABLE_CUDA ifdef migration and bzlmod dependency updates.

- **mercury**: 12 PRs — [#11758](https://github.com/BlueRiverTechnology/brt/pull/11758) [#11708](https://github.com/BlueRiverTechnology/brt/pull/11708) [#11707](https://github.com/BlueRiverTechnology/brt/pull/11707) [#11652](https://github.com/BlueRiverTechnology/brt/pull/11652) [#11617](https://github.com/BlueRiverTechnology/brt/pull/11617) +7 more
- devops: Migrate nlohmann_json, opentelemetry-cpp to bzlmod (perfinion) [#11753](https://github.com/BlueRiverTechnology/brt/pull/11753)
- devops: Add pre-commit script that replaces `#ifdef ENABLE_CUDA` with `#if ENABLE_CUDA` (anivegesana) [#11531](https://github.com/BlueRiverTechnology/brt/pull/11531)
- [ADK-4186] turf-autonomy Domain Participant changes (rickdynarski-brt) [#11711](https://github.com/BlueRiverTechnology/brt/pull/11711)
- Revert "[ROBOT-4180] Enable mcap compression in SDC (#11573)" (mrmod) [#11670](https://github.com/BlueRiverTechnology/brt/pull/11670)
- adk: Switch from #ifdef ENABLE_CUDA to #if ENABLE_CUDA (anivegesana) [#8546](https://github.com/BlueRiverTechnology/brt/pull/8546)
- 🔄 [ADK-4150] Revert QOS changes made with 11147 and 11711 (rickdynarski-brt) [#11800](https://github.com/BlueRiverTechnology/brt/pull/11800)
- 🔄 mercury: Add delta configuration support for data collection nodes (DanielMovsesyanBRT) [#11792](https://github.com/BlueRiverTechnology/brt/pull/11792)
- 🔄 mercury: Refactor resim datasets, change metrics (brt-chris) [#11785](https://github.com/BlueRiverTechnology/brt/pull/11785)
- 🔄 shared: Generate a stationary trajectory when nothing is provided from active pathcontext (brt-chris) [#11682](https://github.com/BlueRiverTechnology/brt/pull/11682)
- 🔄 dune: make dune apps into adk apps (matejgoc-brt) [#11451](https://github.com/BlueRiverTechnology/brt/pull/11451)

### Bumblebee
2 merged | 3 in review | 46.1d avg, 46.1d median

> Bumblebee had minimal activity: cross-cutting CUDA ifdef migration and devops clang toolchain cleanup. Most PRs are shared with other teams.

- devops: remove cuda-11.4/include from clang toolchain -isystem path (rickdynarski-brt) [#11647](https://github.com/BlueRiverTechnology/brt/pull/11647)
- adk: Switch from #ifdef ENABLE_CUDA to #if ENABLE_CUDA (anivegesana) [#8546](https://github.com/BlueRiverTechnology/brt/pull/8546)
- 🔄 shasta: add JP6 TensorRT/inference support and JP5 vs JP6 L4T version detection (tamdo-brt) [#11823](https://github.com/BlueRiverTechnology/brt/pull/11823)
- 🔄 shasta: Fix trailing newlines in C/C++ files (philsc) [#11779](https://github.com/BlueRiverTechnology/brt/pull/11779)
- 🔄 shasta: update to rules_go and bazel_gazelle (brt-alexei) [#11609](https://github.com/BlueRiverTechnology/brt/pull/11609)

### Mesa
3 merged | 1 in review | 4.9d avg, 3.9d median

> Mesa landed Arrow chunking support with schema/data fields for rti_dds_to_arrow_reader and factored the compute module out of Arrow. Python MCAP tools reimplementation is in review.

- devops: Migrate nlohmann_json, opentelemetry-cpp to bzlmod (perfinion) [#11753](https://github.com/BlueRiverTechnology/brt/pull/11753)
- third_party: Factor the compute module out of arrow  (anivegesana) [#11600](https://github.com/BlueRiverTechnology/brt/pull/11600)
- mesa: Add schema and data fields to rti_dds_to_arrow_reader; add chunking (anivegesana) [#11379](https://github.com/BlueRiverTechnology/brt/pull/11379)
- 🔄 mesa: Reimplement MCAP tools in Python (zonera-javed) [#11517](https://github.com/BlueRiverTechnology/brt/pull/11517)

### Athena
1 merged | 0 in review | 4.8d avg, 4.8d median

> Athena merged its initial configuration PR, establishing the program's foundational setup in the monorepo.

- athena: Initial configuration  (divyakul1) [#11603](https://github.com/BlueRiverTechnology/brt/pull/11603)

---

*Generated 2026-04-30T21:00:53Z · Data from GitHub Search API*