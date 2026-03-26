from .ml.model_loader import load_model
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def predict_single(data):
    model = load_model()   # ✅ SAFE

    features = np.array(
        [[data.sqft_living, data.bedrooms, data.bathrooms]],
        dtype=float
    )

    prediction = model.predict(features)
    logger.info(
        f"Prediction request | sqft={data.sqft_living}, "
        f"bed={data.bedrooms}, bath={data.bathrooms} "
        f"=> price={prediction}"
    )
    return round(float(prediction[0]), 2)


def predict_bulk(features: np.ndarray):
    model = load_model()   # ✅ SAFE

    predictions = model.predict(features)
    return [round(float(p), 2) for p in predictions]

