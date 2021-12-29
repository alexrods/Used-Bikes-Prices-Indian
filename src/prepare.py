import re
import sys
import logging
import numpy as np
import pandas as pd
from dvc import api
from io import StringIO


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data...\n')

bikes_data_path = api.read('data/raw/bikes.csv', remote='dataset-track')

bikes_data = pd.read_csv(StringIO(bikes_data_path))

bikes_data.dropna(inplace=True)
bikes_data = bikes_data[bikes_data['price']>0]


bikes_data["model_name"] = bikes_data["model_name"].str.replace("Royal Enfield", "Royal-Enfield")
bikes_data["model_name"] = bikes_data["model_name"].str.replace("Moto Guzzi", "Guzzi")
bikes_data["model_name"] = bikes_data["model_name"].str.replace("BenelliImperiale", "Benelli Imperiale")

bikes_names = bikes_data['model_name']
bikes_names = bikes_names.str.split(pat=" ")

# i´ll create a column with "brand_name" feature 

brand = []
model_dirty = []
for i in range(len(bikes_names)):
    brand.append(bikes_names.iloc[i][0])
    model_dirty.append(bikes_names.iloc[i][1:-1])

brand_name = pd.DataFrame(brand, columns=["brand_name"])
brand_name['brand_name'].replace("Royal-Enfield\u200e", "Royal-Enfield", inplace=True)

# i´ll create two columns, "model_name" and "motor_size"

patron_location = re.compile('(\d{3,})')
motor_size = []
model_name = []
for model in model_dirty:
    model_str = " ".join(model[:6])   
    model_name.append(model[0:1]) 
    try:
        size = patron_location.search(model_str)
        motor_size.append(float(size.group(1)))
    except:
        motor_size.append(np.nan)

model_name_col = pd.DataFrame(model_name, columns=["model_name"])
motor_size_col = pd.DataFrame(motor_size, columns=["motor_size"])

# Clean str values "kms_driven" column

bikes_data['kms_driven'] = bikes_data['kms_driven'].replace('[A-Za-z-\s]+', '', regex=True)

# Set column as float value and create new dataframe

kms_driven_list = []
for i in range(len(bikes_data)):
    try:
        kms_driven_list.append(float(bikes_data['kms_driven'].iloc[i]))
    except Exception as e:
        kms_driven_list.append(np.nan)
        
kms_driven = pd.DataFrame(kms_driven_list, columns=["kms_driven"])

# Clean str values "mileage" column

bikes_data['mileage'].replace('[\sA-Za-z]+', '', regex=True, inplace=True)
bikes_data['mileage'].replace('', '0', regex=True, inplace=True)

# Set column as float value and create new dataframe

mileage_list = []
for i in range(len(bikes_data)):
    try:
        mileage_list.append(float(bikes_data['mileage'].iloc[i][:2]))
    except:
        mileage_list.append(np.nan)

mileage = pd.DataFrame(mileage_list, columns=["mileage"])

# Replace str values from "owner" column and set as int value

bikes_data['owner'].replace({'first owner': 1, 'second owner': 2, 'third owner': 3, 'fourth owner or more': 4}, inplace=True)

# Clean str values "power" column

power_splited = bikes_data['power'].str.split(pat=" ")

power_list = []
for i in range(len(bikes_data)):
    try:
        power_list.append(power_splited.iloc[i][0])
    except:
        power_list.append(np.nan)

power = pd.DataFrame(power_list, columns=["power"])
power['power'].replace('[\sA-Za-z]+', '', regex=True, inplace=True)
power['power'].replace('-.*', '', regex=True, inplace=True)

power['power'] = power['power'].astype(float)

bikes_data['years'] = 2021 - bikes_data['model_year']

bikes_new = pd.concat([brand_name, model_name_col, motor_size_col, kms_driven, mileage, 
                       bikes_data['owner'], power, bikes_data['years'], bikes_data['price']], axis=1)
bikes_new.dropna(inplace=True)

idx = bikes_new["brand_name"].value_counts()[bikes_new["brand_name"].value_counts() > 2].index.tolist()
bikes_new = bikes_new[bikes_new["brand_name"].isin(idx)]

bikes_new = bikes_new[bikes_new['kms_driven'] < bikes_new['kms_driven'].quantile(0.975)]
bikes_new = bikes_new[bikes_new['price'] < 3000000]

bikes_new.to_csv('data/processed/bikes_processed.csv', index=False)

logger.info("Data Fetched and prepared...")

