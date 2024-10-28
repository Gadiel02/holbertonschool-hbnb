# app/main.py
from flask import Flask
from flask_restx import Api
from app.api.user import api as user_api
from app.api.amenity import api as amenity_api
from app.api.place import api as place_api  # Import the place API

app = Flask(__name__)
api = Api(app)

api.add_namespace(user_api, path='/api/v1/users')
api.add_namespace(amenity_api, path='/api/v1/amenities')
api.add_namespace(place_api, path='/api/v1/places')  # Register the place API

if __name__ == '__main__':
    app.run(debug=True)
