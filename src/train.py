from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV

from xgboost import XGBRegressor

import sys
import logging
import numpy as np
import pandas as pd

from utils import update_model, save_simple_metrics_report, get_model_performance_test_set

import warnings 
warnings.filterwarnings('ignore')


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Loading data...')
data = pd.read_csv('data/processed/bikes_processed.csv')
logging.info('Loaded data...')

cat_features = ['brand_name', 'model_name']
cat_transformer = OneHotEncoder(handle_unknown='ignore')

num_features = ['motor_size', 'years', 'kms_driven',
                'mileage', 'power']
num_transformer = StandardScaler()

column_transform = ColumnTransformer(
    transformers=[
        ("num", num_transformer, num_features),
        ("cat", cat_transformer, cat_features)
    ]
)

logging.info("Separating dataset into train and test...")
X = data.drop(['price'], axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

model = Pipeline([('col_trans', column_transform),
                 ('regressor', RandomForestRegressor())])

logger.info("Setting Hyperparameters to tune...")
param_tuning = [
                {
                'regressor': [GradientBoostingRegressor()],
                'regressor__n_estimators': range(100, 1201, 100)
                },
                # {
                # 'regressor': [XGBRegressor()],
                # 'regressor__n_estimators': range(100, 501, 100)
                # }
               ]  

grid_search = GridSearchCV(model, param_tuning, scoring='r2', cv=6, n_jobs=-1)

logger.info("Starting grid search...")
grid_search.fit(X_train, y_train)

logger.info("Cross validating with the best model...")
final_result = cross_validate(grid_search.best_estimator_, X_train, y_train, return_train_score=True, cv=5)

train_score = np.mean(final_result['train_score'])
test_score = np.mean(final_result['test_score'])
assert train_score > 0.7
assert test_score > 0.65

logger.info(f"Train Score: {train_score}")
logger.info(f"Test Score: {test_score}")

logger.info("Updating model...")
update_model(grid_search.best_estimator_)

logger.info("Generating model report...")
validation_score = grid_search.best_estimator_.score(X_test, y_test)
save_simple_metrics_report(train_score, test_score, validation_score, grid_search.best_estimator_)

y_test_pred = grid_search.best_estimator_.predict(X_test)
get_model_performance_test_set(y_test, y_test_pred)

logger.info("Training Finished!")



