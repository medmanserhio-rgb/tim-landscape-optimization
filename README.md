# Intelligent Multi-Criteria Optimization of Landscape-Ecological Parameters in TIM Modeling

This repository contains the source code and algorithm обеспечения for intelligent optimization of landscape and urban greening parameters within Technology of Information Modeling (TIM) using Autodesk Revit and Python.

## 🚀 Core Features
- **Surrogate AI modeling:** Fast microclimate and wind aerodynamics approximation using *Random Forest Regressor* instead of heavy CFD simulations.
- **Evolutionary Optimization:** Spatial tree placement optimization based on *Genetic Algorithm (GA)* via `DEAP` library.
- **BIM Integration:** Automated read/write pipeline for geometry and landscape elements parameters using *Autodesk Revit* and *Dynamo API*.

## 📂 Repository Structure
- `train_model.py` — Python script for training the Random Forest surrogate model.
- `vkr_landscape_data.xlsx` — Experimental dataset based on MBOU SOH № 177 (Novosibirsk).
- `LICENSE` — Open-source MIT License.

## 🛠️ Requirements & Environment
- Python 3.11+
- Autodesk Revit 2024 / 2025 + Dynamo API
- Required Packages: `scikit-learn`, `deap`, `pandas`, `numpy`

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
