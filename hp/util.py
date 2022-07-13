import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def buy_price(location):
    sqft = [600,800,1200,1800]
    bhk = [1,2,3,4]
    bath = [1,2,3,4]
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    graph_dict = {}    
    for i in range(0,4):
        x = np.zeros(len(__data_columns))
        x[0] = sqft[i]
        x[1] = bath[i]
        x[2] = bhk[i]
        if loc_index>=0:
            x[loc_index] = 1

        price = abs(round(__model.predict([x])[0],2))
        graph_dict[sqft[i]] = price
    json_object = json.dumps(graph_dict, indent = 4)
    with open("artifacts/graph.json", "w") as outfile:
        outfile.write(json_object)

def get_location_names():
    return __locations

def load_saved_artifacts():
    global  __data_columns
    global __locations

    with open("artifacts/columns.json", "r") as f:


        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:] 

    global __model
    if __model is None:

        with open("artifacts/hp_model.pickle", 'rb') as f:

            __model = pickle.load(f)

load_saved_artifacts()
get_location_names()

