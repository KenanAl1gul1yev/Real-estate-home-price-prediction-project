import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings('ignore')

__locations = []
__data_columns = []
__model = []


def get_estimated_price(location: str, rooms: int, area: float, floor: float) -> str:
    try:
        loc_index = __data_columns.index(f'location_{location.lower()}')
    except:
        loc_index = -1
        location = 'other'

    X = np.zeros(len(__data_columns))
    X[0] = rooms
    X[1] = area
    X[2] = floor
    if loc_index >= 0:
        X[loc_index] = 1

    ans = round(__model.predict([X])[0], 2)

    return f'{int(ans * 95 / 100): ,}  -  {int(ans * 105 / 100): ,}'


def get_location_names():
    return __locations


def load_saved_artifacts():
    print('loading saved artifacts . . .start')
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        for i in range(len(__locations)):
            __locations[i] = __locations[i][9:]

    with open('./artifacts/azerbaijan_apt_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts . . .done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('20 yanvar m.', 2, 85, 3 / 14))
    print(get_estimated_price('8 noyabr m.', 2, 85, 3 / 14))
    print(get_estimated_price('8 noyabr m.', 4, 150, 3 / 14))
