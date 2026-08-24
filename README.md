# London Property Intelligence

## End-to-End Data Science Portfolio Project

### Project Overview

**London Property Intelligence** is an end-to-end data science project that combines residential property market data with multiple urban intelligence layers to build a structured, borough-level analytical framework for London's housing market.

The project began with HM Land Registry residential property transactions and progressively expanded into a broader **London Intelligence Dataset**, integrating population, income, crime, public transport accessibility, and deprivation-related information.

The project then evolved from exploratory investment analysis into predictive modelling, culminating in a **time-aware machine learning framework for estimating 2025 house-price growth across London's 33 boroughs/districts**.

The project demonstrates an applied data science workflow covering:

* Multi-source data integration
* Data cleaning and validation
* Geographic harmonisation
* Borough-year dataset construction
* Feature engineering
* Exploratory data analysis
* Business-oriented investment analysis
* Time-aware model validation
* Target-specific model selection
* Missing-data imputation
* Imputation backtesting
* Sensitivity analysis
* District-level prediction
* Business interpretation
* Reproducible analytical workflows

---

# Business Problem

London's residential property market is highly heterogeneous.

Property prices, transaction activity, population, income, accessibility, crime, and other socioeconomic characteristics can vary substantially between boroughs. Evaluating a location using a single indicator therefore provides only a partial view of its market characteristics.

This project investigates how multiple urban and property-market indicators can be combined to provide a richer understanding of London's residential property landscape.

The analytical framework has two complementary objectives:

1. **Understand and compare London boroughs using historical market and urban intelligence.**
2. **Evaluate whether historical borough-level information can support next-year house-price-growth forecasting.**

The project therefore moves from descriptive and investment-oriented analysis towards predictive modelling while maintaining explicit validation, robustness checks, and transparent modelling assumptions.

---

# Data Sources

The project integrates multiple public datasets into a common borough-level analytical framework.

## Property Layer

**Source:** HM Land Registry Price Paid Data (PPD)

The property layer contains residential transaction records for Greater London and forms the core historical property-market dataset.

The project uses transaction data covering **2018–2025** for different stages of the analytical workflow.

The predictive modelling framework uses historical observations through 2023 for model training and 2024 feature values to generate **2025 predictions**.

Key property-market variables include:

* Transaction count
* Average price
* Median price
* Minimum price
* Maximum price
* Annual average-price growth
* Annual median-price growth

---

## Population Layer

**Source:** Office for National Statistics (ONS) Mid-Year Population Estimates

Population information is integrated at borough level and provides demographic context for the property-market analysis.

Population data contributes to the broader London Intelligence Dataset and urban intelligence analysis. It is not included among the 10 predictors of the final predictive modelling dataset.

---

## Income Layer

**Source:** HMRC Survey of Personal Incomes (SPI)

The income layer provides borough-level economic indicators including:

* Mean income
* Median income
* Number of individuals

The validated project income layer contains:

* 33 London boroughs
* 6 project years
* 198 borough-year observations
* No duplicate borough-year records
* No missing values

The income data is reported by tax year and is mapped to the project's calendar-year analytical structure where required.

---

## Crime Layer

**Source:** London crime data

Crime information is incorporated as an additional borough-level urban intelligence layer.

The crime workflow includes:

* Data understanding
* Data cleaning
* Geographic harmonisation
* Borough-level integration
* Exploratory analysis
* Post-integration validation

---

## Public Transport Accessibility Layer

**Source:** Public Transport Accessibility Level (PTAL)

PTAL is treated primarily as a geographic accessibility feature.

Because PTAL data is associated with a reference year rather than a complete annual time series equivalent to the property dataset, it is handled as a relatively static borough-level feature rather than artificially creating annual values.

---

## Deprivation Layer

**Source:** Index of Multiple Deprivation (IMD)

Deprivation information is incorporated according to its available reference year.

The project does not artificially extend a single IMD observation across years where equivalent temporal information is unavailable.

---

# London Intelligence Dataset

