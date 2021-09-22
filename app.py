from flask import Flask,request
import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger
from sklearn.linear_model import LogisticRegression    

app  =  Flask(__name__)
Swagger(app)

pickled_model = open("Pickle_file_iris.pkl","rb")
classifier  = pickle.load(pickled_model)

@app.route("/")
def home():
  return("Welcome to Iris classifier")

@app.route("/predict")
def predict_flower():
  """ Predict the Iris flower category
  ---
  parameters:
    - name: Petal_width
      in: query
      type: number
      required: true
    - name : Sepal_width
      in: query
      type: number
      required: true
    - name : Petal_length
      in: query
      type: number
      required: true
    - name : Sepal_length
      in: query
      type: number
      required: true
      
  responses:
    200:
      description: Result is
  """

  pw = request.args.get("Petal_width")
  sw = request.args.get("Sepal_width")
  pl = request.args.get("Petal_length")
  sl = request.args.get("Sepal_length")

  result = classifier.predict([[pw,sw,pl,sl]])
  return f"The prediction is{result}"

if __name__ == "__main__":
  app.run()