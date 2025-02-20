import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'item': '2 ltr bottle', 'price': 120, 'qty': 450},
    'coke': {'item': '500 ml bottle', 'price':40, 'qty': 600},
    'thumbs_up': {'item': '300 ml can', 'price': 50, 'qty': 150}
}

class Product(Resource):

    def get(self, product):
        return {product: products[product]}

    def put(self, product):
        products[product]['cat'] = request.form['cat']
        return {product: products[product]}

    def patch(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product][list(data.keys())[0]] = data[list(data.keys())[0]]
        return {product: products[product]}


api.add_resource(Product, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
