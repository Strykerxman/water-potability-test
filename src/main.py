from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app = FastAPI(
    title='Water Potability Prediction',
    description='Predicting water potability'
)

with open(r'C:\Users\Martin\Desktop\MLOpsProj\model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.get('/')
def index():
    return 'Welcome to the Water Potability Prediction FastAPI!'

@app.post('/predict')
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph': [water.ph],
        'hardness': [water.hardness],
        'solids': [water.solids],
        'chloramines': [water.chloramines],
        'sulfate': [water.sulfate],
        'conductivity': [water.conductivity],
        'organic_carbon': [water.organic_carbon],
        'trihalomethanes': [water.trihalomethanes],
        'turbidity': [water.turbidity]
    })

    predicted_val = model.predict(sample)

    if predicted_val == 1:
        return 'Water is consumable'
    else:
        return 'Water is not consumable'