# Code map

| Module | Role |
|---|---|
| `src/omr/metric.py` | Shared 192D endpoint metric and frozen world-model goal-cost interface. |
| `src/omr/guide_objective.py` | Outcome-matched observation/forecast loss and registered reference objectives. |
| `src/omr/coarse.py` | Current-RGB prefilter, endpoint ranking, independent CEM, and four trajectory modes. |
| `src/omr/refinement.py` | Coarse residual interpolation, separately seeded fine search, retained candidate selection. |
| `src/omr/baselines.py` | Matched CEM/retrieval controls and batch expansion. |
| `src/omr/ablations.py` | Direct fine search and coarse-retention controls used by the confirmation matrix. |
| `src/omr/planner.py` | Public `OMR` constructor and registered method aliases. |
| `scripts/evaluate.py` | Portable confirmation runner with exact roots, seeds, and result schema. |
| `scripts/train_guide.py` | Optional CPU refitting from included features; zero API/model requests. |

The metric is initialized as a 192x192 identity matrix. For OMR (`self_search`), the teacher is the observed endpoint geometric relation; the student matches that relation on both observed endpoints and forecasts at horizons 5/15/25. The identity regularizer is 0.001. The world model and encoder remain frozen.

The trajectory backend is preserved unchanged so experiments isolate retrieval supervision. It retrieves four action priors, searches low-dimensional residuals, performs command-level refinement, and scores nine final means with the original goal cost. No learned final selector or extra success label is introduced.
