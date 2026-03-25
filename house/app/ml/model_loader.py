import pickle
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

MODEL_PATH = os.path.join(BASE_DIR, "model", "house_model.pkl")
print("model",MODEL_PATH)

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train model first.")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

