
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

import joblib
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =====================================================
# 1. LOAD TRAINED MACHINE LEARNING MODEL
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent

MODEL_PATH = PROJECT_ROOT / "models" / "student_score_model.pkl"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
features = saved_data["features"]

print("ML Model Loaded Successfully!")


# =====================================================
# 2. APPLICATION CONFIGURATION
# =====================================================

root = tk.Tk()

root.title("Student Score Predictor")
root.geometry("1250x900")
root.minsize(1000, 750)
root.configure(bg="#F4F7FC")

BG = "#F4F7FC"
WHITE = "#FFFFFF"
BLUE = "#2563EB"
DARK = "#1E293B"
GREY = "#64748B"
BORDER = "#E2E8F0"

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Modern.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=11,
    background=BLUE,
    foreground=WHITE
)

style.map(
    "Modern.TButton",
    background=[("active", "#1D4ED8")]
)


# =====================================================
# 3. HEADER
# =====================================================

header = tk.Frame(root, bg=WHITE, height=75)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="Student Score Predictor",
    font=("Segoe UI", 22, "bold"),
    fg=BLUE,
    bg=WHITE
).pack(side="left", padx=30, pady=15)

tk.Label(
    header,
    text="MACHINE LEARNING DASHBOARD",
    font=("Segoe UI", 9, "bold"),
    fg=GREY,
    bg=WHITE
).pack(side="right", padx=30)


# =====================================================
# 4. SCROLLABLE MAIN WINDOW
# =====================================================

outer = tk.Frame(root, bg=BG)
outer.pack(fill="both", expand=True)

page_canvas = tk.Canvas(
    outer,
    bg=BG,
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    outer,
    orient="vertical",
    command=page_canvas.yview
)

page_canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
page_canvas.pack(side="left", fill="both", expand=True)

main = tk.Frame(page_canvas, bg=BG)

window_id = page_canvas.create_window(
    (0, 0),
    window=main,
    anchor="nw"
)


def update_scroll(event):
    page_canvas.configure(
        scrollregion=page_canvas.bbox("all")
    )


def resize_main(event):
    page_canvas.itemconfigure(
        window_id,
        width=event.width
    )


main.bind("<Configure>", update_scroll)
page_canvas.bind("<Configure>", resize_main)


# =====================================================
# 5. PAGE TITLE
# =====================================================

tk.Label(
    main,
    text="Student Performance Analysis",
    font=("Segoe UI", 21, "bold"),
    fg=DARK,
    bg=BG
).pack(anchor="w", padx=30, pady=(25, 5))

tk.Label(
    main,
    text="Enter academic details to predict exam performance.",
    font=("Segoe UI", 11),
    fg=GREY,
    bg=BG
).pack(anchor="w", padx=30, pady=(0, 20))


# =====================================================
# 6. STUDENT INPUT CARD
# =====================================================

input_card = tk.Frame(
    main,
    bg=WHITE,
    padx=25,
    pady=20,
    highlightbackground=BORDER,
    highlightthickness=1
)

input_card.pack(fill="x", padx=30)

tk.Label(
    input_card,
    text="Student Information",
    font=("Segoe UI", 16, "bold"),
    fg=DARK,
    bg=WHITE
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 15)
)


# Input variables

study_var = tk.DoubleVar(value=6.0)
attendance_var = tk.DoubleVar(value=85.0)
previous_var = tk.DoubleVar(value=75.0)
sleep_var = tk.DoubleVar(value=7.0)


def create_input(parent, label, variable, row, column, minimum, maximum):

    frame = tk.Frame(parent, bg=WHITE)

    frame.grid(
        row=row,
        column=column,
        sticky="ew",
        padx=15,
        pady=10
    )

    tk.Label(
        frame,
        text=label,
        font=("Segoe UI", 10, "bold"),
        fg=DARK,
        bg=WHITE
    ).pack(anchor="w", pady=(0, 7))

    ttk.Spinbox(
        frame,
        from_=minimum,
        to=maximum,
        increment=0.5,
        textvariable=variable,
        font=("Segoe UI", 12),
        width=25
    ).pack(fill="x")


create_input(
    input_card,
    "Daily Study Hours (0.5–10)",
    study_var, 1, 0, 0.5, 10
)

create_input(
    input_card,
    "Attendance (%)",
    attendance_var, 1, 1, 40, 100
)

create_input(
    input_card,
    "Previous Exam Score",
    previous_var, 2, 0, 30, 100
)