A major objective of the project is to construct a unified **borough-year analytical framework**.

A canonical borough reference based on official borough codes (`Borough_Code`) is used to harmonise geographic identifiers across datasets.

Source-specific borough names are normalised and mapped to the canonical reference, including naming differences such as:

* City of Westminster
* Westminster

The integration workflow includes:

* Geographic identifier harmonisation
* Borough-name standardisation
* Borough coverage validation
* Temporal alignment
* Merge validation
* Grain validation
* Duplicate detection
* Post-integration quality checks
* Removal of temporary helper fields

The intended analytical grain is:

> **One row per London Borough × Year**

The integrated dataset currently contains:

* **264 unique Borough-Year observations**
* **33 London boroughs/districts**
* **41 columns**
* **No duplicate Borough-Year combinations**

The integrated dataset is exported as:

`data/processed/london_property_intelligence_integrated_borough_year.parquet`

### Integrated Borough-Year Dataset

Following the integration and geographic harmonisation process, the project produces a controlled borough-year analytical dataset combining the available urban intelligence layers.

The integrated dataset is exported as:

`data/processed/london_property_intelligence_integrated_borough_year.parquet`

This dataset is used as the **controlled input** for the subsequent **integrated data quality and feature analysis** stage, where its structure, completeness, uniqueness, feature distributions, and analytical readiness are evaluated.

The resulting validated dataset provides the analytical foundation for subsequent feature engineering, modelling, and intelligence analysis.

---

# Data Availability

The project uses multiple public datasets to build a multi-layer London Intelligence Dataset.

Source data are processed, validated, harmonised, and integrated through the project notebooks before being used for feature engineering, exploratory analysis, investment analysis, and predictive modelling.

## Processed Datasets

The main processed datasets generated during the project include:

- `data/processed/london_transactions.csv` — Cleaned London residential property transaction dataset.

- `data/processed/london_transactions_2018_2025.csv` — London transaction dataset covering the project's full transaction period.

- `data/processed/borough_year_features.csv` — Borough-year property-market feature dataset.

- `data/processed/london_intelligence_dataset.csv` — Multi-layer borough-year analytical dataset.

- `data/processed/london_intelligence_dataset_with_crime.csv` — Extended analytical dataset incorporating crime information.

- `data/processed/london_population.csv` — Processed borough-level population data.

- `data/processed/london_crime.csv` — Processed borough-level crime dataset.

- `data/processed/london_income.csv` — Processed borough-level income dataset.

- `data/processed/london_imd.csv` — Processed deprivation / IMD dataset.

- `data/processed/borough_ptal_2015.csv` — Processed PTAL-related data.

- `data/processed/ptai_borough_2015.csv` — Borough-level public transport accessibility data.

- `data/processed/london_property_intelligence_integrated_borough_year.parquet` — Controlled integrated borough-year analytical dataset used for integrated data quality and feature analysis.

- `data/processed/london_property_final_predictive_features_targets.parquet` — Final modelling dataset containing the predictive features and target variables used in the predictive modelling workflow.

Final predictive outputs are stored separately in `notebooks/final_outputs/`.

---

## Source Data

The project integrates data from multiple public sources, including:

* HM Land Registry Price Paid Data
* Office for National Statistics (ONS) population estimates
* HMRC Survey of Personal Incomes
* London crime data
* Public Transport Accessibility Level (PTAL)
* Index of Multiple Deprivation (IMD)
* Supporting London geographic reference data

Original source datasets are retained separately from processed analytical datasets and are documented through the project's data workflow and data catalogue.

---

## Data Documentation

A detailed description of the datasets, sources, transformations, and intended analytical use is maintained in:

`docs/Data_Catalog.md`

---

# Project Evolution

The project has evolved through three major development stages.

## Version 1 — Exploratory & Investment Analysis

The first stage focused on understanding London's residential property market and developing borough-level investment analysis.

Key activities included:

* Property transaction exploration
* Price distribution analysis
* Feature engineering
* Borough-level comparisons
* Investment scoring
* Robustness analysis
* Sensitivity to scoring assumptions

