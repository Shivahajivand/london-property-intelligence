import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="London Property Intelligence",
    page_icon="🏠",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent

HISTORICAL_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "london_property_intelligence_integrated_borough_year.parquet"
)

PREDICTIONS_PATH = (
    PROJECT_ROOT
    / "notebooks"
    / "final_outputs"
    / "London_Housing_2025_Final_Predictions.csv"
)

SENSITIVITY_PATH = (
    PROJECT_ROOT
    / "notebooks"
    / "final_outputs"
    / "London_Housing_2025_Sensitivity_Analysis.csv"
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    historical = pd.read_parquet(HISTORICAL_DATA_PATH)
    predictions = pd.read_csv(PREDICTIONS_PATH)
    sensitivity = pd.read_csv(SENSITIVITY_PATH)

    return historical, predictions, sensitivity


# ============================================================
# LOAD DATA
# ============================================================

try:

    historical, predictions, sensitivity = load_data()

except Exception as e:

    st.error("An error occurred while loading the dashboard data.")
    st.exception(e)
    st.stop()


# ============================================================
# BASIC VALIDATION
# ============================================================

required_historical_columns = {
    "District",
    "Borough_Code",
    "Year",
    "Transactions",
    "Average_Price",
    "Median_Price",
    "Average_Price_Growth",
    "Median_Price_Growth",
    "Number_of_Individuals",
    "Median_Income",
    "AvPTAI2015",
}

required_prediction_columns = {
    "District",
    "Borough_Code",
    "Year",
    "Predicted_Average_Price_Growth",
    "Predicted_Median_Price_Growth",
    "Predicted_Average_Growth_%",
    "Predicted_Median_Growth_%",
    "Average_Growth_Rank",
    "Median_Growth_Rank",
    "Combined_Rank",
    "Overall_Rank",
}

required_sensitivity_columns = {
    "Sensitivity_Type",
    "Scenario",
    "Shock",
    "District",
    "Predicted_Average_Price_Growth",
    "Predicted_Median_Price_Growth",
    "Average_Growth_Change",
    "Median_Growth_Change",
}


missing_historical = required_historical_columns - set(historical.columns)
missing_predictions = required_prediction_columns - set(predictions.columns)
missing_sensitivity = required_sensitivity_columns - set(sensitivity.columns)


if missing_historical:
    st.error(
        f"Historical dataset is missing columns: "
        f"{sorted(missing_historical)}"
    )
    st.stop()


if missing_predictions:
    st.error(
        f"Prediction dataset is missing columns: "
        f"{sorted(missing_predictions)}"
    )
    st.stop()


if missing_sensitivity:
    st.error(
        f"Sensitivity dataset is missing columns: "
        f"{sorted(missing_sensitivity)}"
    )
    st.stop()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🏠 London Property Intelligence")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 London Overview",
        "📍 District Intelligence",
        "🔮 2025 Predictions",
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Data-driven London housing intelligence"
)

# ============================================================
# PAGE 1 — LONDON OVERVIEW
# ============================================================

