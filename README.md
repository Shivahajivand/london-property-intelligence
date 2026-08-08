# London Property Intelligence

## Portfolio Project

### Project Overview

London Property Intelligence is an end-to-end data science project that integrates multiple urban datasets to build a comprehensive London Intelligence Dataset for residential property market analysis.

Starting from HM Land Registry property transactions, the project progressively enriches borough-level data with external urban indicators—including population, crime, and other socioeconomic datasets—to create a unified analytical dataset for feature engineering, investment analysis, and predictive modelling.

Rather than analysing property prices in isolation, the project demonstrates how integrating diverse urban data sources can provide deeper insights into London's housing market and support more informed, data-driven decision-making.

The project follows a modular, notebook-based workflow, where each stage incrementally expands the London Intelligence Dataset while applying professional data science practices such as data validation, feature engineering, exploratory analysis, and reproducible data pipelines.

---

## Business Problem

Understanding residential property opportunities across London requires more than analysing property prices alone.

High property values may indicate premium locations, while high transaction activity may reflect stronger market liquidity and demand. However, investment decisions based on a single indicator may provide an incomplete view of market potential.

This project investigates how combining property market data with broader urban intelligence can provide a more comprehensive understanding of London boroughs. By integrating multiple datasets and engineering meaningful features, the project aims to support data-driven analysis, investment evaluation, and future predictive modelling.

The project evolves from initial market scoring approaches towards building a multi-layer London Intelligence Dataset that captures a wider range of factors influencing London's residential property landscape.

## Dataset

The project is built around a multi-layer London Intelligence Dataset that integrates residential property market data with external urban datasets to create a richer borough-level analytical framework.

The foundation of the dataset is the HM Land Registry Price Paid Data (PPD), an official UK government dataset containing residential property transaction records across England and Wales.

For this project, property transactions were filtered to include Greater London, creating a borough-level property dataset covering London's 33 administrative areas. The property layer is progressively enriched with additional urban intelligence layers to support deeper analysis, feature engineering, and future predictive modelling.

### Data Sources

The project currently integrates the following data sources into its analytical workflow:

* **Property Layer**

  * HM Land Registry – Price Paid Data (PPD)
  * Residential property transactions within Greater London
  * Coverage: 2018–2025

* **Population Layer**

  * Office for National Statistics (ONS) Mid-Year Population Estimates
  * Borough-level population statistics

* **Crime Layer**

  * London Crime Data
  * Borough-level crime statistics integrated into the current London Intelligence Dataset

Additional datasets are being prepared for future integration, including:

* Income indicators
* Public Transport Accessibility Level (PTAL)
* Index of Multiple Deprivation (IMD)

### Current Dataset Structure

The current London Intelligence Dataset is structured at borough-year level and combines:

* Property market indicators
* Population statistics
* Crime-related indicators

The dataset is designed as a modular framework, allowing additional urban intelligence layers to be integrated as the project develops.

### Key Variables

The analytical workflow includes variables and features related to:

* Property sale price
* Transaction date
* London borough
* Property market activity
* Population statistics
* Crime indicators
* Borough-year derived features

Additional socioeconomic, accessibility, and deprivation-related features will be incorporated as further urban intelligence layers are integrated.

## Project Workflow

The project follows a modular data science workflow that progressively transforms raw property and urban datasets into a multi-layer London Intelligence Dataset.

The current workflow integrates the property, population, and crime layers, while the architecture allows additional urban intelligence datasets to be incorporated in future development stages.

```text
HM Land Registry Price Paid Data
                │
                ▼
      Property Data Processing
                │
                ▼
     Borough-level Property Dataset
                │
                ├───────────────┐
                ▼               ▼
        Population Layer     Crime Layer
          (ONS Data)      (London Crime Data)
                │               │
                └───────┬───────┘
                        ▼
          London Intelligence Dataset
                        │
                        ▼
          Data Validation & Quality Checks
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
          Exploratory Analysis & Insights
                        │
                        ▼
        Investment Analysis & Evaluation
                        │
                        ▼
          Future Predictive Modelling
```

