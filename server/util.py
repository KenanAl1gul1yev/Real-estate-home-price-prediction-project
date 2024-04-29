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


def get_apt_location_names():
    return __locations_apt


def load_saved_artifacts():
    print('loading saved artifacts . . .start')
    global __data_columns_apt
    global __locations_apt
    global __model_apt

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns_apt = json.load(f)['data_columns']
        __locations_apt = __data_columns_apt[3:]
        for i in range(len(__locations_apt)):
            __locations_apt[i] = __locations_apt[i][9:]

    with open('./artifacts/azerbaijan_apt_prices_model.pickle', 'rb') as f:
        __model_apt = pickle.load(f)
    print('loading saved artifacts . . .done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_apt_location_names())
    print(get_apt_estimated_price('20 yanvar m.', 2, 85, 3 / 14))
    print(get_apt_estimated_price('8 noyabr m.', 2, 85, 3 / 14))
    print(get_apt_estimated_price('8 noyabr m.', 4, 150, 3 / 14))
