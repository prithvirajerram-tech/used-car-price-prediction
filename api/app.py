from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# Initialize FastAPI app
app = FastAPI(title="Used Car Price Prediction API")

# Load trained model once at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input schema
class CarInput(BaseModel):
    Location: str
    Year: int
    Kilometers_Driven: int
    Fuel_Type: str
    Transmission: str
    Owner_Type: str
    Seats: int
    Brand: str
    Model: str = "unknown"
    Mileage: float
    Engine: float
    Power: float

@app.post("/predict")
def predict_price(data: CarInput):
    df = pd.DataFrame([data.dict()])

    # ---------------------------
    # Feature engineering
    # ---------------------------

    # car age
    df["car_age"] = 2024 - df["Year"]

    # 🔴 REQUIRED numeric columns (must exist)
    df["mileage_num"] = df["Mileage"]
    df["engine_num"] = df["Engine"]
    df["power_num"] = df["Power"]

    # ---------------------------
    # Safety defaults
    # ---------------------------
    if "Model" not in df.columns:
        df["Model"] = "unknown"

    # ---------------------------
    # Debug (remove later)
    # ---------------------------
    print("FINAL COLUMNS:", df.columns.tolist())

    prediction = model.predict(df)[0]

    return {"prediction": float(prediction)}


