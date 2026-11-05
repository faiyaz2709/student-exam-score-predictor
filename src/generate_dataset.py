
import numpy as np
import pandas as pd
from pathlib import Path

# 1. Initialize random generator
rng = np.random.default_rng(42)

# 2. Number of students
n = 1000

# 3. Generate student features
study_hours = rng.uniform(0.5, 10, n)
attendance = rng.uniform(40, 100, n)
previous_score = rng.uniform(30, 100, n)
sleep_hours = rng.uniform(4, 10, n)

# 4. Generate random noise
noise = rng.normal(0, 5, n)

# 5. Calculate exam scores
exam_score = (
    2
    + study_hours * 3.2
    + attendance * 0.12
    + previous_score * 0.35
    + sleep_hours * 1.0
    + noise
)

# 6. Restrict scores between 0 and 100
exam_score = np.clip(exam_score, 0, 100)

# 7. Create DataFrame
df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": previous_score,
    "sleep_hours": sleep_hours,
    "exam_score": exam_score
})

# 8. Round values
df = df.round(2)

# 9. Save CSV file
project_root = Path(__file__).resolve().parent.parent
output_path = project_root / "dataset" / "student_scores.csv"

df.to_csv(output_path, index=False)

# 10. Display results
print("Dataset generated successfully!")
print("Total students:", len(df))

print("\nFirst 5 records:")
print(df.head())

print("\nDataset saved at:", output_path)