A **Robust Opportunity Score** was developed to combine multiple investment scenarios into a more stable borough-level ranking.

The analysis identified **Wandsworth** as the highest-ranked borough under the original Robust Opportunity Score framework.

This stage demonstrated the importance of defining the analytical objective before selecting weights, transformations, and scoring methodologies.

---

## Version 2 — Initial Predictive Modelling

Version 2 evaluated whether historical property-market features alone were sufficient to predict next-year borough-level house-price growth.

Several models were compared, including:

* Baseline model
* Linear Regression
* Random Forest
* Random Forest without City of London
* XGBoost

Performance was evaluated using:

* MAE
* RMSE

The results showed that increasing model complexity did not automatically produce better forecasts.

The baseline remained competitive, while removing the City of London produced some improvement in Random Forest performance.

The main conclusion was that **feature quality and information content were more important limitations than algorithmic complexity alone**.

This finding motivated the expansion of the project towards a richer London Intelligence Dataset.

---

# Version 3 — Integrated London Intelligence & Time-Based Forecasting

Version 3 represents the current major development stage.

The project expanded beyond property-only features by integrating additional urban intelligence layers and developing a more rigorous predictive framework.

The current predictive modelling stage focuses on forecasting:

> **2025 Average Price Growth and Median Price Growth for London's 33 boroughs/districts.**

The final modelling workflow incorporates:

* Historical property-market indicators
* Population information
* Income information
* PTAL
* Other validated borough-level intelligence features
* Geographic harmonisation
* Integrated data-quality analysis
* Time-aware validation
* Target-specific model selection
* 2024 socioeconomic-data imputation
* Imputation backtesting
* Sensitivity analysis
* Full historical retraining
* 2025 district-level prediction

---

# Final Predictive Modelling Framework

## Prediction Targets

Two targets are modelled separately:

1. **Average Price Growth**
2. **Median Price Growth**

The separation is intentional because average and median price growth can behave differently across London districts.

This allows the modelling framework to capture potentially different patterns in the two price-growth measures rather than forcing a single model to explain both targets.

---

# Final Training Dataset

The final historical modelling dataset contains:

* **198 observations**
* **33 London districts**
* **6 historical years**
* **2018–2023**
* **10 predictors**
* **2 prediction targets**

The 10 final predictors are:

1. Transactions
2. Average Price
3. Median Price
4. Minimum Price
5. Maximum Price
6. Average Price Growth
7. Median Price Growth
8. Number of Individuals
9. Median Income
10. AvPTAI2015

No missing predictor or target values remained in the final training dataset.

---

# Time-Aware Validation

Random train/test splitting was not used as the primary validation strategy.

Instead, the project uses **expanding time-series validation** to better reflect the real forecasting problem.

The principle is:

> Historical information is used to predict a future period without allowing future observations to influence the training process.

A separate **2023 holdout evaluation** was also used as an additional robustness check.

Model selection therefore considered both:

* Predictive performance
* Temporal robustness

This approach reduces the risk of temporal leakage and provides a more realistic evaluation of forecasting performance.

---

# Final Models

Different models were selected for the two prediction targets.

## Average Price Growth

**Final Model: Ridge Regression**

Configuration:

* Alpha = 100
* StandardScaler preprocessing
* Ridge regression

Performance:

* Expanding validation MAE: **0.090782**
* 2023 holdout MAE: **0.068535**
* 2023 holdout RMSE: **0.082127**

---

## Median Price Growth

**Final Model: Random Forest Regressor**

Configuration:

* `n_estimators = 300`
* `max_depth = 4`
* `min_samples_leaf = 8`
* `random_state = 42`

Performance:

* Expanding validation MAE: **0.039287**
* 2023 holdout MAE: **0.034584**
* 2023 holdout RMSE: **0.048796**

Different models were selected because the two prediction targets exhibited different predictive behaviour.

---

# 2024 Imputation

The final 2025 prediction requires feature values representing the 2024 information available immediately before the forecast year.