Additional urban intelligence layers, including income, PTAL, and IMD, will be incorporated into the workflow as they are completed and integrated into the analytical dataset.

## Skills Demonstrated

This project demonstrates practical data science, data engineering, and business analytics skills, including:

* Data collection and integration from multiple public datasets
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Multi-source feature engineering
* Data validation and consistency checks
* Borough-level dataset construction
* Feature transformation and scaling
* Business-driven scoring model design
* Sensitivity analysis and scenario evaluation
* Data visualization for exploratory analysis and business insight communication
* Building reproducible notebook-based data workflows

## Key Results

The project has progressed through multiple development stages, each contributing to a more comprehensive understanding of London's residential property market. The key outcomes achieved so far include:

* Developed a borough-level investment scoring framework that identified **Wandsworth** as the highest-ranked borough based on the Robust Opportunity Score.
* Demonstrated how different weighting strategies can significantly influence borough rankings, highlighting the importance of aligning analytical models with investment objectives.
* Showed that applying log transformation to property prices reduced the influence of extreme values and produced a more balanced scoring model.
* Evaluated multiple machine learning models for predicting borough-level house price growth and found that the existing feature set was insufficient for reliable forecasting, motivating further feature engineering.
* Built a multi-layer London Intelligence Dataset by integrating property, population, and crime data, creating a stronger analytical foundation for future urban analysis and predictive modelling.

### Robust Opportunity Score

The Robust Opportunity Score combines multiple investment scenarios to identify London boroughs that consistently demonstrate strong investment potential. Unlike individual scoring methods, this composite score provides a more balanced and stable assessment of market opportunities.

<p align="center">
  <img src="visuals/robust_opportunity_score.png"
       alt="Top 10 London Boroughs by Robust Opportunity Score"
       width="800">
</p>

*Figure 1. Top 10 London boroughs ranked by the Robust Opportunity Score.*

------------------

## Version 2 – Predictive Modelling

## Objective

The objective of Version 2 was to evaluate whether historical borough-level market statistics could be used to predict average house price growth in the following year.

Rather than focusing solely on predictive performance, this stage investigates whether the currently available HM Land Registry features contain sufficient information to support reliable forecasting.

## Models Evaluated

The following models were implemented and compared:

- Baseline Model
- Linear Regression
- Random Forest
- Random Forest (without City of London)
- XGBoost

## Model Performance Summary

Model performance was evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²). The baseline model was used as the reference benchmark to assess whether more sophisticated machine learning models provided meaningful improvements.

| Model | MAE ↓ | RMSE ↓ | R² ↑ | Key Observation |
|-------|------:|-------:|------:|----------------|
| **Baseline** | **0.0773** | 0.1120 | -0.2289 | Benchmark model with the lowest MAE |
| Linear Regression | 0.0987 | 0.1499 | -1.2013 | Linear relationships were insufficient for accurate prediction |
| Random Forest | 0.1040 | 0.1513 | -1.2426 | Greater model complexity did not improve performance |
| **Random Forest (without City of London)** | 0.0792 | **0.1020** | **-0.1986** | Best RMSE and R² after removing an influential outlier |
| XGBoost | 0.1100 | 0.1772 | -2.0778 | Gradient boosting did not outperform the baseline |

### Interpretation of Results

The predictive modelling results show that increasing model complexity did not lead to meaningful improvements in forecasting next-year borough-level house price growth. Although Random Forest showed a slight improvement after removing the City of London from the analysis, none of the evaluated machine learning models consistently outperformed the baseline model.

These findings suggest that the main limitation lies in the information available within the current feature set rather than in the choice of algorithm. In other words, more sophisticated models alone cannot compensate for a lack of predictive features.

This outcome reflects an important principle in data science: building better predictive models often requires better data, richer features, and deeper domain knowledge—not simply more complex algorithms.

## Key Findings

None of the evaluated machine learning models outperformed the baseline model.

