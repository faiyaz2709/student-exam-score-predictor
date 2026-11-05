
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 1. Load dataset
project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "dataset" / "student_scores.csv"

df = pd.read_csv(file_path)

# 2. Correlation analysis
correlation = df.corr()

print("\nCORRELATION MATRIX")
print(correlation)

print("\nCORRELATION WITH EXAM SCORE")
print(correlation["exam_score"].sort_values(ascending=False))

# 3. Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="study_hours", y="exam_score")
plt.title("Study Hours vs Exam Score")
plt.show()

# 4. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="exam_score", bins=20, kde=True)
plt.title("Distribution of Exam Scores")
plt.show()

# 5. Heatmap
plt.figure(figsize=(9, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Student Performance Correlation Heatmap")
plt.show()