Some socioeconomic variables required estimation for 2024.

Rather than treating these values as observed facts, the project explicitly treats them as **modelling assumptions**.

Two socioeconomic variables were particularly relevant:

* Number of Individuals
* Median Income

Several approaches for estimating missing 2024 values were evaluated and the imputation strategies were validated using historical backtesting.

This allows the imputation process to be evaluated rather than simply inserted into the modelling pipeline without validation.

---

# Imputation Sensitivity Analysis

Because 2024 socioeconomic values contain estimation uncertainty, a sensitivity analysis was performed.

The baseline 2024 values were perturbed by:

* −10%
* −5%
* 0%
* +5%
* +10%

Three sensitivity scenarios were evaluated:

1. Number of Individuals only
2. Median Income only
3. Both variables simultaneously

For the combined perturbation scenario, the mean predicted Average Price Growth changed approximately as follows:

| Shock | Mean Predicted Average Growth |
| ----: | ----------------------------: |
|  −10% |                        +1.33% |
|   −5% |                        +0.79% |
|    0% |                        +0.25% |
|   +5% |                        −0.30% |
|  +10% |                        −0.84% |

The sensitivity analysis demonstrates that the 2025 estimates are not independent of the assumptions used for the 2024 socioeconomic variables.

Therefore, the resulting rankings should be interpreted as **model-based estimates rather than deterministic forecasts**.

---

# 2025 Prediction Results

The final models were retrained using the available historical training data and applied to the 2024 prediction feature set.

The prediction input contains:

* **33 London districts**
* **10 predictors**
* **2024 feature values**

The resulting dataset contains predictions for both:

* Average Price Growth
* Median Price Growth

An overall ranking framework was then used to compare the predicted performance of the 33 districts.

---

# Key 2025 Predictions

The final ranking identifies substantial heterogeneity across London.

## Highest-Ranked Districts

The current Top 10 are:

| Rank | District             |
| ---: | -------------------- |
|    1 | Sutton               |
|    2 | Barking and Dagenham |
|    3 | Newham               |
|    3 | Croydon              |
|    5 | Enfield              |
|    6 | Havering             |
|    7 | Waltham Forest       |
|    8 | Redbridge            |
|    9 | Haringey             |
|   10 | Bromley              |

**Sutton** has:

* Predicted Average Price Growth: **+3.74%**
* Predicted Median Price Growth: **+2.77%**

**Barking and Dagenham** has the highest predicted Median Price Growth among the districts:

* Predicted Median Price Growth: **+4.56%**

These values represent model-generated estimates conditional on the project's modelling assumptions and input features.

---

# Lowest-Ranked Districts

The current Bottom 10 include:

* Merton
* Barnet
* Kingston upon Thames
* Lambeth
* Camden
* Wandsworth
* Hammersmith and Fulham
* Kensington and Chelsea
* Tower Hamlets
* City of Westminster

**City of Westminster** has the lowest predicted values across both targets:

* Predicted Average Price Growth: **−6.15%**
* Predicted Median Price Growth: **−4.29%**

These results should be interpreted as model predictions rather than guaranteed future market outcomes.

---

# Average vs Median Price Growth

One important finding is that Average Price Growth and Median Price Growth do not always produce the same signal.

For example:

### Kingston upon Thames

* Average Growth: **−2.36%**
* Median Growth: **+0.91%**

### Southwark

* Average Growth: **+2.04%**
* Median Growth: **−0.68%**

This demonstrates why relying on a single price-growth metric may obscure meaningful differences in district-level market behaviour.

The use of two targets therefore provides a more nuanced view of predicted market dynamics.

---

# Business Interpretation

The modelling results suggest that London's housing market should not be treated as a homogeneous market.

Predicted growth rates vary substantially across districts.

The results indicate that some outer and eastern districts receive stronger predicted growth signals, while several high-value central districts receive weaker predictions.

However, these results should not be interpreted as evidence that location alone determines future house-price performance.

The predictions reflect relationships learned from historical data and are conditional on:

