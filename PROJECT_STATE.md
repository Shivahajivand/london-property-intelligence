# London Property Intelligence

## Project Purpose

Build a professional end-to-end Data Science portfolio project that analyses London's residential property market and develops a borough-level intelligence system for investment analysis and predictive modelling.

---

# Project History

## Version 1 — Completed ✅

Objective:
Analyse HM Land Registry Price Paid Data for London.

Main achievements:

* Built the complete data processing pipeline from raw transactions.
* Aggregated transactions at borough level.
* Performed exploratory data analysis (EDA).
* Engineered borough-level property market features.
* Developed Investment Opportunity Score.
* Developed Robust Opportunity Score.
* Produced business insights and borough ranking.

Main conclusion:

Version 1 successfully identified attractive London boroughs using only property market data.

---

## Version 2 — Completed ✅

Objective:

Predict future borough house price growth using machine learning.

Models tested:

* Baseline Model
* Linear Regression
* Random Forest
* XGBoost

Main finding:

The limitation was not the machine learning algorithms.

The limitation was the available features.

This became the key lesson for the next version.

**Better features create better intelligence.**

---

## Version 3 — 

Objective:

Transform the project from a property analysis project into a London Property Intelligence platform by integrating multiple external datasets.

Current external datasets include:

* HM Land Registry
* PTAL (Public Transport Accessibility)
* Crime
* Income
* Deprivation
* Population
* Area

---

# Current Position

The project is currently building a borough-level master dataset that will become the foundation for all later modelling and analysis.

Current focus:

* Build Borough Dataset
* Merge borough-level external datasets
* Create a unified multi-layer London dataset


# Version 3 Architecture Update

## Current Development Phase

Version 3 has entered the multi-layer urban intelligence phase.

The project is moving from a single-source property market analysis into a multi-source London property intelligence system.

The goal is no longer only analysing historical property prices, but building a decision-support system that combines multiple urban datasets to evaluate London boroughs from an investment perspective.

---

# Notebook Responsibilities

## 02_build_london_transactions_dataset.ipynb

Purpose:

Build the clean multi-year London property transaction dataset from HM Land Registry Price Paid Data (2018–2025).

Workflow:

Raw HM Land Registry files

↓

Merge yearly datasets

↓

Filter Greater London transactions

↓

Create:

london_transactions_2018_2025.csv


This notebook creates the foundation dataset for all subsequent borough-level aggregation, feature engineering and modelling.

Status:

Completed ✅

---

## 03_build_borough_year_dataset.ipynb

Purpose:

Transform property transactions into a borough-year analytical dataset.

Each row represents:

One London borough + one calendar year


Created features include:

- Number of transactions
- Average property price
- Median property price
- Minimum and maximum price
- Price volatility
- Historical price growth features
- One-year forward prediction targets


Output:

borough_year_features.csv


Status:

Completed ✅

---

## 06_build_london_intelligence_dataset.ipynb

Purpose:

Build the final multi-layer London intelligence dataset by integrating property market data with additional urban datasets.

This notebook represents the core of Version 3.

The objective is:

"How can multiple urban intelligence datasets be combined to create better property investment decisions?"

Planned data layers:

1. Property Market Layer

Source:
HM Land Registry Price Paid Data

Current foundation:

borough_year_features.csv


2. Transport Accessibility Layer

Source:
PTAL data


3. Crime Layer

Source:
Metropolitan Police Crime Data


4. Income Layer

Source:
HMRC Income Data


5. Deprivation Layer

Source:
Index of Multiple Deprivation


6. Population and Density Layer

Source:
Population datasets and area information


Workflow:

Load validated datasets

↓

Check granularity and join keys

↓

Merge datasets carefully

↓

Perform Data Quality Audit after each integration step

↓

Create final London Intelligence Dataset


Expected output:

london_intelligence_dataset.csv


Status:

In Progress 🚧

---

# Core Design Principle

Each notebook has a single responsibility.

Data understanding and cleaning are performed in dedicated notebooks.

The final integration notebook only focuses on:

- Loading validated datasets
- Joining data layers
- Validating the final structure
- Producing the master intelligence dataset

