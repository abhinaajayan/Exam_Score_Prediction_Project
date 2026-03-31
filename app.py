from flask import Flask, render_template, request
import numpy as np
import joblib
import pickle

app = Flask(__name__)

# -------- LOAD FILES --------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# -------- HOME --------
@app.route("/")
def home():
    return render_template("index.html")

# -------- PREDICT --------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # -------- INPUT --------
        age = int(request.form["age"])
        gender = request.form["gender"]
        course = request.form["course"]
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        internet = request.form["internet"]
        sleep_hours = float(request.form["sleep_hours"])
        sleep_quality = request.form["sleep_quality"]
        study_method = request.form["study_method"]
        facility = request.form["facility"]
        difficulty = request.form["difficulty"]

        # -------- ENCODING --------
        gender = encoders["gender"].transform([gender])[0]
        course = encoders["course"].transform([course])[0]
        internet = encoders["internet_access"].transform([internet])[0]
        sleep_quality = encoders["sleep_quality"].transform([sleep_quality])[0]
        study_method = encoders["study_method"].transform([study_method])[0]
        facility = encoders["facility_rating"].transform([facility])[0]
        difficulty = encoders["exam_difficulty"].transform([difficulty])[0]

        # -------- FINAL ARRAY --------
        data = np.array([[age, gender, course, study_hours, attendance,
                          internet, sleep_hours, sleep_quality,
                          study_method, facility, difficulty]])

        # -------- SCALING --------
        data_scaled = scaler.transform(data)

        # -------- PREDICTION --------
        prediction = model.predict(data_scaled)[0]

        return render_template("index.html",
                               prediction_text=f"🎯 Predicted Score: {round(prediction, 2)}")

    except Exception as e:
        return render_template("index.html",
                               prediction_text=f"❌ Error: {str(e)}")

# -------- RUN --------
if __name__ == "__main__":
    app.run(debug=True)