if page == "🏠 London Overview":

    st.title("🏠 London Property Intelligence")

    st.markdown(
        """
        ### London Overview

        A data-driven view of London's property market,
        urban characteristics, and 2025 housing growth outlook.
        """
    )

    # --------------------------------------------------------
    # BASIC LONDON METRICS
    # --------------------------------------------------------

    latest_year = historical["Year"].max()

    latest_data = historical[
        historical["Year"] == latest_year
    ].copy()

    total_districts = historical["District"].nunique()

    total_transactions = historical["Transactions"].sum()

    latest_average_price = latest_data["Average_Price"].mean()

    latest_average_growth = (
        latest_data["Average_Price_Growth"]
        .dropna()
        .mean()
    )

    # --------------------------------------------------------
    # KPI SECTION
    # --------------------------------------------------------

    st.markdown("### 📊 Market Snapshot")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Districts",
        f"{total_districts}"
    )

    col2.metric(
        "Total Transactions",
        f"{total_transactions:,.0f}"
    )

    col3.metric(
        f"Average Price ({latest_year})",
        f"£{latest_average_price:,.0f}"
    )

    col4.metric(
        f"Average Growth ({latest_year})",
        f"{latest_average_growth:.1%}"
    )

    st.markdown("---")

    # ========================================================
    # HISTORICAL MARKET TREND
    # ========================================================

    st.subheader("📈 London Housing Market Trend")

    yearly_market = (
        historical
        .groupby("Year")
        .agg(
            Average_Price=("Average_Price", "mean"),
            Median_Price=("Median_Price", "median")
        )
        .reset_index()
    )

    import plotly.graph_objects as go

    fig_trend = go.Figure()

    fig_trend.add_trace(
        go.Scatter(
            x=yearly_market["Year"],
            y=yearly_market["Average_Price"],
            mode="lines+markers",
            name="Average Price"
        )
    )

    fig_trend.add_trace(
        go.Scatter(
            x=yearly_market["Year"],
            y=yearly_market["Median_Price"],
            mode="lines+markers",
            name="Median Price"
        )
    )

    fig_trend.update_layout(
        title="Historical London Property Prices",
        xaxis_title="Year",
        yaxis_title="Price (£)",
        hovermode="x unified",
        height=450,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

    st.caption(
        "Historical property prices across London's 33 districts."
    )

    # ========================================================
    # 2025 GROWTH OUTLOOK
    # ========================================================

    st.markdown("---")

    st.subheader("🔮 2025 Growth Outlook")

    st.markdown(
        """
        Predicted price growth across London districts,
        based on the final validated modelling pipeline.
        """
    )

    top_10 = (
        predictions
        .sort_values("Overall_Rank")
        .head(10)
        .copy()
    )

    top_10 = top_10.sort_values(
        "Predicted_Average_Growth_%",
        ascending=True
    )

    fig_growth = go.Figure(
        go.Bar(
            x=top_10["Predicted_Average_Growth_%"],
            y=top_10["District"],
            orientation="h",
            text=(
                top_10["Predicted_Average_Growth_%"]
                .map(lambda x: f"{x:.1f}%")
                ),
            textposition="outside"
        )
    )

    fig_growth.update_layout(
        title="Top 10 Districts by Predicted Average Price Growth",
        xaxis_title="Predicted Growth",
        yaxis_title="",
        height=500,
        margin=dict(l=20, r=80, t=60, b=20)
    )

    st.plotly_chart(
        fig_growth,
        use_container_width=True
    )

    # ========================================================
    # TOP 5 PREDICTIONS
    # ========================================================

    st.subheader("🏆 Top 5 Districts — Overall Ranking")

    top_5 = (
        predictions
        .sort_values("Overall_Rank")
        .head(5)
        [
            [
                "Overall_Rank",
                "District",
                "Predicted_Average_Growth_%",
                "Predicted_Median_Growth_%",
            ]
        ]
        .copy()
    )

    top_5.columns = [
        "Rank",
        "District",
        "Predicted Average Growth",
        "Predicted Median Growth"
    ]

    top_5["Predicted Average Growth"] = (
        top_5["Predicted Average Growth"]
        .map(lambda x: f"{x:.1f}%")
    )

    top_5["Predicted Median Growth"] = (
        top_5["Predicted Median Growth"]
        .map(lambda x: f"{x:.1f}%")
    )

    st.dataframe(
        top_5,
        use_container_width=True,
        hide_index=True
    )
    # ========================================================
    # DATA / METHODOLOGY NOTE
    # ========================================================

    st.markdown("---")

    st.caption(
        "Data covers 33 London districts. "
        "Historical market data spans 2018–2025. "
        "2025 predictions are generated from the final modelling pipeline."
    )

# ============================================================
# PAGE 2 — DISTRICT INTELLIGENCE
# ============================================================

elif page == "📍 District Intelligence":

    st.title("📍 District Intelligence")

    st.markdown(
        """
        Explore the historical property market and urban
        characteristics of an individual London district.
        """
    )

    # --------------------------------------------------------
    # DISTRICT SELECTION
    # --------------------------------------------------------

    districts = sorted(
        historical["District"].dropna().unique()
    )

    selected_district = st.selectbox(
        "Select a District",
        districts
    )

    district_data = (
        historical[
            historical["District"] == selected_district
        ]
        .sort_values("Year")
        .copy()
    )

    # Latest available historical year
    latest_district_data = district_data.iloc[-1]

    # --------------------------------------------------------
    # DISTRICT PROFILE
    # --------------------------------------------------------

    st.markdown("---")

    st.subheader(
        f"🏙️ {selected_district}"
    )

    profile_col1, profile_col2, profile_col3 = st.columns(3)

    profile_col1.metric(
        "Average Price",
        f"£{latest_district_data['Average_Price']:,.0f}"
    )

    profile_col2.metric(
        "Median Price",
        f"£{latest_district_data['Median_Price']:,.0f}"
    )

    profile_col3.metric(
        "Transactions",
        f"{latest_district_data['Transactions']:,.0f}"
    )

    profile_col4, profile_col5, profile_col6 = st.columns(3)

    population = latest_district_data["Number_of_Individuals"]
    income = latest_district_data["Median_Income"]
    ptal = latest_district_data["AvPTAI2015"]

    profile_col4.metric(
        "Population",
        f"{population:,.0f}"
        if pd.notna(population)
        else "N/A"
    )

    profile_col5.metric(
        "Median Income",
        f"£{income:,.0f}"
        if pd.notna(income)
        else "N/A"
    )

    profile_col6.metric(
        "PTAL",
        f"{ptal:.2f}"
        if pd.notna(ptal)
        else "N/A"
    )

    # ========================================================
    # HISTORICAL PROPERTY PRICES
    # ========================================================

    st.markdown("---")

    st.subheader("📈 Historical Property Prices")

    fig_district_prices = go.Figure()

    fig_district_prices.add_trace(
        go.Scatter(
            x=district_data["Year"],
            y=district_data["Average_Price"],
            mode="lines+markers",
            name="Average Price"
        )
    )

    fig_district_prices.add_trace(
        go.Scatter(
            x=district_data["Year"],
            y=district_data["Median_Price"],
            mode="lines+markers",
            name="Median Price"
        )
    )

    fig_district_prices.update_layout(
        xaxis_title="Year",
        yaxis_title="Price (£)",
        hovermode="x unified",
        height=450,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(
        fig_district_prices,
        use_container_width=True
    )

    # ========================================================
    # HISTORICAL PRICE GROWTH
    # ========================================================

    st.subheader("📊 Historical Price Growth")

    growth_data = district_data.dropna(
        subset=[
            "Average_Price_Growth",
            "Median_Price_Growth"
        ]
    )

    fig_growth = go.Figure()

    fig_growth.add_trace(
        go.Scatter(
            x=growth_data["Year"],
            y=growth_data["Average_Price_Growth"],
            mode="lines+markers",
            name="Average Price Growth"
        )
    )

    fig_growth.add_trace(
        go.Scatter(
            x=growth_data["Year"],
            y=growth_data["Median_Price_Growth"],
            mode="lines+markers",
            name="Median Price Growth"
        )
    )

    fig_growth.update_layout(
        xaxis_title="Year",
        yaxis_title="Growth",
        yaxis_tickformat=".1%",
        hovermode="x unified",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(
        fig_growth,
        use_container_width=True
    )

    # ========================================================
    # 2025 PREDICTION
    # ========================================================

    st.markdown("---")

    st.subheader("🔮 2025 Prediction")

    district_prediction = predictions[
        predictions["District"] == selected_district
    ]

    if not district_prediction.empty:

        prediction_row = district_prediction.iloc[0]

        pred_col1, pred_col2, pred_col3 = st.columns(3)

        pred_col1.metric(
            "Predicted Average Growth",
            f"{prediction_row['Predicted_Average_Growth_%']:.1f}%"
        )

        pred_col2.metric(
            "Predicted Median Growth",
            f"{prediction_row['Predicted_Median_Growth_%']:.1f}%"
        )

        pred_col3.metric(
            "Overall Rank",
            f"#{int(prediction_row['Overall_Rank'])}"
        )

    else:

        st.info(
            "No 2025 prediction is available for this district."
        )

# ============================================================
# PAGE 3 — 2025 PREDICTIONS
# ============================================================

elif page == "🔮 2025 Predictions":

    st.title("🔮 2025 London Housing Predictions")

    st.markdown(
        "Final model predictions and district rankings "
        "for expected 2025 housing price growth."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Districts Predicted",
        len(predictions)
    )

    col2.metric(
        "Top Overall District",
        predictions.loc[
            predictions["Overall_Rank"].idxmin(),
            "District"
        ]
    )

    col3.metric(
        "Top Overall Rank",
        int(predictions["Overall_Rank"].min())
    )

    st.markdown("---")

    st.subheader("2025 District Rankings")

    display_columns = [
        "District",
        "Predicted_Average_Growth_%",
        "Predicted_Median_Growth_%",
        "Average_Growth_Rank",
        "Median_Growth_Rank",
        "Combined_Rank",
        "Overall_Rank",
    ]

    ranking_table = (
        predictions[display_columns]
        .sort_values("Overall_Rank")
        .reset_index(drop=True)
    )

    ranking_table.columns = [
        "District",
        "Predicted Average Growth",
        "Predicted Median Growth",
        "Average Growth Rank",
        "Median Growth Rank",
        "Combined Rank",
        "Overall Rank",
    ]

    ranking_table["Predicted Average Growth"] = (
        ranking_table["Predicted Average Growth"]
        .map(lambda x: f"{x:.1f}%")
    )

    ranking_table["Predicted Median Growth"] = (
        ranking_table["Predicted Median Growth"]
        .map(lambda x: f"{x:.1f}%")
    )

    st.dataframe(
        ranking_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

st.subheader("🔎 Explore a District's 2025 Forecast")

selected_district = st.selectbox(
    "Select a District",
    predictions["District"].sort_values().tolist()
)

selected_row = predictions[
    predictions["District"] == selected_district
].iloc[0]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Overall Rank",
    f"#{int(selected_row['Overall_Rank'])}"
)

col2.metric(
    "Predicted Avg Growth",
    f"{selected_row['Predicted_Average_Growth_%']:.2f}%"
)

col3.metric(
    "Predicted Median Growth",
    f"{selected_row['Predicted_Median_Growth_%']:.2f}%"
)

col4.metric(
    "Average Growth Rank",
    f"#{int(selected_row['Average_Growth_Rank'])}"
)

col5.metric(
    "Median Growth Rank",
    f"#{int(selected_row['Median_Growth_Rank'])}"
)


st.markdown("---")

st.subheader("📊 Predicted 2025 Growth by District")

chart_data = (
        predictions[
            [
                "District",
                "Predicted_Average_Growth_%",
                "Predicted_Median_Growth_%"
            ]
        ]
        .sort_values(
            "Predicted_Average_Growth_%",
            ascending=False
        )
    )

st.bar_chart(
        chart_data.set_index("District")
    )
st.markdown("---")

st.markdown("---")

st.subheader("🛡️ Sensitivity Analysis")

st.markdown(
        "Sensitivity analysis shows how the 2025 model predictions "
        "respond to changes in key input assumptions."
    )

    # --------------------------------------------------------
    # London-wide sensitivity
    # --------------------------------------------------------

st.markdown("### 🌍 London-wide Sensitivity")

sensitivity_types = sorted(
        sensitivity["Sensitivity_Type"].unique()
    )

selected_sensitivity = st.selectbox(
        "Sensitivity Type",
        sensitivity_types,
        key="london_sensitivity_type"
    )

filtered_sensitivity = sensitivity[
        sensitivity["Sensitivity_Type"] == selected_sensitivity
    ].copy()

scenarios = sorted(
        filtered_sensitivity["Scenario"].unique(),
        key=lambda x: float(x.replace("%", ""))
    )

selected_scenario = st.selectbox(
        "Scenario",
        scenarios,
        key="london_scenario"
    )

scenario_data = filtered_sensitivity[
        filtered_sensitivity["Scenario"] == selected_scenario
    ].copy()

    # London-wide average impact
london_avg_change = (
        scenario_data["Average_Growth_Change"].mean() * 100
    )

london_median_change = (
        scenario_data["Median_Growth_Change"].mean() * 100
    )

col1, col2 = st.columns(2)

col1.metric(
        "Average Growth Change",
        f"{london_avg_change:.2f}%"
    )

col2.metric(
        "Median Growth Change",
        f"{london_median_change:.2f}%"
    )

scenario_chart = (
        filtered_sensitivity
        .groupby("Scenario", as_index=False)[
            [
                "Average_Growth_Change",
                "Median_Growth_Change"
            ]
        ]
        .mean()
    )

scenario_chart["Scenario_Value"] = (
        scenario_chart["Scenario"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )

scenario_chart = (
        scenario_chart
        .sort_values("Scenario_Value")
        .drop(columns="Scenario_Value")
        .set_index("Scenario")
    )

scenario_chart = scenario_chart.rename(
        columns={
            "Average_Growth_Change": "Average Growth Change",
            "Median_Growth_Change": "Median Growth Change"
        }
    )

scenario_chart = scenario_chart * 100

st.line_chart(
        scenario_chart
    )

    # --------------------------------------------------------
    # District-specific sensitivity
    # --------------------------------------------------------

st.markdown("---")

st.markdown("### 🔍 Explore a District")

district_options = sorted(
        filtered_sensitivity["District"].unique()
    )

selected_district = st.selectbox(
        "Select a District",
        district_options,
        key="sensitivity_district"
    )

district_sensitivity = filtered_sensitivity[
        filtered_sensitivity["District"] == selected_district
    ].copy()

district_sensitivity = (
        district_sensitivity
        .sort_values(
            "Shock"
        )
    )

st.markdown(
        f"**Sensitivity profile for {selected_district}**"
    )

district_chart = district_sensitivity[
        [
            "Scenario",
            "Average_Growth_Change",
            "Median_Growth_Change"
        ]
    ].copy()

district_chart = district_chart.rename(
        columns={
            "Average_Growth_Change": "Average Growth Change",
            "Median_Growth_Change": "Median Growth Change"
        }
    )

district_chart = district_chart.set_index(
        "Scenario"
    ) * 100

st.line_chart(
        district_chart
    )

district_display = district_sensitivity[
        [
            "Scenario",
            "Predicted_Average_Price_Growth",
            "Predicted_Median_Price_Growth",
            "Average_Growth_Change",
            "Median_Growth_Change"
        ]
    ].copy()

district_display.columns = [
        "Scenario",
        "Predicted Average Growth",
        "Predicted Median Growth",
        "Average Growth Change",
        "Median Growth Change"
    ]

for column in [
        "Predicted Average Growth",
        "Predicted Median Growth",
        "Average Growth Change",
        "Median Growth Change",
    ]:
        district_display[column] = (
            district_display[column] * 100
        ).map(lambda x: f"{x:.2f}%")

st.dataframe(
        district_display,
        use_container_width=True,
        hide_index=True
    )