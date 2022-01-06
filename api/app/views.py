from typing import Dict
from .models import PredictionRequest
from .utils import get_model, transform_to_df

model = get_model()

def get_prediction(request: dict) -> float:
    data_to_predict = transform_to_df(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, round(prediction, 2))

    