from flask import Flask, request, jsonify
import util
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

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
    # try:
    #     print(request.json)
    # except:
    #     e = sys.exc_info()[0]
    #     print(e)
    pluck = lambda dict, *args: (dict[arg] for arg in args)
    bedrooms, bathrooms, area, used_area, furniture_status, balcony, garage, private_pool, district, sovereignty_type = pluck(request.json["body"], "bedrooms", "bathrooms", "area", "used_area", "furniture_status", "balcony", "garage", "private_pool", "district", "sovereignty_type")
    
    # estimated_price = util.get_estimated_price(2,1.0,59.1,54,0.0, 0, 0, 0,'Bình Thạnh','HĐ mua bán')
    estimated_price = util.get_estimated_price(bedrooms, bathrooms, area, used_area, furniture_status, balcony, garage, private_pool, district, sovereignty_type)
    response = jsonify({
        "estimated_price": estimated_price
    })
    # response = jsonify({
    #     "bedrooms": bedrooms, 
    #     "bathrooms": bathrooms, 
    #     "area": area, 
    #     "used_area": used_area, 
    #     "furniture_status": furniture_status, 
    #     "balcony": balcony, 
    #     "garage": garage, 
    #     "private_pool": private_pool, 
    #     "district": district, 
    #     "sovereignty_type": sovereignty_type
    # })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Start server")
    util.load_saved_artifacts()
    # print(util.get_location_names())
    app.run()