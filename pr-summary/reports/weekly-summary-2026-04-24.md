# Weekly Engineering Summary — Week of 2026-04-17

**Period**: 2026-04-17 to 2026-04-24 | **254 merged, 135 open** across **8 teams** | avg days to merge: **10.1**

## Highlights

- Shasta shipped BSP 3.2.1 across both VPU platforms and merged 124 PRs — the most active team this week.
- Jupiter optimized the Gretzky depth model pipeline with windowed disparity regression and curated stereo pseudo-GT improvements.
- Infrastructure migrated core third-party dependencies (gRPC, protobuf, gtest, jsoncpp) to bzlmod, modernizing the build system.

## Team Reports

### Shasta
124 merged | 63 in review | avg merge: 13.6d | median: 5.3d

- Shipped BSP 3.2.1 for VPU1 & VPU2 (brt-brennan-coslett) [#11528](https://github.com/BlueRiverTechnology/brt/pull/11528) [#11414](https://github.com/BlueRiverTechnology/brt/pull/11414) [#11367](https://github.com/BlueRiverTechnology/brt/pull/11367) [#11362](https://github.com/BlueRiverTechnology/brt/pull/11362)
- Hardened Shark diagnostic and firmware tests (jocelyn-vil) [#11571](https://github.com/BlueRiverTechnology/brt/pull/11571) [#11537](https://github.com/BlueRiverTechnology/brt/pull/11537) [#11535](https://github.com/BlueRiverTechnology/brt/pull/11535) [#11530](https://github.com/BlueRiverTechnology/brt/pull/11530) [#11463](https://github.com/BlueRiverTechnology/brt/pull/11463)
- Refined weed pressure and boomtrac mode logic (maxwellgumley-brt) [#11519](https://github.com/BlueRiverTechnology/brt/pull/11519) [#11512](https://github.com/BlueRiverTechnology/brt/pull/11512) [#11511](https://github.com/BlueRiverTechnology/brt/pull/11511)
- Improved raven upload status checking (brt-alexei) [#11538](https://github.com/BlueRiverTechnology/brt/pull/11538)
- 5 CI/Buildkite infrastructure improvements
- Diagnostic aggregator and VPU config fixes (pallavi-brt) [#11593](https://github.com/BlueRiverTechnology/brt/pull/11593)
- Robotech B-series memory and stability improvements (sanjaynarayanan-brt) [#11405](https://github.com/BlueRiverTechnology/brt/pull/11405) [#11367](https://github.com/BlueRiverTechnology/brt/pull/11367)
- 88 additional maintenance/fix PRs
- 🔄 robotech: b-series: Shrink MqttEmulator memory usage (sanjaynarayanan-brt) [#11638](https://github.com/BlueRiverTechnology/brt/pull/11638)
- 🔄 Fix boomtrac_mode_module oscillations (brian-griglak) [#11636](https://github.com/BlueRiverTechnology/brt/pull/11636)
- 🔄 Update spyglass to publish SprayControl message (brian-griglak) [#11635](https://github.com/BlueRiverTechnology/brt/pull/11635)
- 🔄 60 more PRs in review

### Jupiter
48 merged | 23 in review | avg merge: 12.7d | median: 2.8d

- Advanced depth model pipeline with optimized disparity regression and stereo pseudo-GT (scottmiller-brt) [#11624](https://github.com/BlueRiverTechnology/brt/pull/11624) [#11551](https://github.com/BlueRiverTechnology/brt/pull/11551) [#11508](https://github.com/BlueRiverTechnology/brt/pull/11508) [#11502](https://github.com/BlueRiverTechnology/brt/pull/11502) [#11484](https://github.com/BlueRiverTechnology/brt/pull/11484)
- Enhanced SDC recording with MCAP compression and JQ triggering (brt-junwuzhang) [#11573](https://github.com/BlueRiverTechnology/brt/pull/11573) [#11558](https://github.com/BlueRiverTechnology/brt/pull/11558) [#11477](https://github.com/BlueRiverTechnology/brt/pull/11477)
- Improved subsystem replay with user-defined output folders (scottmiller-brt) [#11624](https://github.com/BlueRiverTechnology/brt/pull/11624) [#11575](https://github.com/BlueRiverTechnology/brt/pull/11575) [#11446](https://github.com/BlueRiverTechnology/brt/pull/11446)
- Fixed blind spot monitor logic and lidar extrinsic calibration (brt-jing) [#11545](https://github.com/BlueRiverTechnology/brt/pull/11545) [#11492](https://github.com/BlueRiverTechnology/brt/pull/11492) [#11448](https://github.com/BlueRiverTechnology/brt/pull/11448)
- Galileo test rerun now supports exclude filters (daipayandeb-brt) [#11592](https://github.com/BlueRiverTechnology/brt/pull/11592) [#11439](https://github.com/BlueRiverTechnology/brt/pull/11439) [#11254](https://github.com/BlueRiverTechnology/brt/pull/11254) [#11202](https://github.com/BlueRiverTechnology/brt/pull/11202)
- 16 additional maintenance/fix PRs
- 🔄 gretzky: Separate SkySupervisedLoss from StereoLeftRightConsistencyLos (danny-schwartz-brt) [#11627](https://github.com/BlueRiverTechnology/brt/pull/11627)
- 🔄 Automated single camera replacement testing (brt-ivanpauno) [#11618](https://github.com/BlueRiverTechnology/brt/pull/11618)
- 🔄 jupiter: Remove implement_type publisher and dependencies. (BRTMiguel) [#11611](https://github.com/BlueRiverTechnology/brt/pull/11611)
- 🔄 20 more PRs in review

### ADK
32 merged | 16 in review | avg merge: 6.0d | median: 1.1d

- Epiviz gained frame index warnings and Jupiter VPU delta config (daneshgandhi) [#11607](https://github.com/BlueRiverTechnology/brt/pull/11607) [#11605](https://github.com/BlueRiverTechnology/brt/pull/11605) [#11525](https://github.com/BlueRiverTechnology/brt/pull/11525)
- Camera calibration UI shipped 3D coverage views and memory optimizations (daneshgandhi) [#11606](https://github.com/BlueRiverTechnology/brt/pull/11606) [#11465](https://github.com/BlueRiverTechnology/brt/pull/11465) [#11464](https://github.com/BlueRiverTechnology/brt/pull/11464)
- Fixed EEPROM write bugs and improved dogbone handling (athulkbrt) [#11602](https://github.com/BlueRiverTechnology/brt/pull/11602) [#11499](https://github.com/BlueRiverTechnology/brt/pull/11499)
- Fixed I2C write path (chuckstanski-brt) [#11590](https://github.com/BlueRiverTechnology/brt/pull/11590)
- 22 additional maintenance/fix PRs
- 🔄 [ADK-4247] Start heartbeats if enabled (rickdynarski-brt) [#11621](https://github.com/BlueRiverTechnology/brt/pull/11621)
- 🔄 adk: EEPROM Tool - Improve dogbone EEPROM handling (daneshgandhi) [#11616](https://github.com/BlueRiverTechnology/brt/pull/11616)
- 🔄 [ADK-4248] Add large file support to the autocal python script (stream (danielgotsch-brt) [#11604](https://github.com/BlueRiverTechnology/brt/pull/11604)
- 🔄 13 more PRs in review

### Dune
24 merged | 14 in review | avg merge: 2.6d | median: 1.1d

- Advanced replay infrastructure with autocalibration and metrics (LuisIvSandoval) [#11619](https://github.com/BlueRiverTechnology/brt/pull/11619) [#11541](https://github.com/BlueRiverTechnology/brt/pull/11541) [#11504](https://github.com/BlueRiverTechnology/brt/pull/11504) [#11441](https://github.com/BlueRiverTechnology/brt/pull/11441)
- Updated test experiences and cleaned up delta configs (LuisIvSandoval) [#11570](https://github.com/BlueRiverTechnology/brt/pull/11570) [#11543](https://github.com/BlueRiverTechnology/brt/pull/11543)
- Added hardware metrics reporting (RubenMovsesyan) [#11444](https://github.com/BlueRiverTechnology/brt/pull/11444) [#11262](https://github.com/BlueRiverTechnology/brt/pull/11262)
- 14 additional maintenance/fix PRs
- 🔄 dune: fix zone splitting drift (matejgoc-brt) [#11632](https://github.com/BlueRiverTechnology/brt/pull/11632)
- 🔄 [SW-3877] Configuration bridge can update Gen5/DAV Display (nahueespinosa) [#11630](https://github.com/BlueRiverTechnology/brt/pull/11630)
- 🔄 dune: Fix geojson 3D offset (gracematera-brt) [#11608](https://github.com/BlueRiverTechnology/brt/pull/11608)
- 🔄 11 more PRs in review

### Unlabeled
23 merged | 17 in review | avg merge: 4.9d | median: 1.0d

- Migrated core third-party deps to bzlmod (perfinion) [#11522](https://github.com/BlueRiverTechnology/brt/pull/11522) [#11462](https://github.com/BlueRiverTechnology/brt/pull/11462) [#11461](https://github.com/BlueRiverTechnology/brt/pull/11461)
- DevOps tooling updates (ramiro-serra-brt) [#11529](https://github.com/BlueRiverTechnology/brt/pull/11529) [#11442](https://github.com/BlueRiverTechnology/brt/pull/11442) [#11404](https://github.com/BlueRiverTechnology/brt/pull/11404)
- 11 additional unlabeled PRs
- 🔄 devops: Graphite bot double-check prior to PR nudge (ryancalhoun-brt) [#11637](https://github.com/BlueRiverTechnology/brt/pull/11637)
- 🔄 Enable highres_mapper and tile uploads in rainier wacker config (kiran-mohan-brt) [#11626](https://github.com/BlueRiverTechnology/brt/pull/11626)
- 🔄 [ROBOT-4061] Create warm cache upload workflow (andrewring) [#11622](https://github.com/BlueRiverTechnology/brt/pull/11622)
- 🔄 14 more PRs in review

### Mercury
9 merged | 4 in review | avg merge: 12.3d | median: 2.3d

- devops: Add pre-commit script that replaces `#ifdef ENABLE_CUDA` with  (anivegesana) [#11531](https://github.com/BlueRiverTechnology/brt/pull/11531)
- mercury: add more stats to resim, and fix plots  (brt-chris) [#11450](https://github.com/BlueRiverTechnology/brt/pull/11450)
- mercury: Gamma data collection work (ramiro-serra-brt) [#11443](https://github.com/BlueRiverTechnology/brt/pull/11443)
- mercury: Remove event trigger from OpenImu and simplify publishing log (ramiro-serra-brt) [#11434](https://github.com/BlueRiverTechnology/brt/pull/11434)
- mercury: Map test assertion failures to success exit code in ReSim en… (ramiro-serra-brt) [#11427](https://github.com/BlueRiverTechnology/brt/pull/11427)
- mercury: port vo metrics to resim (brt-chris) [#11380](https://github.com/BlueRiverTechnology/brt/pull/11380)
- 3 additional PRs
- 🔄 mercury: Implementation of VADC protocol (DanielMovsesyanBRT) [#11617](https://github.com/BlueRiverTechnology/brt/pull/11617)
- 🔄 merlin: localization fixes (ramiro-serra-brt) [#11612](https://github.com/BlueRiverTechnology/brt/pull/11612)
- 🔄 merlin: [WIP] localization work (ramiro-serra-brt) [#11527](https://github.com/BlueRiverTechnology/brt/pull/11527)
- 🔄 1 more PRs in review

### Bumblebee
5 merged | 1 in review | avg merge: 62.6d | median: 74.5d

- bumblebee: Update dataset creation script to merge with previous datas (rakhil575) [#10702](https://github.com/BlueRiverTechnology/brt/pull/10702)
- bumblebee: Implementation to parse observation states with offset time (SanjayKV-deere) [#9542](https://github.com/BlueRiverTechnology/brt/pull/9542)
- bumblebee: Inference with multiple models (SanjayKV-deere) [#8803](https://github.com/BlueRiverTechnology/brt/pull/8803)
- bumblebee: harvest automation (SanjayKV-deere) [#8649](https://github.com/BlueRiverTechnology/brt/pull/8649)
- adk: Switch from #ifdef ENABLE_CUDA to #if ENABLE_CUDA (anivegesana) [#8546](https://github.com/BlueRiverTechnology/brt/pull/8546)
- 🔄 shasta: update to rules_go and bazel_gazelle (brt-alexei) [#11609](https://github.com/BlueRiverTechnology/brt/pull/11609)

### Mesa
1 merged | 3 in review | avg merge: 15.6d | median: 15.6d

- adk: Add a low level `ChannelMessageView.iter_arrow` function to ADK m (anivegesana) [#10852](https://github.com/BlueRiverTechnology/brt/pull/10852)
- 🔄 third_party: Factor the compute module out of arrow  (anivegesana) [#11600](https://github.com/BlueRiverTechnology/brt/pull/11600)
- 🔄 mesa: Updating _mcap_tools_pybind.py to match C++ MCAP tools' implemen (zonera-javed) [#11517](https://github.com/BlueRiverTechnology/brt/pull/11517)
- 🔄 mesa: Add schema and data fields to rti_dds_to_arrow_reader; add chunk (anivegesana) [#11379](https://github.com/BlueRiverTechnology/brt/pull/11379)

### Athena
0 merged | 1 in review | avg merge: 0d | median: 0d

- 🔄 athena: Initial configuration  (divyakul1) [#11603](https://github.com/BlueRiverTechnology/brt/pull/11603)
