# app.py
from flask import Flask, request, render_template
import pickle
import numpy as np
import os
# Set the working directory to the location where your files are
os.chdir(r'C:\Users\thanay\Desktop\Online fraud detection')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model = pickle.load(open('model.pkl', 'rb'))
    # Get input values from the form
    step = 1
    type_ = request.form['type']
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = oldbalanceOrg - amount
    oldbalanceDest = float(request.form['oldbalanceDest'])
    newbalanceDest = oldbalanceDest + amount
    # Convert type to numerical value (you may need to adjust this mapping based on your encoding)
    type_dict = {'CASH_IN': 0, 'CASH_OUT': 1, 'TRANSFER': 2, 'DEBIT': 3, 'PAYMENT': 4}
    type_num = type_dict[type_.upper()]
    # Create the input array
    input_features = np.array([step, type_num, amount, newbalanceOrig, oldbalanceDest]).reshape(1, -1)
    # Make prediction
    prediction = model.predict(input_features)
    # Display prediction on the UI
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)














