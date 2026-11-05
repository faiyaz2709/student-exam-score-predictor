
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "dataset" / "student_scores.csv"

df = pd.read_csv(file_path)

# 1. First five records
print("\nFIRST 5 RECORDS")
print(df.head())

# 2. Dataset dimensions
print("\nDATASET SHAPE")
print(df.shape)

# 3. Column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# 4. Dataset information
print("\nDATASET INFORMATION")
df.info()

# 5. Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 6. Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())
