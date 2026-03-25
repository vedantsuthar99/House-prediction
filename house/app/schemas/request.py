from pydantic import BaseModel

class HouseInput(BaseModel):
    sqft_living: float
    bedrooms: int
    bathrooms: float
