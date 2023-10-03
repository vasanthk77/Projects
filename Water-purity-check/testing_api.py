import json
import requests

url = 'http://127.0.0.1:8000/predict'

input_data_for_model = {
    'ph': 9.44513,
    'Hardness': 145.80,
    'Solids': 13168.52,
    'Chloramines': 9.444,
    'Sulfate': 310.5833,
    'Conductivity': 592.65,
    'Organic_carbon': 8.606397,
    'Trihalomethanes': 77.457,
    'Turbidity': 3.875
}

# Send a POST request with the input data to the FastAPI endpoint
response = requests.post(url, json=input_data_for_model)  # Use 'json' instead of 'data'

print(response.text)

# Check the response from the API
if response.status_code == 200:
    result = response.json()  # Parse the JSON response
    print("Prediction is:", result)
else:
    print("Error:", response.status_code, response.text)
