from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('decision_tree_diabetes_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get values from form
        features = [
            
            float(request.form['Glucose']),
            
            float(request.form['Insulin']),
            float(request.form['BMI']),
            
            float(request.form['Age'])
        ]
        pred = model.predict([features])[0]
        prediction = "DIABETIC" if pred == 1 else "NOT DIABETIC"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