More complex algorithms, including Random Forest and XGBoost, did not produce better predictions than the simpler baseline approach.

A sensitivity analysis was also conducted by removing the City of London, which had previously shown unusually large annual price fluctuations. Although model performance improved slightly, the overall conclusions remained unchanged.

## Conclusion

The results suggest that the current feature set does not contain enough predictive information to model next-year house price growth reliably.

This indicates that the main limitation lies in the available features rather than in the choice of machine learning algorithm.

These findings motivate the next stage of the project, which will focus on feature engineering and the integration of additional external datasets.

## Project Evolution

The project has evolved through three major development stages:

* **Version 1** – Exploratory Data Analysis, feature engineering, and business scoring.
* **Version 2** – Predictive modelling using Linear Regression, Random Forest, and XGBoost.
* **Version 3 (Current)** – Development of a multi-layer London Intelligence Dataset by integrating external urban datasets to strengthen feature engineering and support more informative analysis and future predictive modelling.

### Version 3 Progress

The current Version 3 development has progressed from the initial property dataset towards a broader borough-year urban intelligence framework.

**Completed**

* ✅ Population Layer — ONS Mid-Year Population Estimates
* ✅ Crime Layer — London borough-level crime data

**Planned / In Progress**

* Income Layer
* Public Transport Accessibility Level (PTAL)
* Index of Multiple Deprivation (IMD)

The resulting London Intelligence Dataset is being progressively enriched with additional urban indicators to provide richer explanatory variables for investment analysis, feature engineering, and future predictive modelling.

## Future Development

The next stage of the project will focus on further enriching the London Intelligence Dataset and improving its analytical and predictive capabilities.

Planned future development includes:

* **Completing additional urban intelligence layers**, including income, Public Transport Accessibility Level (PTAL), and Index of Multiple Deprivation (IMD) data.
* **Integrating the completed layers** into the borough-year London Intelligence Dataset.
* **Expanding feature engineering** to create richer market, socioeconomic, accessibility, and urban intelligence features.
* **Revisiting predictive modelling** using the expanded feature set to evaluate whether additional urban indicators improve next-year property market forecasting.
* **Extending the investment analysis framework** by incorporating the newly engineered features and broader urban indicators.
* **Developing an interactive Streamlit dashboard** to communicate market patterns, borough-level insights, and investment indicators.
* **Preparing the project for deployment** as an interactive data science portfolio application.

## Repository Structure

```text
London-Property-Intelligence/
│
├── data/
│   ├── raw/
│   │   ├── pp-2018.csv
│   │   ├── pp-2019.csv
│   │   ├── pp-2020.csv
│   │   ├── pp-2021.csv
│   │   ├── pp-2022.csv
│   │   ├── pp-2023.csv
│   │   ├── pp-2024.csv
│   │   ├── pp-2025.csv
│   │   ├── borough_crime_historical.csv
│   │   ├── borough_income_taxpayers.xlsx
│   │   ├── borough_ptai_2015.csv
│   │   ├── ID_2019_for_London.xlsx
│   │   ├── london_borough_area.csv
│   │   └── ons_population_2022.xlsx
│   │
│   └── processed/
│       ├── borough_ptal_2015.csv
│       ├── borough_year_features.csv
│       ├── london_intelligence_dataset.csv
│       ├── london_intelligence_dataset_with_crime.csv
│       ├── london_population.csv
│       ├── london_transactions.csv
│       ├── london_transactions_2018_2025.csv
│       └── ptai_borough_2015.csv
│
├── docs/
│   ├── Data_Catalog.md
│   └── investment_decision_framework.md
│
├── notebooks/
│   ├── 01_exploring_hm_land_registry.ipynb
│   ├── 01_PTAL_Understanding.ipynb
│   ├── 02_build_london_transactions_dataset.ipynb
│   ├── 02_crime_data_understanding.ipynb
│   ├── 03_Build_Borough_Year_Dataset.ipynb
│   ├── 03_income_understanding.ipynb
│   ├── 04_deprivation_data_understanding.ipynb
│   ├── 04_Model_Development.ipynb
│   ├── 05_population_eda.ipynb
│   ├── 06_build_london_intelligence_dataset.ipynb
│   └── 07_crime_layer_eda.ipynb
│
├── reports/
├── src/
├── visuals/
│   └── robust_opportunity_score.png
│
├── .gitignore
├── LICENSE
├── PROJECT_STATE.md
├── README.md
└── requirements.txt
```

