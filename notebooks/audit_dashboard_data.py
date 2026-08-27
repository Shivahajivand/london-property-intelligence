import pandas as pd

file_path = r"data/processed/london_property_final_predictive_features_targets.parquet"

df = pd.read_parquet(file_path)

print("\n" + "=" * 80)
print("FILE AUDIT")
print("=" * 80)

print("\nShape:")
print(df.shape)

print("\nColumns:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
missing = df.isna().sum()
print(missing[missing > 0].sort_values(ascending=False))

print("\nUnique Years:")
if "Year" in df.columns:
    print(sorted(df["Year"].dropna().unique()))
else:
    print("No column named 'Year' found.")

print("\nUnique District/Borough Counts:")

for col in ["Borough", "Borough_Name", "District", "borough", "borough_name"]:
    if col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")

print("\nFirst 5 Rows:")
print(df.head().to_string())

print("\n" + "=" * 80)
print("END OF AUDIT")
print("=" * 80)

print("\n" + "=" * 80)
print("FINAL OUTPUTS AUDIT")
print("=" * 80)

files = [
    r"notebooks/final_outputs/London_Housing_2025_Final_Predictions.csv",
    r"notebooks/final_outputs/London_Housing_2025_Final_Results.xlsx",
    r"notebooks/final_outputs/London_Housing_2025_Sensitivity_Analysis.csv",
]

for path in files:
    print("\n" + "-" * 80)
    print(f"FILE: {path}")
    print("-" * 80)

    if path.endswith(".xlsx"):
        xls = pd.ExcelFile(path)
        print("Sheets:")
        print(xls.sheet_names)

        for sheet in xls.sheet_names:
            temp = pd.read_excel(path, sheet_name=sheet)
            print(f"\nSheet: {sheet}")
            print("Shape:", temp.shape)
            print("Columns:")
            for i, col in enumerate(temp.columns, 1):
                print(f"{i}. {col}")

            print("\nFirst 5 rows:")
            print(temp.head())

    else:
        temp = pd.read_csv(path)

        print("Shape:", temp.shape)

        print("\nColumns:")
        for i, col in enumerate(temp.columns, 1):
            print(f"{i}. {col}")

        print("\nData Types:")
        print(temp.dtypes)

        print("\nMissing Values:")
        print(temp.isna().sum()[temp.isna().sum() > 0])

        print("\nFirst 5 rows:")
        print(temp.head())

print("\n" + "=" * 80)
print("END OF FINAL OUTPUTS AUDIT")
print("=" * 80)