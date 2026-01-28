# FRED Macro Research Engine

A modular, notebook-driven macroeconomic research framework built on  
**Federal Reserve Economic Data (FRED)**.

This project provides a structured way to:
- transform raw macro time series,
- reason about macro regimes instead of point estimates,
- study behavior around regime transitions and contractions, and
- export clean, dashboard-ready outputs.

The emphasis is on interpretability, structure, and reuse — not forecasting or trading signals.

---

##  What This Project Is (and Is Not)

### This project **is**:
- A **macro research engine**, not a strategy
- A framework for **exploration, diagnostics, and regime analysis**
- Built for analysts, researchers, and systematic thinkers
- Designed to be extended into dashboards or decision-support tools

### This project is **not**:
- A black-box forecasting model
- A buy/sell signal generator
- A production trading system

---

## Project Structure (High-Level)

```text
fred-macro-regimes-lab/
├── notebooks/
│   ├── Notebook 01 - FRED Quickstart.ipynb
│   ├── Notebook 02 - Transformations That Matter.ipynb
│   ├── Notebook 03 - Macro Relationships.ipynb
│   ├── Notebook 04 - Regimes & Signals.ipynb
│   ├── Notebook 05 - Research Templates.ipynb
│   ├── Notebook 06v1 - Macro Research Dashboard.ipynb
│   ├── Notebook 06v2 - Fully Built Macro Research Pipeline.ipynb
│   └── Notebook 07 - Regime Transitions & Practical Monitoring.ipynb
│
├── macro_utils/
│   ├── __init__.py
│   ├── transforms.py
│   ├── regimes.py
│   ├── events.py
│   ├── plotting.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── outputs/
│
├── figures/
├── dashboards/
├── .gitignore
└── README.md
```
---

## Notebook Roadmap

| Notebook | Purpose |
|--------|--------|
| 01 | FRED ingestion & raw data setup |
| 02 | Core transformations (YoY, MoM, normalization) |
| 03 | Macro relationships & exploratory diagnostics |
| 04 | Regime construction (growth, inflation, policy) |
| 05 | Event studies & reusable research templates |
| **06v2** | **End-to-end macro research dashboard** |
| **07** | **Regime transitions & monitoring** |

> Notebooks **06v2** and **07** represent the culmination of the framework.

---

## Core Outputs

The framework produces:
- Regime-labeled macro time series
- Event-study windows around contractions
- Distributional summaries by macro regime
- Snapshot CSVs for dashboards or monitoring systems

Example exports:
- `macro_dashboard_table.csv`
- `current_macro_snapshot.csv`
- `macro_transition_monitor.csv`

---

## Design Philosophy

- Macro analysis is about context, not precision
- Regimes are often more informative than point estimates
- Research tools should be modular, inspectable, and extensible

---

## Walkthrough & Demo

A video walkthrough accompanies this project, focusing on:
- Notebook **06v2** (macro research dashboard)
- Notebook **07** (regime transitions & monitoring)

Links:
- Video walkthrough: https://youtu.be/mJ_8cxvRnoU

---
