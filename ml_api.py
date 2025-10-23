from fastapi import FastAPI
from pydantic import BaseModel
import json
import joblib
app = FastAPI()

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

# Load the model diabetes_model
diabetes_model = joblib.load("diabetes_model.sav")

@app.post('/diabetes_prediction')
def diabetes_prediction(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    Pregnancies = input_dictionary['Pregnancies']
    Glucose = input_dictionary['Glucose']
    BloodPressure = input_dictionary['BloodPressure']
    SkinThickness = input_dictionary['SkinThickness']
    Insulin = input_dictionary['Insulin']
    BMI = input_dictionary['BMI']
    DiabetesPedigreeFunction = input_dictionary['DiabetesPedigreeFunction']
    Age = input_dictionary['Age']

    input_list = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    prediction = diabetes_model.predict([input_list])
    
    if (prediction[0] == 0):
        return {'The person is not diabetic'}
    else:
        return {'The person is diabetic'}
    