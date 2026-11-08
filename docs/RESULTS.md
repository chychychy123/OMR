# Result notes

Primary OMR rows are `refined_self` in `results/all_methods.csv`. The four-task mean is computed after averaging all heads and planners within each root, then equally weighting tasks. Fixed macro intervals are in `results/all_methods_macro.csv`.

The confirmation includes all registered negative and positive controls; no row was removed based on score. `paired_contrasts.csv` contains the frozen same-root OMR-minus-control intervals. `paired_outcome_decomposition.csv` reports both-succeed, OMR-only, control-only, and both-fail categories.

External RGB-system scores in `published_baselines.json` are descriptive cross-report values, not paired reruns. Their checkpoints, roots, and budgets differ; only OMR intervals are available from this study.

Recorded controller time and transition counts are retained in `controller_resources.csv`. Timing is descriptive shared-hardware evidence, not a new benchmark endpoint.
