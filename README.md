# clock-quorum-window

Public alpha prepared on 12 October 2026. **Remote verification pending; not yet a verified launch.**
Original Python implementation, MIT, zero runtime dependencies. AI-assisted development.

Reliability engineer comparing captured clock-offset uncertainty estimates. Find every closed offset interval supported by a required count and expose disjoint or point-only agreement.

Exact integer interval sweep for k-coverage with separate point/interior support counts and merged quorum windows.

## Install and first useful result

Python 3.10+ (only Linux Python 3.12.14 tested in this preparation). Build requires setuptools 61+ and wheel already available; install into a fresh venv uses only the generated wheel. Run source tests with your build interpreter:

```sh
python -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse .
python -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps wheelhouse/*.whl
.venv/bin/clock-quorum-window example.json
python -m unittest -v
```

The included synthetic input documents the exact normalized JSON schema.
Output is deterministic JSON; malformed inputs exit 2. Inputs are limited to 1 MiB.
No network connections, credential reads or writes to input files occur.
Hostnames, identifiers, paths and selected SSH values may be disclosed in output.
Review exported inputs and outputs before sharing. Use synthetic examples for reports.

## Scope and limits

Not NTP/PTP implementation, authenticated time, clock correction or proof that independent sources are trustworthy.

Specific demand: Inferred from clock synchronization workflows; adjacent NTP/Roughtime/Time-Card tools are broader alternatives.
Discovery: Clock uncertainty and quorum examples.
Portfolio distinction: DNS quorum compares serial equality; this tool solves geometric uncertainty overlap.
See RESEARCH.md and the bundled research record for alternatives and incomplete research coverage.
No competitor absence, performance superiority or customer-adoption claim.

## Acceptance criteria

- Closed shared endpoints count, including zero-width intervals.
- Return every disjoint component deterministically.
- Unique source IDs, bounded count, valid intervals and quorum are mandatory.

## Support and contribution

Report a reproducible synthetic input, expected result, actual output and Python version.
Keep changes bounded and run the unit suite and clean installed example.
Do not submit private host configuration, production metric labels or credentials.
Security reports should omit secrets; this offline diagnostic is not a security boundary.
The source distribution is the supported install path; no registry release is claimed.