This keeps the project reproducible, maintainable and easy to extend.
---

# Overall Architecture

Raw Data

↓

Data Understanding

↓

Cleaning & Preparation

↓

Borough-Level Feature Tables

↓

Master London Intelligence Dataset

↓

EDA

↓

Feature Engineering

↓

Machine Learning

↓

Business Insights

---

# Immediate Next Step

Continue developing the Borough Dataset and progressively integrate every external dataset into the Master London Intelligence Dataset.

Do not start new modelling work until the integrated dataset is complete.

---

# Working Rules

* Build first, document second.
* Keep this file short and practical.
* Update this document only after completing a major milestone.
* This file exists only to prevent losing project context between work sessions 

# Vision

## Mission

Build an intelligent decision-support system for London property investment using multi-source urban data.

---

## Core Question

**How can we combine multiple urban intelligence datasets to make better property investment decisions?**

---

## Final Outcome

The final product is **not** just a machine learning model.

It is a borough-level intelligence system that evaluates each London borough from multiple perspectives and supports evidence-based property investment decisions.

Each borough should have an intelligence profile similar to the following:

```text
Camden

Current Market
★★★★★

Crime
★★☆☆☆

Income
★★★★★

Transport
★★★★★

Deprivation
★☆☆☆☆

Population Density
★★★★★

Investment Opportunity
9.2 / 10

Predicted Growth
High

Overall Recommendation

Strong Long-Term Investment
```

---

## Success Criteria

By the end of Version 3, the project should be able to answer:

* Which London boroughs offer the best investment opportunities?
* Why are they attractive?
* Which urban factors influence the recommendation?
* What level of future growth is expected?
* How can multiple datasets be combined into one intelligent decision-support system?

---

## Project Compass

Whenever making a design decision, ask:

**"Does this make our London Property Intelligence System more intelligent?"**

If the answer is **Yes**, continue.

If the answer is **No**, postpone it or remove it.

## Latest Project State

### Current Phase

Version 3 is currently in the **multi-layer urban intelligence integration phase**.

The Population Layer has been successfully cleaned, validated and integrated into the London Intelligence Dataset.

The project is now continuing with the remaining external urban intelligence layers before moving to further feature engineering and predictive modelling.

---

## Latest Progress — Population Layer

### Completed

* Audited the ONS MYE4 population dataset.
* Verified dataset structure and metadata.
* Converted the dataset from wide format to long format.
* Filtered the data to the 33 London Boroughs.
* Cleaned the Year column (2011–2022).
* Validated:

  * 33 boroughs
  * 12 years
  * 396 borough-year records
  * No missing values
  * No duplicate Borough-Year pairs
* Saved the cleaned layer as:

`data/processed/london_population.csv`

### Integration

The cleaned Population Layer was successfully integrated into the London Intelligence Dataset.

Completed integration checks included:

* Standardised `Merge_Key`
* Resolved borough naming differences
* Verified dataset compatibility before merging
* Preserved the borough-year analytical grain
* Validated the merged dataset after integration
* Saved the updated:

`data/processed/london_intelligence_dataset.csv`

---

## Current Integration Status

### Completed

* Property Market Layer ✅
* Population Layer ✅

### In Progress

* PTAL / Transport Accessibility Layer 🚧
* Crime Layer 🚧
* Income Layer 🚧
* Deprivation / IMD Layer 🚧
* Area / Density features 🚧

---

## Current Priority

Complete and validate the remaining urban intelligence layers and progressively integrate them into the master London Intelligence Dataset.

No new predictive modelling should begin until the integrated multi-layer dataset is complete.

---

## Integration Rule

Every external dataset follows the same workflow:

```text
Load
↓
Audit
↓
Compatibility Check
↓
Merge Key Standardisation
↓
Merge
↓
Post-Merge Validation
↓
Save
```

The final integration notebook should only work with validated processed datasets.

---

## Project State Rule

This file should remain short and practical.

Update it only after a meaningful project milestone so that it always answers three questions:

1. Where are we?
2. What has been completed?
3. What is the next step?
