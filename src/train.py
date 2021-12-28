from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder, PowerTransformer

import sys
import logging
import numpy as np
import pandas as pd


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Loading data...')
data = pd.read_csv('../data/processed/bikes_processed.csv')
logging.info('Loading data...')

cat_features = ['brand_name', 'model_name']
cat_transformer = OneHotEncoder(handle_unknown='ignore')

num_features = ['motor_size', 'years', 'kms_driven',
                'mileage', 'power']
num_transformer = PowerTransformer()

column_transform = ColumnTransformer(
    transformers=[
        ("num", num_transformer, num_features),
        ("cat", cat_transformer, cat_features)
    ]
)

model = Pipeline([("col_trans", column_transform),
                 ("regressor", GradientBoostingRegressor())])

logging.info("Separating dataset into train and test...")
X = data.drop(['price'], axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