create_input(
    input_card,
    "Daily Sleep Hours (4–10)",
    sleep_var, 2, 1, 4, 10
)

input_card.grid_columnconfigure(0, weight=1)
input_card.grid_columnconfigure(1, weight=1)


# =====================================================
# 7. RESULT CARD
# =====================================================

result_card = tk.Frame(
    main,
    bg=WHITE,
    padx=20,
    pady=15,
    highlightbackground=BORDER,
    highlightthickness=1
)

result_card.pack(fill="x", padx=30, pady=15)

tk.Label(
    result_card,
    text="PREDICTED EXAM SCORE",
    font=("Segoe UI", 10, "bold"),
    fg=GREY,
    bg=WHITE
).pack()

result_label = tk.Label(
    result_card,
    text="-- / 100",
    font=("Segoe UI", 34, "bold"),
    fg=BLUE,
    bg=WHITE
)

result_label.pack(pady=5)


# =====================================================
# 8. ANALYTICS CHART CARD
# =====================================================

chart_card = tk.Frame(
    main,
    bg=WHITE,
    padx=15,
    pady=15,
    highlightbackground=BORDER,
    highlightthickness=1
)

chart_card.pack(fill="x", padx=30, pady=10)

tk.Label(
    chart_card,
    text="Performance Analytics",
    font=("Segoe UI", 16, "bold"),
    fg=DARK,
    bg=WHITE
).pack(anchor="w", padx=10, pady=10)


# Only TWO charts

fig, axes = plt.subplots(
    1, 2,
    figsize=(10, 4)
)

fig.patch.set_facecolor(WHITE)

for ax in axes:
    ax.set_facecolor(WHITE)

fig.tight_layout(pad=3)

chart_canvas = FigureCanvasTkAgg(
    fig,
    master=chart_card
)

chart_canvas.draw()

chart_canvas.get_tk_widget().pack(
    fill="both",
    expand=True
)


# =====================================================
# 9. IMPROVEMENT SUGGESTIONS
# =====================================================

suggestion_card = tk.Frame(
    main,
    bg=WHITE,
    padx=20,
    pady=20,
    highlightbackground=BORDER,
    highlightthickness=1
)

suggestion_card.pack(fill="x", padx=30, pady=15)

tk.Label(
    suggestion_card,
    text="Improvement Suggestions",
    font=("Segoe UI", 16, "bold"),
    fg=DARK,
    bg=WHITE
).pack(anchor="w", pady=(0, 10))

suggestion_label = tk.Label(
    suggestion_card,
    text="Suggestions will appear after prediction.",
    font=("Segoe UI", 11),
    fg=GREY,
    bg=WHITE,
    justify="left",
    anchor="w",
    wraplength=1000
)

suggestion_label.pack(fill="x")


# =====================================================
# 10. CSV RESULTS TABLE
# =====================================================

table_card = tk.Frame(
    main,
    bg=WHITE,
    padx=15,
    pady=15,
    highlightbackground=BORDER,
    highlightthickness=1
)

table_card.pack(fill="x", padx=30, pady=15)

tk.Label(
    table_card,
    text="CSV Prediction Results",
    font=("Segoe UI", 15, "bold"),
    fg=DARK,
    bg=WHITE
).pack(anchor="w", padx=10, pady=10)

table_frame = tk.Frame(table_card, bg=WHITE)
table_frame.pack(fill="x", padx=5)

tree = ttk.Treeview(
    table_frame,
    columns=features + ["predicted_score"],
    show="headings",
    height=6
)

for column in features:

    tree.heading(
        column,
        text=column.replace("_", " ").title()
    )

    tree.column(
        column,
        width=130,
        anchor="center"
    )

tree.heading(
    "predicted_score",
    text="Predicted Score"
)

tree.column(
    "predicted_score",
    width=140,
    anchor="center"
)

tree_scroll = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=tree_scroll.set
)

tree.pack(side="left", fill="x", expand=True)
tree_scroll.pack(side="right", fill="y")


# =====================================================
# 11. CSV VARIABLES
# =====================================================

imported_df = None
prediction_df = None


# =====================================================
# 12. INPUT VALIDATION
# =====================================================

def validate_student(row):

    limits = {
        "study_hours": (0.5, 10),
        "attendance": (40, 100),
        "previous_score": (30, 100),
        "sleep_hours": (4, 10)
    }

    for feature, (low, high) in limits.items():

        value = float(row[feature])

        if not np.isfinite(value):
            raise ValueError(
                f"{feature} must be a valid number."
            )

        if not low <= value <= high:
            raise ValueError(
                f"{feature} must be between {low} and {high}."
            )


