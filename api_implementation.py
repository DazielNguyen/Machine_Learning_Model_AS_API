import json
import requests
url = 'http://[take from uvicorn]]/diabetes_prediction'
input_data = {
    "Pregnancies": 1,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,    
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 31
}
input_json = json.dumps(input_data)
response = requests.post(url, data=input_json)
print(response.text)

