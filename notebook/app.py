import numpy as np
import joblib
from flask import Flask, render_template, request
from flask import Flask
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the model
model = joblib.load('loan_status_predict')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = {
            'Gender': int(request.form['Gender']),
            'Married': int(request.form['Married']),
            'Dependents': int(request.form['Dependents']),
            'Education': int(request.form['Education']),
            'Self_Employed': int(request.form['Self_Employed']),
            'ApplicantIncome': float(request.form['ApplicantIncome']),
            'CoapplicantIncome': float(request.form['CoapplicantIncome']),
            'LoanAmount': float(request.form['LoanAmount']),
            'Loan_Amount_Term': int(request.form['Loan_Amount_Term']),
            'Credit_History': int(request.form['Credit_History']),
            'Property_Area': int(request.form['Property_Area'])
        }

        input_data = np.array(list(features.values())).reshape(1, -1)
        result = model.predict(input_data)

        if result == 1:
            prediction = "Loan Approved"
        else:
            prediction = "Loan Not Approved"

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555) 