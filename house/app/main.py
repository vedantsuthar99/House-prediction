from fastapi import FastAPI
from .routes.predict import router

app = FastAPI(title="House Price Prediction API", version="1.0")
app.include_router(router)
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "House Price Prediction API Running"}