* The selected feature set
* Historical relationships
* The modelling methodology
* 2024 input assumptions
* The imputation strategy

Potential applications include:

* Property investment screening
* Borough prioritisation
* Market segmentation
* Location-based strategy
* Housing-market monitoring
* Scenario analysis

---

# Robust Opportunity Score

Earlier versions of the project developed a **Robust Opportunity Score** to combine multiple investment scenarios and identify boroughs that performed consistently across different weighting assumptions.

The original scoring framework identified **Wandsworth** as the highest-ranked borough.

This analysis remains an important part of the project's evolution because it demonstrates the difference between:

* Rule-based investment scoring
* Predictive machine learning
* Scenario analysis

The project therefore does not treat predictive modelling as a replacement for all previous analytical approaches. Instead, the different components provide complementary perspectives.

---

# Limitations

The final modelling framework has several important limitations.

## 1. 2024 Imputation

Some 2024 socioeconomic variables were estimated rather than directly observed.

Sensitivity analysis demonstrates that these assumptions can influence the resulting predictions.

## 2. Limited Historical Sample

The final modelling dataset contains 198 borough-year observations.

Although this provides multiple years of observations across all 33 districts, it remains a relatively small dataset for machine learning.

## 3. Historical Relationships

The models learn relationships from historical observations.

Unexpected future changes in:

* Interest rates
* Housing policy
* Economic conditions
* Employment
* Migration
* Housing supply
* Housing demand
* Other macroeconomic conditions

may not be fully captured.

## 4. Forecast Uncertainty

The model predictions are estimates rather than guaranteed outcomes.

District rankings may change if future socioeconomic and housing-market conditions differ substantially from historical patterns.

## 5. Target Differences

Average and median price growth can produce different signals.

Consequently, a single overall ranking should not be interpreted as a complete representation of housing-market conditions.

---

# Final Project Outcome

The current project combines:

* Multi-source urban data integration
* Borough-level geographic harmonisation
* Data validation
* Feature engineering
* Exploratory analysis
* Investment scoring
* Time-aware model validation
* Target-specific model selection
* 2024 socioeconomic-data imputation
* Imputation backtesting
* Sensitivity analysis
* Full historical model retraining
* 2025 district-level prediction
* Ranking and comparative analysis
* Business interpretation
* Reproducible final outputs

The central conclusion is that **London's housing market exhibits substantial district-level heterogeneity**.

The project demonstrates that useful property-market intelligence requires more than simply predicting prices. It requires careful data integration, temporal validation, explicit assumptions, robustness analysis, and clear communication of uncertainty.

---

# Final Deliverables

The final predictive modelling workflow produces three primary outputs:

notebooks/final_outputs/
│
├── London_Housing_2025_Final_Predictions.csv
├── London_Housing_2025_Sensitivity_Analysis.csv
└── London_Housing_2025_Final_Results.xlsx
```

The final prediction dataset contains:

* 33 London districts
* Predicted Average Price Growth
* Predicted Median Price Growth
* Overall ranking information

The sensitivity-analysis output contains:

* 495 scenario-level observations
* Three sensitivity types
* Five shock levels
* District-level predictions

The Excel workbook provides a consolidated final-results format suitable for inspection and further analysis.

---

# Project Workflow

The project follows the following high-level workflow:

```text
HM Land Registry Price Paid Data
                │
                ▼
      Property Data Exploration
                │
                ▼
      London Transactions Dataset
                │
                ▼
      Borough-Year Property Dataset
                │
       ┌────────┼────────┬──────────┐
       ▼        ▼        ▼          ▼
   Population  Income   Crime      PTAL
       │        │        │          │
       └────────┴────────┴──────────┘
                │
                ▼
         Deprivation / IMD
                │
                ▼
     London Intelligence Dataset
                │
                ▼
     Geographic Harmonisation
                │
                ▼
 Data Quality & Feature Analysis
                │
                ▼
 Exploratory & Investment Analysis
                │
                ▼
 Time-Based Predictive Modelling
                │
                ▼
 2024 Imputation & Backtesting
                │
                ▼
     Sensitivity Analysis
                │
                ▼
 2025 District-Level Predictions
                │
                ▼
 Final Rankings & Business Interpretation
