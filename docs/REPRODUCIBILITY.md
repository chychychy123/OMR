# Reproducibility

## Exact runtime

Install Python 3.11, PyTorch 2.8.0, and the pinned dependency revision. `scripts/check_runtime.py` compares installed planning source hashes with `provenance/tested_environment.json`. Linux/EGL is the recorded configuration.

## External datasets

Place the original HDF5 files under `external_data/`:

- `pusht_expert_train.h5`
- `tworoom.h5`
- `reacher.h5`
- `ogbench/cube_single_expert.h5`

The runner caches only dataset action keys. Evaluation roots are fixed by `results/confirmation/<environment>/split.json`.

## Checkpoints

Use the exact checkpoint SHA recorded in `configs/experiment.json`. A mismatched checkpoint is rejected even if the architecture loads. The confirmation used one frozen world-model training seed per environment; independent model-seed training and real-robot evaluation were not part of this study.

## Confirmation matrix

Each environment uses 24 configurations, 128 roots, and planner seeds 8301/8302. Learned-guide methods additionally average heads 2131/2132/2133. The complete matrix is 6,144 episodes per environment and 24,576 total. The runner refuses to overwrite an existing output directory.

The stored analysis files were computed once with 10,000 root-cluster bootstrap replicates and fixed seeds. `scripts/verify_release.py` verifies SHA records and point estimates; it does not recompute uncertainty.

## Engineering identity

The package includes complete episode rows, audits, exclusions, retrieval IDs, and engineering QA records. It does not include remote scheduler logs, process identities, credentials, or machine-local paths. The frozen code registry in `results/code_registry.json` preserves the original experiment-time source identities.
