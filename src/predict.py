
import joblib
import pandas as pd
from pathlib import Path

# Locate project folder
project_root = Path(__file__).resolve().parent.parent

# Load saved model
model_path = project_root / "models" / "student_score_model.pkl"

saved_data = joblib.load(model_path)

model = saved_data["model"]
features = saved_data["features"]

print("STUDENT EXAM SCORE PREDICTOR")
print("----------------------------")

# Get student information
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous exam score: "))
sleep_hours = float(input("Enter sleep hours: "))

# Prepare input data
student_data = pd.DataFrame(
    [[study_hours, attendance, previous_score, sleep_hours]],
    columns=features
)

# Predict exam score
prediction = model.predict(student_data)

print("\nPredicted Exam Score:", round(prediction[0], 2))
