from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(title="Used Car Price Prediction API")

# Load trained model once at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def normalize_model(model: str) -> str:
    if not model or model.strip() == "":
        return "unknown"
    return model.lower()

# Define input schema
from pydantic import BaseModel

class CarInput(BaseModel):
    Location: str
    Year: int
    Kilometers_Driven: int
    Fuel_Type: str
    Transmission: str
    Owner_Type: str
    Seats: int
    Brand: str
    Model: str

    Mileage_KMPH: float
    Engine_CC: float
    Power_BHP: float



@app.post("/predict")
def predict(data: CarInput):
    # Convert request body to dictionary
    input_dict = data.dict()

    # Convert frontend fields to model-required fields
    input_dict["mileage_num"] = input_dict.pop("Mileage_KMPH")
    input_dict["engine_num"] = input_dict.pop("Engine_CC")
    input_dict["power_num"] = input_dict.pop("Power_BHP")

    # Create DataFrame
    df = pd.DataFrame([input_dict])

    # Feature engineering
    df["car_age"] = datetime.now().year - df["Year"]

    # Make prediction
    prediction = model.predict(df)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }


