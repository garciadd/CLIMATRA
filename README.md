# CLIMATRA — CLIMAte TRAnsferability

**Status: early development.** CLIMATRA is an independent Python package for reproducible experiments on the environmental, spatial and temporal transferability of machine-learning models.

The initial scientific benchmark uses global annual Leaf Area Index (LAI, 1982–2022, 0.5°) and environmental predictors. Its main question is how predictive reliability degrades under increasing environmental novelty, including transfers between geographical regions, time periods, and both together. The objective is to compare statistical baselines and machine-learning architectures under controlled information budgets.

## Research scope

- Predict LAI from environmental covariates: `LAI = f(X)`. Spatial and temporal windows, where used, contain environmental **covariates**, not observed neighboring/past/future LAI.
- Planned analyses: climatic regimes, environmental dissimilarity, land-cover and macroclimate stratification, spatial/temporal/spatiotemporal transfer, error, explainability, and computing cost.
- Models under consideration (not yet implemented): statistical references, RF, MLP, CNN, LSTM and ConvLSTM. Choice and experimental design will be finalized after data auditing and feasibility pilots.

## Data

**Input datasets are external, frozen outputs** of an existing data generator. CLIMATRA does not download or regenerate these datasets. Future dataset manifests will record versions, checksums, variables, units, geographic/temporal coverage and provenance. Neither raw nor processed research data are included in this repository.

## Install and verify the initial skeleton

Python 3.10 or newer is required.

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
```

At present, CLIMATRA provides an installable package and a smoke test only. No modeling functionality has been implemented.