from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_apt_location_names', methods=['GET'])
def get_apt_location_names():
    response = jsonify({
        'locations': util.get_apt_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_house_location_names', methods=['GET'])
def get_house_location_names():
    response = jsonify({
        'locations': util.get_house_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_apt_price', methods=['GET', 'POST'])
def predict_apt_price():
    location = request.form['location']
    rooms = int(request.form['rooms'])
    area = float(request.form['area'])
    floor = float(request.form['floor'])

    response = jsonify({
        'estimated_price': util.get_apt_estimated_price(location, rooms, area, floor)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_house_price', methods=['GET', 'POST'])
def predict_house_price():
    location = request.form['location']
    rooms = int(request.form['rooms'])
    area = float(request.form['area'])
    groundArea = float(request.form['groundArea'])

    response = jsonify({
        'estimated_price': util.get_house_estimated_price(location, rooms, area, groundArea)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Python Flask Server For Home Price Prediction . . .')
    util.load_saved_artifacts()
    app.run()
