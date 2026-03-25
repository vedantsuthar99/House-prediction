from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.schemas.request import HouseInput
from app.services.predictor import predict_single, predict_bulk

router = APIRouter(prefix="/api")

@router.post("/predict")
def predict_house_price(data: HouseInput):
    return {"predicted_price": predict_single(data)}


@router.post("/predict-csv")
def predict_from_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    required = ["sqft_living", "bedrooms", "bathrooms"]
    if not all(col in df.columns for col in required):
        raise HTTPException(400, "Invalid CSV format")

    features = df[required].values
    df["predicted_price"] = predict_bulk(features)

    return df.to_dict(orient="records")
