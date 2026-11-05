
import pandas as pd
from pathlib import Path

# Locate dataset
project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "dataset" / "student_scores.csv"

# Load data
df = pd.read_csv(file_path)

# 1. Missing values
print("Missing Values:")
print(df.isnull().sum())

# 2. Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 3. Data types
print("\nData Types:")
print(df.dtypes)

# 4. Validate ranges
ranges = {
    "study_hours": (0.5, 10),
    "attendance": (40, 100),
    "previous_score": (30, 100),
    "sleep_hours": (4, 10),
    "exam_score": (0, 100)
}

print("\nInvalid Values:")

for column, (low, high) in ranges.items():
    invalid = (~df[column].between(low, high)).sum()
    print(column, ":", invalid)

# 5. Remove duplicates if present
df = df.drop_duplicates()

# 6. Save cleaned dataset
output_path = project_root / "dataset" / "student_scores_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nData cleaning completed!")
print("Final dataset shape:", df.shape)
