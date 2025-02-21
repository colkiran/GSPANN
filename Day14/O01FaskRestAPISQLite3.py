
from flask import Flask, make_response, request, jsonify
from flask_restful import Api, Resource
import dataset

app = Flask(__name__)
api = Api(app)

db = dataset.connect("sqlite:///api.db")

table = db['books']

def fetch_db_all():
    books=[]
    for book in table:
        books.append(book)
    return books


# table.insert(
#     {
#         'book_id': '1',
#         'name': 'Begning Python',
#         'Author': 'Jeff Thompson'
#     }
# )
# table.insert(
#     {
#         'book_id': '2',
#         'name': 'Python Design Patterns',
#         'Author': 'John Peter'
#     }
# )

class Books(Resource):

    def get(self):
        return make_response(jsonify(fetch_db_all()), 200)

api.add_resource(Books, "/getbooks")

if __name__ == '__main__':
    app.run(debug=True)