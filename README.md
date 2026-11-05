# 🎓 Student Score Predictor

> A Python desktop application that predicts student exam scores with a trained **Linear Regression** model and a **Tkinter** interface.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Model-Linear%20Regression-6C63FF?style=for-the-badge)
![GUI](https://img.shields.io/badge/Interface-Tkinter-2563EB?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Individual Prediction** | Predict an exam score from study hours, attendance, previous score, and sleep hours |
| 📄 **CSV Import** | Load a CSV file containing multiple student records |
| 📊 **Batch Prediction** | Generate predictions for imported records |
| 💾 **CSV Export** | Save batch prediction results to a CSV file |
| 📈 **Charts** | View the predicted score and the study-hours regression trend |
| 💡 **Suggestions** | Display simple study and attendance suggestions based on entered values |

---

## 🏗️ Project Structure

```
Student_Score_Predictor/
├── app.py                         # Tkinter desktop application
├── check_environment.py           # Environment check helper
├── requirements.txt               # Python dependencies
├── .gitignore
├── dataset/
│   ├── student_scores.csv         # Synthetic dataset
│   └── student_scores_cleaned.csv # Cleaned synthetic dataset
├── models/
│   └── student_score_model.pkl    # Saved trained model
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_model_training.ipynb
└── src/
    ├── data_preprocessing.py
    ├── eda.py
    ├── explore_dataset.py
    ├── generate_dataset.py
    ├── predict.py
    ├── prepare_data.py
    └── train_model.py
```

---

## 🔄 How It Works

```text
Student inputs or CSV records
          │
          ▼
Input validation and feature ordering
          │
          ▼
Saved Linear Regression model
          │
          ▼
Predicted exam score
          │
          ├── Charts and suggestions in the desktop app
          └── Batch results exported to CSV
```

The model uses `study_hours`, `attendance`, `previous_score`, and `sleep_hours` as input features and predicts `exam_score`.

---

## 📊 Model Evaluation

Reported results on the **synthetic dataset**:

| Metric | Result |
|---|---:|
| MAE | 4.01 |
| RMSE | 5.05 |
| R² | 0.8539 |

These scores describe performance on the synthetic data and should not be treated as evidence of accuracy for real students.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/faiyaz2709/Student_Score_Predictor.git
cd Student_Score_Predictor
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The app loads the saved model from `models/student_score_model.pkl`. Tkinter is included with most standard Windows Python installations.

---

## 📄 CSV Input Format

CSV files for batch prediction must include these four input columns. Additional columns are retained in the exported results.

```csv
study_hours,attendance,previous_score,sleep_hours
7.5,85,75,7
5,72,64,6.5
```

The application validates input values before generating predictions.

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Desktop interface | Tkinter |
| Data handling | Pandas, NumPy |
| Machine learning | Scikit-learn, Linear Regression |
| Charts | Matplotlib |
| Model storage | Joblib |

---

## ⚠️ Dataset Note

The included dataset is synthetic and does not contain real student records. This project is for learning and demonstration; predictions should not be used to make decisions about real students.

---

## 📄 License

No license file is included yet. Add a license if you want to specify how others may use or distribute this project.


## Live web application

The Streamlit version uses the existing trained model and the same four features as the desktop app: study hours, attendance, previous score, and sleep hours.

### Run locally

Install the project dependencies and start the web app:

```powershell
python -m pip install -r requirements.txt
streamlit run web_app.py
```

### Deploy on Streamlit Community Cloud

1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
2. Choose **Create app**, select this repository and the `main` branch, and set the app file path to `web_app.py`.
3. Deploy. No secrets are required. The repository must include `models/student_score_model.pkl`.

The live app URL can be added here after deployment succeeds.

## Build the Windows desktop application

Build on Windows from the repository root. The existing Tkinter source and trained model are required.

```powershell
python -m pip install -r requirements.txt
python -m pip install pyinstaller
python -m PyInstaller --clean --onefile --windowed --name StudentScorePredictor --add-data "models/student_score_model.pkl;models" app.py
```

The executable is written to `dist\StudentScorePredictor.exe`. Test it on a Windows computer without the development environment before sharing it. A GitHub Release can be created to distribute the executable; no release is created by this README update.

## Dataset limitation

The model was trained and evaluated using synthetic data. Its reported metrics do not establish accuracy for real students. This demonstration should not be used to make decisions about real students.