The repository is organised into separate directories for raw data, processed datasets, notebooks, documentation, visual outputs, and project resources.

* `data/raw/` contains source datasets used throughout the project's data exploration and integration workflow.
* `data/processed/` contains cleaned, transformed, and integrated datasets generated during the project.
* `notebooks/` contains notebooks covering data exploration, dataset construction, urban intelligence layers, feature engineering, and modelling.
* `docs/` contains supporting project documentation and the data catalogue.
* `visuals/` contains selected visual outputs used in the project.
* `reports/` is reserved for project reports and analytical outputs.
* `src/` is reserved for reusable project source code as the project develops.

## How to Run

The project is organised as a modular, notebook-based data science workflow. Individual notebooks cover data understanding, dataset construction, exploratory analysis, feature engineering, and modelling stages.

### Setup

1. Clone this repository.
2. Open the project in Visual Studio Code or Jupyter Notebook.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

The notebooks are organised by development stage rather than as a single linear execution pipeline.

The main workflow can be followed through the relevant notebooks in the `notebooks/` directory:

* **Property data exploration and processing**

  * `01_exploring_hm_land_registry.ipynb`
  * `02_build_london_transactions_dataset.ipynb`

* **Borough-year dataset construction**

  * `03_Build_Borough_Year_Dataset.ipynb`

* **Urban intelligence data exploration**

  * `01_PTAL_Understanding.ipynb`
  * `02_crime_data_understanding.ipynb`
  * `03_income_understanding.ipynb`
  * `04_deprivation_data_understanding.ipynb`
  * `05_population_eda.ipynb`

* **London Intelligence Dataset construction**

  * `06_build_london_intelligence_dataset.ipynb`
  * `07_crime_layer_eda.ipynb`

* **Predictive Modelling (Version 2)**

  * `04_Model_Development.ipynb`

Notebook names and outputs reflect the project's iterative development process. Processed datasets generated during the workflow are stored in `data/processed/`.

For reproducibility, notebooks should be run with the project dependencies installed and with the required source data available in the appropriate `data/raw/` directories.


## Data Availability

The project uses multiple public datasets to build a multi-layer London Intelligence Dataset. Source data are processed and integrated through the project notebooks before being used for analysis and feature engineering.

### Processed Datasets

The main processed datasets currently available in the project include:

* `data/processed/london_transactions.csv` — Cleaned London residential property transaction dataset used for exploratory analysis and feature engineering.
* `data/processed/london_intelligence_dataset.csv` — Multi-layer borough-year analytical dataset incorporating the property and population layers.
* `data/processed/london_intelligence_dataset_with_crime.csv` — Current extended analytical dataset incorporating property, population, and crime information.
* `data/processed/london_population.csv` — Processed borough-level population data.
* `data/processed/borough_year_features.csv` — Borough-year feature dataset used during the feature engineering workflow.

### Source Data

The project integrates data from multiple public sources, including:

* HM Land Registry Price Paid Data
* Office for National Statistics (ONS) population data
* London crime data
* Additional London datasets used for planned and ongoing intelligence layers

The original source datasets are retained separately from the processed analytical datasets and are documented through the project's data workflow and data catalogue.

### Data Documentation

A detailed description of the datasets, their sources, transformations, and intended use is maintained in:

`docs/Data_Catalog.md`

As the project evolves, additional external datasets will be integrated into the London Intelligence Dataset and corresponding processed outputs will be added to the repository.

## Author

Shiva

Data Science Portfolio Project

## License

This project is released under the MIT License.

See the `LICENSE` file for details.