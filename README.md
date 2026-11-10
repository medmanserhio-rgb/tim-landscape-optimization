# Intelligent Multi-Criteria Optimization of Landscape-Ecological Parameters in TIM Modeling

This repository contains the source code and algorithm support for the intelligent optimization of landscape and urban greening parameters within Technology of Information Modeling (TIM) using Autodesk Revit and Python.

## Core Features
*   **Surrogate AI Modeling:** Fast microclimate and wind aerodynamics approximation using Random Forest Regressor instead of heavy CFD simulations.
*   **Evolutionary Optimization:** Spatial tree placement optimization based on Genetic Algorithm (GA) via DEAP library.
*   **BIM Integration:** Automated read/write pipeline for geometry and landscape elements parameters using Autodesk Revit and Dynamo API.

## Repository Structure
*   `train_model.py` — Python script for training the Random Forest surrogate model and evaluating metrics (R2, MAE).
*   `vkr_landscape_data.csv` — Experimental dataset based on MBOU SOH № 177 (Novosibirsk). Contains 102 tree configurations.
*   `LICENSE` — Open-source MIT License.

## Dataset Description (`vkr_landscape_data.csv`)
The dataset contains spatial and dendrological parameters used to train the surrogate model:
*   `tree_id` — Unique identifier for each tree.
*   `species` — Tree species (*Populus sibirica*, *Betula pendula*, *Tilia cordata*, *Malus baccata*).
*   `coord_X`, `coord_Y` — Spatial coordinates of the planting point on the site plan.
*   `height` — Tree height (meters).
*   `crown_diam` — Crown diameter (meters).
*   `wind_coef` — Wind retention coefficient (relative aerodynamic efficiency).
*   `E_wind` — Wind protection efficiency score (target variable for regression).

## Requirements & Environment
*   Python 3.11+
*   Autodesk Revit 2024 / 2025 + Dynamo API
*   Required Packages: `scikit-learn`, `deap`, `pandas`, `numpy`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