```

The workflow is modular rather than a single uninterrupted execution pipeline. Individual notebooks document specific analytical stages and development decisions.

---

# Repository Structure

```text
London-Property-Intelligence/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── Data_Catalog.md
│   └── investment_decision_framework.md
│
├── notebooks/
│   │
│   ├── 01_exploring_hm_land_registry.ipynb
│   ├── 01_PTAL_Data_Understanding.ipynb
│   │
│   ├── 02_build_london_transactions_dataset.ipynb
│   ├── 02_crime_data_understanding.ipynb
│   │
│   ├── 03_Build_Borough_Year_Dataset.ipynb
│   ├── 03_income_data_understanding.ipynb
│   │
│   ├── 04_deprivation_data_understanding.ipynb
│   ├── 04_Model_Development.ipynb
│   │
│   ├── 05_population_eda.ipynb
│   ├── 06_build_london_intelligence_dataset.ipynb
│   ├── 07_crime_layer_eda.ipynb
│   ├── 08_income_layer_eda.ipynb
│   │
│   ├── integrated_data_quality_and_feature_analysis.ipynb
│   ├── integration.ipynb
│   ├── Predictive_Modelling_and_Time_Based_Validation.ipynb
│   │
│   └── final_outputs/
│       ├── London_Housing_2025_Final_Predictions.csv
│       ├── London_Housing_2025_Sensitivity_Analysis.csv
│       └── London_Housing_2025_Final_Results.xlsx
│
├── reports/
│
├── src/
│
├── visuals/
│   └── robust_opportunity_score.png
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The repository is organised into separate directories for:

* Raw and processed data
* Analytical notebooks
* Final predictive outputs
* Supporting documentation
* Reports
* Reusable source code
* Visual outputs


---

# Notebook Guide

The notebooks are organised by analytical purpose rather than requiring a single uninterrupted execution sequence.

## Property Data

### `01_exploring_hm_land_registry.ipynb`

Explores the raw HM Land Registry property transaction data.

### `02_build_london_transactions_dataset.ipynb`

Builds the cleaned London residential transaction dataset.

### `03_Build_Borough_Year_Dataset.ipynb`

Constructs the borough-year property-market dataset.

---

## Urban Intelligence Layers

### `01_PTAL_Data_Understanding.ipynb`

Explores and validates PTAL data.

### `02_crime_data_understanding.ipynb`

Explores and prepares the crime dataset.

### `03_income_data_understanding.ipynb`

Explores and prepares the income dataset.

### `04_deprivation_data_understanding.ipynb`

Explores and prepares deprivation/IMD data.

### `05_population_eda.ipynb`

Performs exploratory analysis of population data.

---

## Intelligence Dataset Construction

### `06_build_london_intelligence_dataset.ipynb`

Builds the multi-layer London Intelligence Dataset.

### `07_crime_layer_eda.ipynb`

Performs exploratory analysis of the integrated crime layer.

### `08_income_layer_eda.ipynb`

Performs exploratory analysis of the integrated income layer.

### `integration.ipynb`

Performs the broader cross-source integration and geographic harmonisation workflow.

This stage establishes the canonical borough reference, aligns datasets by geographic and temporal dimensions, validates merge behaviour, and produces the controlled integrated borough-year dataset.

### `integrated_data_quality_and_feature_analysis.ipynb`

Performs integrated dataset quality checks and feature-level analysis.

This includes evaluation of:

* Dataset structure
* Borough-year uniqueness
* Completeness
* Missing values
* Feature distributions
* Data quality
* Analytical readiness

The notebook operates on the controlled integrated borough-year dataset produced by the integration stage.

---

## Predictive Modelling

### `04_Model_Development.ipynb`

Contains the earlier predictive modelling development and model comparison work associated with Version 2.

