from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.statespace import sarimax
from datetime import datetime
import requests
from io import BytesIO
#!pip install urllib3
from collections.abc import Mapping

app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self):
        #budget = request.args.get('budget')
        
        # Let's load the package
        with open("test.pickle","rb") as f:
            SARIMAX_model = pickle.load(f)

        res = sarimax.SARIMAXResultsWrapper.load("test.pickle")
        pred_uc = res.get_forecast(steps = 36)
        prediction=pred_uc.predicted_mean
        
        
#         budget = [int(budget)]
#         df = pd.DataFrame(budget, columns=['Marketing Budget'])
#         model = pickle.load(open('simple_linear_regression.pkl', 'rb'))
        
#         prediction = model.predict(df)
          #prediction = int(prediction[0])
        return str(prediction)

#data api
# class getData(Resource):
#     def get(self):
#             df = pd.read_excel('data.xlsx')
#             df =  df.rename({'Marketing Budget': 'budget', 'Actual Sales': 'sale'}, axis=1)  # rename columns
#             #print(df.head())
#             #out = {'key':str}
#             res = df.to_json(orient='records')
#             #print( res)
#             return res

#
# api.add_resource(getData, '/api')
api.add_resource(prediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)