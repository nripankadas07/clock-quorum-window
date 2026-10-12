# Qualitative research — 12 October 2026

Observed 2026-10-12 06:35:23 UTC. Search queries: `ntp time synchronization sort:stars-desc`.

GitHub search requested star ordering through query qualifiers. Direct repository-search REST fetch was unsupported; connector results were noisy and some irrelevant matches were rejected. Established adjacent tools were added explicitly, with current repository metadata, README and three recent open issue/PR records inspected. Ranking is the highest-star relevant comparable among these found sources, not an exhaustive global ranking. Code inspected for one relevant comparable in each area; complete competitor installations and full feature inventories were not tested.

| Repository | Stars | Last pushed UTC | API license |
| --- | ---: | --- | --- |
| [Time-Appliances-Project/Time-Card](https://github.com/Time-Appliances-Project/Time-Card) | 1486 | 2026-09-08T05:29:39Z | NOASSERTION |
| [ntpsec/ntpsec](https://github.com/ntpsec/ntpsec) | 287 | 2026-10-10T02:22:29Z | NOASSERTION |
| [cloudflare/roughtime](https://github.com/cloudflare/roughtime) | 178 | 2026-04-28T20:48:37Z | Apache-2.0 |

Highest-star relevant/adjacent source found in this inspected set: Time-Appliances-Project/Time-Card.

Time-Card is hardware/time-server infrastructure, NTPsec implements NTP, and Roughtime provides cryptographic time-protocol utilities. They are adjacent alternatives, not direct interval-diagnostic equivalents. This candidate solves closed interval k-coverage over supplied integer offsets, preserving disjoint components and point-only agreement. It does not measure time, authenticate observations or implement NTP/PTP/Roughtime. The Roughtime README warns against production use and describes unstable draft/API compatibility.

Installability, examples and support were assessed from current README/issue evidence. No measured time-to-result, reliability ranking, comparative speed or superiority claim is made. Our offline installed example passes; that establishes our behavior only. Specific demand remains inferred, as stated in README. All implementation code is original; no third-party source or prose was imported.

## Current evidence links

- Time-Appliances-Project/Time-Card: [README](https://github.com/Time-Appliances-Project/Time-Card/blob/master/README.md), observed blob `165e74506a7cf14081fff53b2394a43c8194e6ff`.
  - [issue](https://github.com/Time-Appliances-Project/Time-Card/issues/120) — Linux installation related
  - [issue](https://github.com/Time-Appliances-Project/Time-Card/issues/118) — Multiple TimeCards synchronization via 1PPS or 10MHz connection
  - [issue](https://github.com/Time-Appliances-Project/Time-Card/issues/116) — Password for ECAD archives
- ntpsec/ntpsec: [README](https://github.com/ntpsec/ntpsec/blob/master/README.adoc), observed blob `aa750b2005183708435c94578dcab961a85554d5`.
  - [PR](https://github.com/ntpsec/ntpsec/pull/10) — Refactor ntpd to support non-root execution
  - [PR](https://github.com/ntpsec/ntpsec/pull/8) — Fix ntpdig.py
  - [PR](https://github.com/ntpsec/ntpsec/pull/7) — Support  ecdhcurves list TLS Option
- cloudflare/roughtime: [README](https://github.com/cloudflare/roughtime/blob/master/README.md), observed blob `65703ed42420412a0f975f244906580c1602e901`.
  - [PR](https://github.com/cloudflare/roughtime/pull/73) — Add roughtime.alastyr.com to the ecosystem
  - [issue](https://github.com/cloudflare/roughtime/issues/72) — `cmd/getroughtime -config ecosystem.json` failing to get responses from cloudflare
  - [issue](https://github.com/cloudflare/roughtime/issues/60) — Have `CreateRequest()` return a `*Request`
