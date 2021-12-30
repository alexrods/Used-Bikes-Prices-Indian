from pydantic import BaseModel


class PredictionRequest(BaseModel):
    brand_name: str
    model_name: str
    motor_size: float
    years: int
    kms_driven: float
    mileage: float
    owner: int
    power: float

class PredictionResponse(BaseModel):
    price: float