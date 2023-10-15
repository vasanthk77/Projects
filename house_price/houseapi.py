from fastapi import FastAPI, Request
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np

app = FastAPI()

# Load your trained machine learning model and StandardScaler
model = pickle.load(open('house_price.sav', 'rb'))
scaler = pickle.load(open('standard.sav', 'rb'))

class ModelInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post('/predict')
def predict(request: Request, input_data: ModelInput):
    # Extract the input features from the request
    input_features = [input_data.MedInc, input_data.HouseAge, input_data.AveRooms, input_data.AveBedrms, 
                      input_data.Population, input_data.AveOccup, input_data.Latitude, input_data.Longitude]

    # Standardize the input data using the pre-trained scaler
    input_features = np.array(input_features).reshape(1, -1)  # Reshape for single prediction
    input_features_scaled = scaler.transform(input_features)

    # Make a prediction using the model
    prediction = model.predict(input_features_scaled)

    # You can return the prediction as a response
    return {"prediction": prediction[0]}

##4

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)