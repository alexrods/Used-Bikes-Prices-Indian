from os import sep
import re
import sys
import logging
import numpy as np
import pandas as pd
from dvc import api
from io import StringIO

import warnings 
warnings.filterwarnings('ignore')


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)
logging.info('Fetching data...')

bikes_data_path = api.read('data/raw/bikes.csv', remote='dataset-track')

bikes = pd.read_csv(StringIO(bikes_data_path))

bikes.dropna(inplace=True)
#i'll ignore bikes with price equals 0 
bikes = bikes[bikes['price']>0]
bikes.reset_index(drop=True, inplace=True)

bikes_names = bikes['model_name']
# I´ll split the column "model_name" in blankspace   
bikes_names = bikes_names.str.replace("Royal Enfield", "Royal-Enfield")
bikes_names = bikes_names.str.replace("BenelliImperiale", "Benelli Imperiale")
bikes_names = bikes_names.str.split(pat=" ")

# i´ll create a column with "brand_name" feature 
brand = []
model_dirty = []
for i in range(len(bikes_names)):
    brand.append(bikes_names.iloc[i][0])
    model_dirty.append(bikes_names.iloc[i][1:-1])
brand_name = pd.DataFrame(brand, columns=["brand_name"])

# i´ll create two columns, "model_name" and "motor_size"
patron_location = re.compile('(\d{3,})')
motor_size = []
model_name = []
for model in model_dirty:
    model_str = " ".join(model[:6])
    if model[0] == " ":   
        model_name.append(model[1])
    else:
        model_name.append(model[0])

    try:
        size = patron_location.search(model_str)
        motor_size.append(float(size.group(1)))
    except:
        motor_size.append(np.nan)
model_name_col = pd.DataFrame(model_name, columns=["model_name"])
model_name_col.replace("FZs", "FZS", inplace=True)
model_name_col.replace("YZFR15", "YZF-R15", inplace=True)
motor_size_col = pd.DataFrame(motor_size, columns=["motor_size"])
model_name_col.replace("\d{3,}cc", "", regex=True, inplace=True)

name_stract = pd.concat([brand_name, model_name_col, motor_size_col], axis=1)
name_stract['brand_name'].replace("Royal-Enfield\u200e", "Royal-Enfield", inplace=True)

bikes['kms_driven'] = bikes['kms_driven'].replace('[A-Za-z-\s]+', '', regex=True)
kms_driven_list = []
for i in range(len(bikes)):
    try:
        kms_driven_list.append(float(bikes['kms_driven'].iloc[i]))
    except Exception as e:
        kms_driven_list.append(np.nan)        
kms_driven = pd.DataFrame(kms_driven_list, columns=["kms_driven"])

bikes['mileage'].replace('[\sA-Za-z]+', '', regex=True, inplace=True)
bikes['mileage'].replace('', '0', regex=True, inplace=True)
mileage_list = []
for i in range(len(bikes)):
    try:
        mileage_list.append(float(bikes['mileage'].iloc[i][:2]))
    except:
        mileage_list.append(np.nan)
mileage = pd.DataFrame(mileage_list, columns=["mileage"])

bikes['owner'].replace({'first owner': 1, 'second owner': 2, 'third owner': 3, 'fourth owner or more': 4}, inplace=True)

power_col = bikes['power']
power_splited = power_col.str.split(pat=" ")
power_list = []
for i in range(len(bikes)):
    try:
        power_list.append(power_splited.iloc[i][0])
    except:
        power_list.append(np.nan)
power = pd.DataFrame(power_list, columns=["power"])
power['power'].replace('[\sA-Za-z]+', '', regex=True, inplace=True)
power['power'].replace('-.*', '', regex=True, inplace=True)
power['power'] = power['power'].astype(float)

bikes['years'] = 2021 - bikes['model_year']

bikes_new = pd.concat([name_stract, bikes['years'], kms_driven, mileage, bikes['owner'], power, bikes['price']], axis=1)
bikes_new.dropna(inplace=True)
bikes_new = bikes_new[bikes_new['kms_driven'] < bikes_new['kms_driven'].quantile(0.975)]
bikes_new = bikes_new[bikes_new['price'] < 3000000]
idx = bikes_new['brand_name'].value_counts()[bikes_new['brand_name'].value_counts() > 2].index.tolist()
bikes_new = bikes_new[bikes_new['brand_name'].isin(idx)]

bikes_new.to_csv('data/processed/bikes_processed.csv', index=False)

logger.info("Data Fetched and prepared...")

