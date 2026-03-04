# Trader Joe's NYC Site Selection Case Study

This project evaluates where Trader Joe’s should open its next store in New York City using a layered, business-oriented site selection framework.

## Recommendation

**Recommended ZIP code: 10128 (Upper East Side)**

The final recommendation is based on a two-stage process:
1. A citywide screening model built from public-data proxies for demand, customer fit, whitespace from existing Trader Joe’s stores, and transit access.
2. A finalist-stage refinement overlay incorporating direct-grocery competition and a directional retail rent proxy.

## Project Goal

The goal of this case study is to identify the strongest next expansion market for Trader Joe’s in NYC while balancing:
- market demand
- likely customer fit
- spacing from existing stores
- accessibility
- competitive intensity
- occupancy cost

## Methodology Overview

### Core Screening Model
The citywide model scores ZIP codes using:
- population density
- median household income / income percentile
- distance to nearest Trader Joe’s
- subway station count

### Refinement Overlay
For the top finalists, the model adds:
- competitor count within 1 mile
- nearest competitor distance
- directional retail rent proxy

The final recommendation is not based on a single raw rank alone; it reflects a business judgment informed by both the core model and the refinement overlay.

## Key Outputs

- Executive summary recommendation chart
- Top candidate maps
- Raw-attribute comparison tables
- Weighting and feature-engineering diagnostics

## Repository Structure

- `notebooks/` — end-to-end workflow notebooks
- `src/` — helper functions and path configuration
- `data/` — raw, interim, and processed data
- `outputs/` — exported figures, maps, and tables

## Notebooks

1. `01_data_sources.ipynb` — load and organize source data
2. `02_clean_join.ipynb` — clean, standardize, and join source tables
3. `03_feature_engineering.ipynb` — create model features
4. `04_scoring_model.ipynb` — build core and refinement scoring
5. `05_visualization_and_export.ipynb` — generate final report exhibits

## Notes

- Public-data-only analysis
- Rent inputs are directional retail corridor proxies, not literal ZIP-wide rents
- This project is a ZIP-level screening exercise, not a parcel-level underwriting model