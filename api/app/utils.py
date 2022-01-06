from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os
from io import BytesIO


def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH', 'models/model.pkl')
    with open(model_path, 'rb') as model_file:
        model = load(BytesIO(model_file.read()))

    return model


def transform_to_df(class_model: dict) -> DataFrame:
    transition_dictionary = {key: [value] for key, value in class_model.items()}
    data_frame = DataFrame(transition_dictionary)

    return data_frame

