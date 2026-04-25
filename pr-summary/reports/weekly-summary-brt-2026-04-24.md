# Weekly Engineering Summary — Week of April 17

**Period**: 2026-04-17 to 2026-04-24 | **251 merged, 132 open** across **8 teams**

## Highlights

- Massive Bazel bzlmod migration landed — gRPC, protobuf, gtest, and dozens of third-party deps moved to bzlmod with legacy WORKSPACE cleanup.
- Mercury shipped resim v0 with visual odometry metrics, stats dashboards, and a new universal wheel odometer.
- ADK tooling surge: calibration UI, Epiviz MCAP warnings, EEPROM handling, and Direct-to-Host AWS broker connectivity all shipped.

## Team Reports

### Shasta
123 merged | 60 in review

- 12 Phelps MY27 SOP machine configs added (rajshah-brt) [#11308](https://github.com/BlueRiverTechnology/brt/pull/11308)–[#11325](https://github.com/BlueRiverTechnology/brt/pull/11325)
- Variable Rate mode: disabled weed pressure, fixed op-check fallback, unified VR activation (maxwellgumley-brt) [#11519](https://github.com/BlueRiverTechnology/brt/pull/11519) [#11364](https://github.com/BlueRiverTechnology/brt/pull/11364) [#11346](https://github.com/BlueRiverTechnology/brt/pull/11346)
- BSP 3.2.1 released for VPU1 & VPU2 with rev7 support and flash ratchet protection (brt-brennan-coslett, brt-sarah-newman) [#11528](https://github.com/BlueRiverTechnology/brt/pull/11528) [#11415](https://github.com/BlueRiverTechnology/brt/pull/11415) [#11466](https://github.com/BlueRiverTechnology/brt/pull/11466)
- Fixed realtime malloc in capabilities watcher and concurrent log access crashes (maxwellgumley-brt, brt-alexei) [#11483](https://github.com/BlueRiverTechnology/brt/pull/11483) [#11388](https://github.com/BlueRiverTechnology/brt/pull/11388)
- Shark test automation: 6 new automated tests including install, CAN mux, and camera firmware (jocelyn-vil, W7NIIIF-deere, omarmanzano-brt)
- Nozzle mapping and command fixes for non-S&S geometries (brt-Naman-Gupta) [#11473](https://github.com/BlueRiverTechnology/brt/pull/11473) [#11267](https://github.com/BlueRiverTechnology/brt/pull/11267) [#11348](https://github.com/BlueRiverTechnology/brt/pull/11348)
- MTG client refactored into separate files for handlers, services, and API (brt-alexei) [#10693](https://github.com/BlueRiverTechnology/brt/pull/10693) [#10703](https://github.com/BlueRiverTechnology/brt/pull/10703) [#10726](https://github.com/BlueRiverTechnology/brt/pull/10726) [#10734](https://github.com/BlueRiverTechnology/brt/pull/10734)
- ~15 maintenance PRs (CI configs, test rewrites, Buildkite params, Go SDK updates)
- 🔄 Python 3.11 default, AOS Python bindings, rules_go/gazelle update, Raven upload improvements

### Jupiter
47 merged | 24 in review

- Gretzky stereo depth: optimized disparity regression, curated pseudo-GT loss refactor, temperature scaling compat fix (danny-schwartz-brt, bin-cheng-brt) [#11474](https://github.com/BlueRiverTechnology/brt/pull/11474) [#11502](https://github.com/BlueRiverTechnology/brt/pull/11502) [#11551](https://github.com/BlueRiverTechnology/brt/pull/11551)
- EM V2 final large pass and dust loss improvements for depth model training (Alex17Li) [#11205](https://github.com/BlueRiverTechnology/brt/pull/11205) [#10281](https://github.com/BlueRiverTechnology/brt/pull/10281)
- Replay-aware latency metrics across detection, tracking, zone comparator, and object localizer (ziyang-brt) [#11355](https://github.com/BlueRiverTechnology/brt/pull/11355)–[#11360](https://github.com/BlueRiverTechnology/brt/pull/11360)
- MCAP compression enabled in SDC and event file naming fixes (brt-junwuzhang) [#11573](https://github.com/BlueRiverTechnology/brt/pull/11573) [#11447](https://github.com/BlueRiverTechnology/brt/pull/11447)
- Blind Spot Monitor test logic fixed with subset option (scottmiller-brt) [#11492](https://github.com/BlueRiverTechnology/brt/pull/11492)
- Feature flags validation library and design landed (brt-ivanpauno) [#9509](https://github.com/BlueRiverTechnology/brt/pull/9509)
- Initial radar point cloud processor (rondomingobrt) [#9268](https://github.com/BlueRiverTechnology/brt/pull/9268)
- ~8 maintenance PRs (test infra, monitor cleanup, subsystem replay fixes)
- 🔄 Feature flags app, stereo loss refactoring, single camera replacement testing

### ADK
32 merged | 16 in review

- Calibration UI rebuilt with separate app views and 3D OpenGL coverage (daneshgandhi) [#11606](https://github.com/BlueRiverTechnology/brt/pull/11606)
- Epiviz App: MCAP frame index warnings and Jupiter implement config (daneshgandhi, athulkbrt) [#11607](https://github.com/BlueRiverTechnology/brt/pull/11607) [#11525](https://github.com/BlueRiverTechnology/brt/pull/11525)
- Direct-to-Host: AWS broker connectivity with prod certs and root CA (rakeshdugad-brt) [#11577](https://github.com/BlueRiverTechnology/brt/pull/11577) [#11333](https://github.com/BlueRiverTechnology/brt/pull/11333) [#11292](https://github.com/BlueRiverTechnology/brt/pull/11292)
- EEPROM tool improvements and I2C write bug fix (chuckstanski-brt, athulkbrt) [#11590](https://github.com/BlueRiverTechnology/brt/pull/11590) [#11499](https://github.com/BlueRiverTechnology/brt/pull/11499) [#11602](https://github.com/BlueRiverTechnology/brt/pull/11602)
- IMU calibration with StarFire GPS poses (bartoszkalinczuk) [#11143](https://github.com/BlueRiverTechnology/brt/pull/11143)
- mcap_merge: strict-schema option and replay publish-clock looping (wingiptam-brt) [#11022](https://github.com/BlueRiverTechnology/brt/pull/11022) [#11240](https://github.com/BlueRiverTechnology/brt/pull/11240)
- UDS support moved from Jupiter to ADK layer (pabloanigstein-brt) [#10974](https://github.com/BlueRiverTechnology/brt/pull/10974)
- 🔄 Large file streaming for autocal, COLMAP parallelization, Direct-to-Host VPU communication

### Dune
24 merged | 14 in review

- Subsystem replay with autocalibration and EMU replay with S3 metrics (LuisIvSandoval, RubenMovsesyan) [#11541](https://github.com/BlueRiverTechnology/brt/pull/11541) [#11504](https://github.com/BlueRiverTechnology/brt/pull/11504)
- Sim rework: better exit handling, camera support, and launch screen (matejgoc-brt, mattelsey-brt) [#11272](https://github.com/BlueRiverTechnology/brt/pull/11272) [#11352](https://github.com/BlueRiverTechnology/brt/pull/11352) [#11249](https://github.com/BlueRiverTechnology/brt/pull/11249)
- Hardware metrics collection and VADC CAN message validation (RubenMovsesyan, brt-holgerbanski) [#11444](https://github.com/BlueRiverTechnology/brt/pull/11444) [#11002](https://github.com/BlueRiverTechnology/brt/pull/11002)
- SC02 bundle updated for tech field days (gracematera-brt) [#11262](https://github.com/BlueRiverTechnology/brt/pull/11262)
- ~8 maintenance PRs (delta cleanup, experience updates, IQ fixes)
- 🔄 Zone splitting drift fix, deceleration message source change, velocity buffer extension

### Mercury
9 merged | 4 in review

- Resim v0 shipped with visual odometry metrics and stats dashboards (ramiro-serra-brt, brt-chris) [#11237](https://github.com/BlueRiverTechnology/brt/pull/11237) [#11380](https://github.com/BlueRiverTechnology/brt/pull/11380) [#11450](https://github.com/BlueRiverTechnology/brt/pull/11450)
- New shared universal wheel odometer (brt-chris) [#11256](https://github.com/BlueRiverTechnology/brt/pull/11256)
- Simplified OpenImu publishing logic by removing event triggers (ramiro-serra-brt) [#11434](https://github.com/BlueRiverTechnology/brt/pull/11434)
- 🔄 VADC protocol implementation, localization fixes

### Bumblebee
5 merged | 1 in review

- Harvest automation and multi-model inference support shipped (SanjayKV-deere) [#8649](https://github.com/BlueRiverTechnology/brt/pull/8649) [#8803](https://github.com/BlueRiverTechnology/brt/pull/8803)
- Observation state parsing with offset time (SanjayKV-deere) [#9542](https://github.com/BlueRiverTechnology/brt/pull/9542)
- Dataset creation script now supports merging with previous datasets (rakhil575) [#10702](https://github.com/BlueRiverTechnology/brt/pull/10702)

### Unlabeled / Cross-team
22 merged | 16 in review

- Bazel bzlmod migration: gRPC, protobuf, gtest, libjpeg, and more moved to bzlmod; legacy WORKSPACE cleaned up (perfinion) [#11187](https://github.com/BlueRiverTechnology/brt/pull/11187) [#11400](https://github.com/BlueRiverTechnology/brt/pull/11400) [#11459](https://github.com/BlueRiverTechnology/brt/pull/11459)–[#11462](https://github.com/BlueRiverTechnology/brt/pull/11462)
- Open3D 0.19.0 and kiss-icp added as third-party deps (amaharshi) [#11159](https://github.com/BlueRiverTechnology/brt/pull/11159) [#10638](https://github.com/BlueRiverTechnology/brt/pull/10638)
- Devin AI tool config: GitHub MCP access, allowed tools, CLI config (philsc, danielgotsch-brt) [#11501](https://github.com/BlueRiverTechnology/brt/pull/11501) [#11370](https://github.com/BlueRiverTechnology/brt/pull/11370)
- ~8 maintenance PRs (profiling paths, merge queue fixes, DNS, domain redirects)
