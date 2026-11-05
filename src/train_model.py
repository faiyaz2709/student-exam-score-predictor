import joblib
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Locate project directory
project_root = Path(__file__).resolve().parent.parent

# 2. Load cleaned dataset
file_path = project_root / "dataset" / "student_scores_cleaned.csv"

df = pd.read_csv(file_path)

# 3. Select features (X)
X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "sleep_hours"
    ]
]

# 4. Select target (y)
y = df["exam_score"]

# 5. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 6. Create Linear Regression model
model = LinearRegression()

# 7. Train the model
model.fit(X_train, y_train)

# 8. Display model information
print("MODEL TRAINED SUCCESSFULLY!")

print("\nIntercept:")
print(model.intercept_)

print("\nCoefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", coefficient)

# 9. Predict testing data
predictions = model.predict(X_test)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np

# 1. Calculate MAE
mae = mean_absolute_error(y_test, predictions)

# 2. Calculate MSE
mse = mean_squared_error(y_test, predictions)

# 3. Calculate RMSE
rmse = np.sqrt(mse)

# 4. Calculate R2 Score
r2 = r2_score(y_test, predictions)

# Display evaluation results
print("\n========== MODEL EVALUATION ==========")

print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

print("======================================")

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.scatter(y_test, predictions, alpha=0.7)

plt.plot(
    [0, 100],
    [0, 100],
    linestyle="--"
)

plt.xlabel("Actual Exam Scores")
plt.ylabel("Predicted Exam Scores")

plt.title("Actual vs Predicted Exam Scores")

plt.show()


print("\nFirst 10 Predictions:")
print(predictions[:10])

print("\nFirst 10 Actual Scores:")
print(y_test.iloc[:10].values)


# SAVE THE TRAINED MODEL

model_path = project_root / "models" / "student_score_model.pkl"

joblib.dump(
    {
        "model": model,
        "features": list(X.columns)
    },
    model_path
)

print("\nMODEL SAVED SUCCESSFULLY!")
print("Saved at:", model_path)