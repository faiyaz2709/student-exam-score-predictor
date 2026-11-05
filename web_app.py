"""Streamlit interface for the Student Score Predictor."""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "student_score_model.pkl"
FEATURES = ["study_hours", "attendance", "previous_score", "sleep_hours"]


@st.cache_resource
def load_model(path: Path):
    saved = joblib.load(path)
    # The existing Tkinter app saves the estimator and ordered features together.
    if isinstance(saved, dict):
        model = saved.get("model")
        features = saved.get("features")
        if model is None or features is None:
            raise ValueError("Model bundle must contain 'model' and 'features'.")
        return model, list(features)
    return saved, list(getattr(saved, "feature_names_in_", FEATURES))


st.set_page_config(page_title="Student Score Predictor", page_icon="📘", layout="centered")
st.title("Student Score Predictor")
st.caption("Estimate an exam score from study habits and prior performance.")
st.warning(
    "Demonstration only. This model was trained and evaluated using synthetic data. "
    "Its predictions are not validated for real students and must not be used for educational decisions."
)

if not MODEL_PATH.is_file():
    st.error(f"Trained model not found at {MODEL_PATH.relative_to(ROOT)}. Add the existing model file there.")
    st.stop()

try:
    model, model_features = load_model(MODEL_PATH)
except Exception as exc:
    st.error(f"Could not load the trained model: {exc}")
    st.stop()

if list(model_features) != FEATURES:
    st.error(
        "The model feature names or order do not match the expected inputs: "
        + ", ".join(FEATURES)
        + ". Update the web app to match the model before deploying."
    )
    st.stop()

with st.form("prediction_form"):
    st.subheader("Student inputs")
    col1, col2 = st.columns(2)
    study_hours = col1.number_input("Daily study hours", min_value=0.5, max_value=10.0, value=6.0, step=0.5)
    attendance = col2.number_input("Attendance (%)", min_value=40.0, max_value=100.0, value=85.0, step=1.0)
    previous_score = col1.number_input("Previous exam score", min_value=30.0, max_value=100.0, value=75.0, step=1.0)
    sleep_hours = col2.number_input("Daily sleep hours", min_value=4.0, max_value=10.0, value=7.0, step=0.5)
    submitted = st.form_submit_button("Predict score", type="primary")

if submitted:
    row = pd.DataFrame([[study_hours, attendance, previous_score, sleep_hours]], columns=FEATURES)
    try:
        score = float(model.predict(row)[0])
        score = min(max(score, 0.0), 100.0)
        st.metric("Predicted exam score", f"{score:.1f} / 100")
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")

st.caption("Model inputs: study_hours, attendance, previous_score, sleep_hours.")
