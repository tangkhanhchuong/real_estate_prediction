import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations



def get_data_columns():
    return __data_columns




def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open('./artifacts/real_estate_price.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_estimated_price(bedrooms,bathrooms,area,used_area,furniture_status,balcony,garage,private_pool,district,loaisohong):    
    
    X = pd.read_csv("./artifacts/train_data.csv") 
    district_index = np.where(X.columns==district)[0][0]
    loaisohong_index = np.where(X.columns==loaisohong)[0][0]


    x = np.zeros(len(X.columns))
    x[0] = 0
    x[1] = bedrooms
    x[2] = bathrooms
    x[3] = area
    x[4] = used_area
    x[5] = furniture_status

    x[6] = balcony
    x[7] = garage
    x[8] = private_pool
    x[9] = 13.720461
    x[10] = 1.576874e+09

    if district_index >= 0:
        x[district_index] = 1
    
    if loaisohong_index >= 0:
        x[loaisohong_index] = 1

    return (__model.predict([x])[0])
    