### `Predictive_Modelling_and_Time_Based_Validation.ipynb`

Contains the current final predictive modelling workflow, including:

* Time-based validation
* Model selection
* Final model training
* 2024 socioeconomic-data imputation
* Imputation backtesting
* Sensitivity analysis
* 2025 predictions
* Final rankings
* Final model diagnostics
* Export of final deliverables

This notebook represents the project's **current modelling endpoint**.

---

# How to Run

The project is organised as a modular, notebook-based workflow.

## Setup

1. Clone this repository.
2. Open the project in Visual Studio Code or Jupyter Notebook.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure the required source datasets are available in the appropriate `data/raw/` directories.

---

## Running the Project

The notebooks represent different analytical stages and are not necessarily intended to be executed as one uninterrupted linear script.

A recommended high-level order is:

1. Explore and process the HM Land Registry data.
2. Construct the London transaction dataset.
3. Build the borough-year property dataset.
4. Explore and prepare the population, income, crime, PTAL, and deprivation layers.
5. Build and explore the relevant intelligence layers.
6. Run the broader integration workflow.
7. Generate the controlled integrated borough-year dataset.
8. Run integrated data quality and feature analysis.
9. Review the earlier investment and predictive modelling workflows.
10. Run the final predictive modelling and time-based validation notebook.
11. Review the final prediction and sensitivity outputs.

The final predictive modelling notebook should be interpreted as the project's **current modelling endpoint**, while the earlier notebooks document the project's development history and analytical evolution.

---

# Reproducibility

The project follows reproducible data science practices including:

* Explicit data-processing stages
* Validated geographic mappings
* Controlled dataset grain
* Feature-order validation
* Missing-value checks
* Temporal validation
* Explicit model configurations
* Fixed random state for the Random Forest model
* Exported final prediction datasets
* Exported sensitivity-analysis results
* Documented modelling assumptions

Because several source datasets are external public datasets, complete reproduction also depends on access to the relevant source files and their historical versions.

---

# Skills Demonstrated

This project demonstrates practical skills across data science, analytics, and data engineering, including:

* Python
* pandas
* NumPy
* scikit-learn
* Data cleaning
* Data integration
* Geographic harmonisation
* Feature engineering
* Exploratory Data Analysis
* Data validation
* Time-aware validation
* Regression modelling
* Random Forest
* Ridge Regression
* Model comparison
* Hyperparameter selection
* Missing-data imputation
* Backtesting
* Sensitivity analysis
* Scenario analysis
* Data visualisation
* Business interpretation
* Reproducible notebook workflows
* Structured analytical dataset design

---

# Future Development

The current project provides a strong analytical and predictive foundation, but several extensions remain possible.

Potential future development includes:

* Further enrichment of the London Intelligence Dataset
* Additional socioeconomic and economic indicators
* More detailed accessibility features
* Macroeconomic variables
* Additional temporal observations as they become available
* More advanced uncertainty estimation
* Model monitoring and forecast evaluation
* Interactive Streamlit dashboard
* API-based model serving
* Production-oriented deployment
* Automated data pipelines
* Cloud deployment

An important future step is to compare the **2025 predictions against actual 2025 outcomes once reliable observed data is available**.

This would provide a genuine out-of-sample evaluation of the forecasting framework and allow the project's predictive performance to be assessed against realised market outcomes.

---

# Project Status

**Current status: Active portfolio project**

The project has completed a substantial end-to-end modelling stage, including:

* Integrated London urban intelligence dataset
* Validated borough-year structure
* Integrated data quality and feature analysis
* Target-specific final models
* Time-aware validation
* 2024 socioeconomic imputation
* Imputation backtesting
* Sensitivity analysis
* 2025 predictions
* Final rankings
* Final CSV and Excel deliverables

The project can continue to evolve towards interactive analysis, production deployment, and post-hoc evaluation of the 2025 forecasts.

---

# Author

**Shiva**

Data Science Portfolio Project

---

# License

This project is released under the MIT License.

See `LICENSE` for details.
