import flask
from flask import flask, remender_template, request
import pickle
import numpy as np
import sklearn
from flask_ngrok import run_with_ngrok
import warnings
warnings.filterwarnings('ignore')
app=Flask(__name__)
run_with_ngrok(app)
model=pickle.load(open('lr.pkl','rb')
@app.route('/',methods=[GET])
def home():
    return render_template('index.html')
@app.route('/',methods=['GET',"POST"])
def predict():
    inpuy_values=[float(x) for x in request.form.values()]
    input_features=[input_values]
    input(input_features)
    prediction=model.predict(input_features)
    if prediction==1:
        return render_template('index.html',prediction_text='Eligible to Chance of Admit)
    else:
        return render_template('thyroid.html',prediction_text='Not eligible to Chance of Admit ')

