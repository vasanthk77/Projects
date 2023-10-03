from fastapi import FastAPI
from pydantic import BaseModel
import pickle


## 1 creation of the app

app = FastAPI()

##2 crate the model pydantic using basemodel

class ModelInput(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

## 3 load the model 
# Load the saved water purity check model

water_purity = pickle.load(open('purity_check.sav', 'rb'))


## 4 creation of routes for the api

@app.get('/Hello')
def hello():
    return {"welcome to the water purity check"}

@app.post('/predict')
def water_purity_prediction(input_parameters: ModelInput):
    ph1 = input_parameters.ph
    hard = input_parameters.Hardness
    solid = input_parameters.Solids
    chlor = input_parameters.Chloramines
    sul = input_parameters.Sulfate
    conduct = input_parameters.Conductivity
    org_car = input_parameters.Organic_carbon
    trihal = input_parameters.Trihalomethanes
    Turbi = input_parameters.Turbidity

    input_list = [ph1, hard, solid, chlor, sul, conduct, org_car, trihal, Turbi]

    # Use the predict method from the loaded model
    prediction = water_purity.predict([input_list])

    if prediction[0] == 0:
        return {"message": "This is not Potable water"}
    else:
        return {"message": "This is Potable water"}