# =====================================================
# 13. DRAW TWO ANALYTICS CHARTS
# =====================================================

def draw_charts(
    prediction,
    study_hours,
    attendance,
    previous_score,
    sleep_hours
):

    # Chart 1: Circular Score

    axes[0].clear()

    axes[0].pie(
        [prediction, 100 - prediction],
        labels=["Score", "Remaining"],
        startangle=90,
        counterclock=False,
        autopct="%1.1f%%",
        wedgeprops={"width": 0.35}
    )

    axes[0].set_title(
        "Predicted Exam Score",
        fontsize=12,
        fontweight="bold"
    )

    # Chart 2: Linear Regression

    axes[1].clear()

    study_range = np.linspace(0.5, 10, 100)

    trend_data = pd.DataFrame({
        "study_hours": study_range,
        "attendance": attendance,
        "previous_score": previous_score,
        "sleep_hours": sleep_hours
    })

    # Match model's original feature order

    trend_data = trend_data[features]

    trend_predictions = model.predict(trend_data)

    axes[1].plot(
        study_range,
        trend_predictions,
        linewidth=2,
        label="Regression Trend"
    )

    axes[1].scatter(
        study_hours,
        prediction,
        s=70,
        label="Current Student"
    )

    axes[1].set_title(
        "Study Hours vs Predicted Score",
        fontsize=12,
        fontweight="bold"
    )

    axes[1].set_xlabel("Study Hours")
    axes[1].set_ylabel("Predicted Score")

    axes[1].legend(fontsize=8)
    axes[1].grid(alpha=0.2)

    fig.tight_layout(pad=3)

    chart_canvas.draw()


# =====================================================
# 14. IMPROVEMENT SUGGESTIONS
# =====================================================

def show_suggestions(
    study,
    attendance,
    previous,
    sleep
):

    suggestions = []

    if study < 5:
        suggestions.append(
            "• Increase consistent study time gradually."
        )

    if attendance < 75:
        suggestions.append(
            "• Improve class attendance and participation."
        )

    if previous < 60:
        suggestions.append(
            "• Revise weak subjects and practise previous papers."
        )

    if sleep < 6:
        suggestions.append(
            "• Maintain a consistent and healthy sleep schedule."
        )

    if not suggestions:
        suggestions.append(
            "• Maintain your current academic routine."
        )

    suggestions.append(
        "• Practise mock tests and analyse your mistakes."
    )

    suggestion_label.config(
        text="\n".join(suggestions)
    )


# =====================================================
# 15. MANUAL STUDENT PREDICTION
# =====================================================

def predict_score():

    try:

        row = {
            "study_hours": study_var.get(),
            "attendance": attendance_var.get(),
            "previous_score": previous_var.get(),
            "sleep_hours": sleep_var.get()
        }

        validate_student(row)

        student_data = pd.DataFrame(
            [[row[feature] for feature in features]],
            columns=features
        )

        prediction = float(
            model.predict(student_data)[0]
        )

        prediction = float(
            np.clip(prediction, 0, 100)
        )

        # Display numerical score only

        result_label.config(
            text=f"{prediction:.2f} / 100"
        )

        draw_charts(
            prediction,
            row["study_hours"],
            row["attendance"],
            row["previous_score"],
            row["sleep_hours"]
        )

        show_suggestions(
            row["study_hours"],
            row["attendance"],
            row["previous_score"],
            row["sleep_hours"]
        )

    except (ValueError, TypeError) as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )

    except Exception as error:

        messagebox.showerror(
            "Prediction Error",
            str(error)
        )


# =====================================================
# 16. IMPORT CSV
# =====================================================

