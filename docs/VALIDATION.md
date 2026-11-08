# Validation

| Check | Result |
|---|---|
| Complete confirmation matrix | 24,576 rows; all registered root/method/head/planner keys present exactly once |
| OMR primary scores | TwoRoom 97.40, PushT 91.02, Cube 86.46, Reacher 85.55, mean 90.10 |
| Fixed intervals | All four task intervals and macro interval retained without recomputation |
| Resource rows | 40 method-environment rows retained |
| Release check | SHA manifest, result schema, point estimates, and bundled resource hashes |
| Solver parity | CPU synthetic equivalence against `reference/frozen` |
| New bootstrap | None; frozen statistics are read-only |

Run `python scripts/verify_release.py` after installation. It uses the standard library only.
