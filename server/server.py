from flask import Flask, request, jsonify
import util
import json

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi, What is your name?"


@app.route('/locations')
def get_location_names():
    res = jsonify({'locations': util.get_location_names()})
    res.headers.add('Access-Control-Allow-Origin', '*')

    return res



@app.route('/predict', methods=['POST'])
def predict_home_price():
    pluck = lambda dict, *args: (dict[arg] for arg in args)
    bedrooms, bathrooms, area, used_area, furniture_status, balcony, garage, private_pool, district, loaisohong = pluck(request.json, "bedrooms", "bathrooms", "area", "used_area", "furniture_status", "balcony", "garage", "private_pool", "district", "loaisohong")

    print(area)
    response = jsonify({
        'estimated_price': util.get_estimated_price(2,1.0,59.1,54,0.0, 0, 0, 0,'Bình Thạnh','HĐ mua bán')
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print("Start server")
    util.load_saved_artifacts()
    # print(util.get_location_names())
    app.run()