def import_csv():

    global imported_df, prediction_df

    file_path = filedialog.askopenfilename(
        title="Select Student CSV File",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:

        df = pd.read_csv(file_path)

        missing_columns = [
            feature for feature in features
            if feature not in df.columns
        ]

        if missing_columns:

            raise ValueError(
                "Missing columns: "
                + ", ".join(missing_columns)
            )

        if df.empty:
            raise ValueError(
                "CSV file contains no records."
            )

        for feature in features:

            df[feature] = pd.to_numeric(
                df[feature],
                errors="coerce"
            )

        if df[features].isnull().any().any():

            raise ValueError(
                "CSV contains missing or non-numeric values."
            )

        if not np.isfinite(
            df[features].to_numpy(dtype=float)
        ).all():

            raise ValueError(
                "CSV contains infinite or invalid values."
            )

        for index, row in df.iterrows():

            try:
                validate_student(row)

            except ValueError as error:

                raise ValueError(
                    f"CSV row {index + 2}: {error}"
                )

        imported_df = df.copy()
        prediction_df = None

        for item in tree.get_children():
            tree.delete(item)

        for _, row in df.head(100).iterrows():

            tree.insert(
                "",
                "end",
                values=[
                    row[feature] for feature in features
                ] + ["Pending"]
            )

        status_label.config(
            text=f"Imported {len(df)} student records."
        )

        messagebox.showinfo(
            "CSV Import",
            f"{len(df)} records imported successfully."
        )

    except Exception as error:

        messagebox.showerror(
            "CSV Import Error",
            str(error)
        )


# =====================================================
# 17. PREDICT ALL CSV STUDENTS
# =====================================================

def predict_csv():

    global prediction_df

    if imported_df is None:

        messagebox.showwarning(
            "No CSV",
            "Please import a CSV file first."
        )

        return

    try:

        predictions = model.predict(
            imported_df[features]
        )

        result = imported_df.copy()

        result["predicted_score"] = np.clip(
            predictions,
            0,
            100
        ).round(2)

        prediction_df = result

        for item in tree.get_children():
            tree.delete(item)

        for _, row in result.head(100).iterrows():

            tree.insert(
                "",
                "end",
                values=[
                    row[feature] for feature in features
                ] + [row["predicted_score"]]
            )

        status_label.config(
            text=f"Predictions completed for {len(result)} students."
        )

        messagebox.showinfo(
            "Prediction Complete",
            f"Predictions generated for {len(result)} students."
        )

    except Exception as error:

        messagebox.showerror(
            "Prediction Error",
            str(error)
        )


# =====================================================
# 18. EXPORT CSV RESULTS
# =====================================================

def export_csv():

    if prediction_df is None:

        messagebox.showwarning(
            "No Predictions",
            "Please predict CSV students before exporting."
        )

        return

    save_path = filedialog.asksaveasfilename(
        title="Save Prediction Results",
        defaultextension=".csv",
        initialfile="student_predictions.csv",
        filetypes=[
            ("CSV Files", "*.csv")
        ]
    )

    if not save_path:
        return

    try:

        prediction_df.to_csv(
            save_path,
            index=False
        )

        messagebox.showinfo(
            "Export Successful",
            "Prediction results saved successfully."
        )

    except Exception as error:

        messagebox.showerror(
            "Export Error",
            str(error)
        )


# =====================================================
# 19. BUTTONS DIRECTLY BELOW INPUT FIELDS
# =====================================================

button_frame = tk.Frame(main, bg=BG)

button_frame.pack(
    fill="x",
    padx=30,
    pady=15
)

ttk.Button(
    button_frame,
    text="PREDICT EXAM SCORE",
    style="Modern.TButton",
    command=predict_score
).pack(
    fill="x",
    pady=(0, 10)
)

csv_button_frame = tk.Frame(
    button_frame,
    bg=BG
)

csv_button_frame.pack(fill="x")

ttk.Button(
    csv_button_frame,
    text="IMPORT CSV",
    style="Modern.TButton",
    command=import_csv
).pack(side="left", padx=3, expand=True, fill="x")

ttk.Button(
    csv_button_frame,
    text="PREDICT CSV",
    style="Modern.TButton",
    command=predict_csv
).pack(side="left", padx=3, expand=True, fill="x")

ttk.Button(
    csv_button_frame,
    text="EXPORT RESULTS",
    style="Modern.TButton",
    command=export_csv
).pack(side="left", padx=3, expand=True, fill="x")


# =====================================================
# 20. STATUS LABEL
# =====================================================

status_label = tk.Label(
    main,
    text="Ready | Enter student details or import CSV.",
    font=("Segoe UI", 10),
    fg=GREY,
    bg=BG
)

status_label.pack(
    anchor="w",
    padx=35,
    pady=5
)


# =====================================================
# 21. FOOTER
# =====================================================

tk.Label(
    main,
    text="Student Score Predictor | Python | Tkinter | Scikit-learn",
    font=("Segoe UI", 9),
    fg=GREY,
    bg=BG
).pack(pady=20)


# =====================================================
# 22. START APPLICATION
# =====================================================

root.mainloop()
