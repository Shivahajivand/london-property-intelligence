# London Property Intelligence

## Portfolio Project

### Project Overview

London Property Intelligence is a data science project that analyzes residential property transactions across London's 33 administrative areas using HM Land Registry data.

The project explores market activity, property values, and investment opportunities through exploratory data analysis (EDA), feature engineering, business-driven scoring models, and data visualization.

Rather than focusing only on descriptive statistics, the analysis develops custom scoring methods to evaluate London boroughs from different investment perspectives and demonstrates how data can support real-world decision-making.

---

## Business Problem

Property investors often face a trade-off between expensive premium locations and highly active housing markets.

High property values may indicate prestigious locations, while high transaction activity may reflect stronger market liquidity and demand. Considering only one of these factors may lead to incomplete investment decisions.

This project investigates whether combining market activity and property values can provide a more balanced view of investment opportunities across London boroughs through a transparent, data-driven scoring approach.

## Dataset

The analysis uses the HM Land Registry Price Paid Data (PPD), an official UK government dataset containing residential property transaction records across England and Wales.

For this project, the dataset was filtered to include only transactions within Greater London, resulting in a borough-level analysis covering London's 33 administrative areas.

### Data Source

- HM Land Registry – Price Paid Data (PPD)
- Year: 2025

### Key Variables Used

- Property sale price
- Transaction date
- London borough (District)
- County

## Project Workflow

The project follows a structured data science workflow, transforming raw property transaction data into business-oriented market insights.

```text
HM Land Registry Price Paid Data (2025)
                │
                ▼
Filter Greater London Transactions
                │
                ▼
Explore Borough Activity & Average Property Prices
                │
                ▼
Engineer Investment Features
(Log Price Transformation & Scaling)
                │
                ▼
Build Market Opportunity Score
                │
                ▼
Evaluate Alternative Weighting Scenarios
                │
                ▼
Create Robust Opportunity Score
                │
                ▼
Generate Business Insights
```

## Skills Demonstrated

This project demonstrates practical data science techniques and business analytics skills, including:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Feature transformation and scaling
- Business-driven scoring model design
- Sensitivity analysis
- Data visualization
- Business insight communication

## Key Results

The analysis produced several key findings:

- Wandsworth achieved the highest Robust Opportunity Score, demonstrating a strong balance between market activity and property value.
- City of Westminster ranked highly due to its premium property prices despite lower transaction activity.
- Market rankings changed under different weighting scenarios, showing that investment opportunities depend on investor priorities.
- Applying a log transformation reduced the influence of extreme property prices and produced a more balanced scoring model.
- The Robust Opportunity Score identified boroughs that consistently performed well across multiple investment scenarios.

## Repository Structure

```text
London-Property-Intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── london_transactions.csv
│
├── docs/
├── notebooks/
│   └── 01_Exploring_HM_Land_Registry.ipynb
│
├── reports/
├── src/
├── visuals/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How to Run

1. Clone this repository.
2. Open the project in Visual Studio Code or Jupyter Notebook.
3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook located in the `notebooks` directory.
5. Run the notebook cells sequentially to reproduce the analysis.

## Future Development

Planned future improvements include:

- Integrating additional London open datasets
- Developing predictive machine learning models
- Building an interactive Streamlit dashboard
- Expanding the investment scoring framework
- Deploying the project as a portfolio application

## Author

Shiva

Data Science Portfolio Project


## Data Availability

The original HM Land Registry Price Paid dataset is not included in this repository because of its large file size.

The processed London dataset used throughout this project is available in:

`data/processed/london_transactions.csv`

The original dataset can be downloaded from the official HM Land Registry website.

## License

This project is released under the MIT License.

See the `LICENSE` file for details.