
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# 1. Locate project directory
project_root = Path(__file__).resolve().parent.parent

# 2. Load cleaned dataset
file_path = project_root / "dataset" / "student_scores_cleaned.csv"

df = pd.read_csv(file_path)

# 3. Select input features (X)
X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "sleep_hours"
    ]
]

# 4. Select target variable (y)
y = df["exam_score"]

# 5. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 6. Display results
print("FEATURE SELECTION")
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nTRAINING DATA")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTESTING DATA")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)

print("\nTRAIN-TEST SPLIT COMPLETED!")
