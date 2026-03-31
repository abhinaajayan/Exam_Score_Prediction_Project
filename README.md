# Exam Score Prediction Web App

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/flask-1.1%2B-green.svg)
![Status](https://img.shields.io/badge/status-ready-success.svg)

## 🚀 Project Overview

`exam_score_pred` is a simple Flask web app that predicts student exam scores using a trained machine learning model.  
The app accepts personal and study lifestyle inputs and returns a predicted exam score.

- Front-end: `templates/index.html`
- Back-end: `app.py`
- Model artifacts: `model.pkl`, `scaler.pkl`, `encoders.pkl`
- Dataset (original): `Exam_Score_Prediction.csv`

---

## 🧠 Key Features

- Accepts inputs:
  - age, gender, course
  - study hours, attendance
  - internet access, sleep hours, sleep quality
  - study method, facility rating, exam difficulty
- Uses preprocessing encoders + scaler + trained model
- Displays prediction on the same form
- Error handling with user-friendly message

---

## 📦 Requirements

- Python 3.8+
- pip packages:
  - Flask
  - numpy
  - scikit-learn
  - joblib
  - pickle (Stdlib)

---

## ⚙️ Install & Run

```bash
# 1) Clone
git clone https://github.com/your-username/exam_score_pred.git
cd exam_score_pred

# 2) Virtual env (recommended)
python -m venv venv
# Windows:
venv\\Scripts\\activate
# macOS/Linux:
source venv/bin/activate

# 3) Install deps
pip install Flask numpy scikit-learn joblib

# 4) Run
python app.py