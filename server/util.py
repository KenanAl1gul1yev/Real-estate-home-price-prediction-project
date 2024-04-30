import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings('ignore')

__locations_apt = []
__data_columns_apt = []
__model_apt = []

__locations_house = []
__data_columns_house = []
__model_house = []


def get_apt_estimated_price(location: str, rooms: int, area: float, floor: float) -> str:
    try:
        loc_index = __data_columns_apt.index(f'location_{location.lower()}')
    except:
        loc_index = -1
        location = 'other'

    X = np.zeros(len(__data_columns_apt))
    X[0] = rooms
    X[1] = area
    X[2] = floor
    if loc_index >= 0:
        X[loc_index] = 1

    ans = round(__model_apt.predict([X])[0], 2)

    return f'{int(ans * 95 / 100): ,}  -  {int(ans * 105 / 100): ,}'


def get_house_estimated_price(location: str, rooms: int, area: float, ground_area: float) -> str:
    try:
        loc_index = __data_columns_house.index(f'location_{location.lower()}')
    except:
        loc_index = -1
        location = 'other'

    X = np.zeros(len(__data_columns_house))
    X[0] = rooms
    X[1] = area
    X[2] = ground_area
    if loc_index >= 0:
        X[loc_index] = 1

    ans = round(__model_house.predict([X])[0], 2)

    return f'{int(ans * 95 / 100): ,}  -  {int(ans * 105 / 100): ,}'


def get_apt_location_names():
    return __locations_apt


def get_house_location_names():
    return __locations_house


def load_saved_artifacts():
    print('loading saved artifacts apt . . .start')
    global __data_columns_apt
    global __locations_apt
    global __model_apt

    global __data_columns_house
    global __locations_house
    global __model_house

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns_apt = json.load(f)['data_columns']
        __locations_apt = __data_columns_apt[3:]
        for i in range(len(__locations_apt)):
            __locations_apt[i] = __locations_apt[i][9:]

    with open('./artifacts/azerbaijan_apt_prices_model.pickle', 'rb') as f:
        __model_apt = pickle.load(f)
    print('loading saved artifacts apt . . .done')

    print('loading saved artifacts house . . .start')
    with open('./artifacts/columns_house.json', 'r') as f:
        __data_columns_house = json.load(f)['data_columns']
        __locations_house = __data_columns_house[3:]
        for i in range(len(__locations_house)):
            __locations_house[i] = __locations_house[i][9:]

    with open('./artifacts/azerbaijan_house_prices_model.pickle', 'rb') as f:
        __model_house = pickle.load(f)
    print('loading saved artifacts house . . .done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_apt_estimated_price('20 yanvar m.', 2, 85, 3 / 14))
    print(get_apt_estimated_price('8 noyabr m.', 2, 85, 3 / 14))
    print(get_house_estimated_price('Mərdəkan q.', 5, 200, 6))
    print(get_house_estimated_price('Hövsan q.', 9, 280, 5.5))
