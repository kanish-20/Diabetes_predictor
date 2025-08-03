# Diabetes Prediction using Flask & Decision Tree

This is a simple web application that predicts whether a person is diabetic based on input health metrics like Glucose, BMI, Insulin, and Age. The backend is powered by a Decision Tree Classifier and the frontend is built using HTML and styled with CSS.

---

## Features

- Predict diabetes based on 4 key medical inputs
- Built with Python, Flask, and Scikit-learn
- Simple and clean user interface
- Model trained on PIMA Indians Diabetes dataset

---

##  Input Fields

| Field     | Description               |
|-----------|---------------------------|
| Glucose   | Plasma glucose concentration |
| BMI       | Body Mass Index (weight/height²) |
| Insulin   | 2-Hour serum insulin (mu U/ml) |
| Age       | Age of the person          |

---

## 📁 Project Structure

diabetes-prediction-flask/
├── app.py
├── train_model.py
├── diabetes.csv
├── decision_tree_diabetes_model.pkl
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md

---
## How It Works

The app uses a Decision Tree Classifier trained on real-world data from diabetes.csv

When a user submits their Glucose, BMI, Insulin, and Age:

The model predicts whether the person is Diabetic or Not Diabetic

The app displays the prediction result instantly on the same page

---

## 🛠 How to Run Locally

1. Clone the repository:

```
git clone https://github.com/kanish-20/diabetes-prediction-flask.git
cd diabetes-prediction-flask
```

2.Install the requirements:

```
pip install -r requirements.txt
```

3.train the model(Optional):

```
python train_model.py
```

---
## Running the application

Start the Flask development server:
```
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```
---

## Step-by-step :

![WhatsApp Image 2025-08-03 at 23 51 21](https://github.com/user-attachments/assets/176b1317-3d8c-417f-896a-caf472162639)
![WhatsApp Image 2025-08-03 at 23 51 21 (1)](https://github.com/user-attachments/assets/8179145e-b59e-4990-94ee-9d857ca425e9)
![WhatsApp Image 2025-08-03 at 23 51 21 (2)](https://github.com/user-attachments/assets/18479e23-2c2c-4abc-b42d-e81e37901b19)




