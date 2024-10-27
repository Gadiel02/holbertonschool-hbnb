from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.place import Place
from app.repositories.place_repository import PlaceRepository
from app.repositories.user_repository import UserRepository
from app.repositories.amenity_repository import AmenityRepository

api = Namespace('places', description='Operations related to places')

place_model = api.model('Place', {
    'id': fields.String(required=True, description='Unique identifier of the place'),
    'name': fields.String(required=True, description='Place name'),
    'owner_id': fields.String(required=True, description='Owner ID (User)'),
    'description': fields.String(required=True, description='Place description'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude'),
    'amenities': fields.List(fields.String, description='Amenity IDs associated with the place'),
})

place_repo = PlaceRepository()
user_repo = UserRepository()
amenity_repo = AmenityRepository()

@api.route('/')
class PlaceList(Resource):
    @api.doc('create_place')
    @api.expect(place_model)
    @api.response(201, 'Place created')
    @api.response(400, 'Invalid data')
    def post(self):
        """Create a new place"""
        data = request.json
        if not (isinstance(data['price'], (int, float)) and data['price'] > 0):
            return {'message': 'Price must be positive'}, 400
        if not (-90 <= data['latitude'] <= 90):
            return {'message': 'Latitude must be between -90 and 90'}, 400
        if not (-180 <= data['longitude'] <= 180):
            return {'message': 'Longitude must be between -180 and 180'}, 400
        if not user_repo.get(data['owner_id']):
            return {'message': 'Owner not found'}, 404

        new_place = Place(
            name=data['name'], owner_id=data['owner_id'],
            description=data['description'], price=data['price'],
            latitude=data['latitude'], longitude=data['longitude'],
            amenities=data.get('amenities', [])
        )
        place_repo.add(new_place)
        return new_place.to_dict(), 201

    @api.doc('list_places')
    @api.marshal_list_with(place_model)
    def get(self):
        """List all places"""
        return [p.to_dict() for p in place_repo.all()], 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.doc('get_place')
    @api.response(200, 'Place found')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get a place by ID"""
        place = place_repo.get(place_id)
        return place.to_dict() if place else {'message': 'Place not found'}, 404

    @api.doc('update_place')
    @api.expect(place_model)
    @api.response(200, 'Place updated')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid data')
    def put(self, place_id):
        """Update a place by ID"""
        place = place_repo.get(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        data = request.json
        if 'price' in data and not (isinstance(data['price'], (int, float)) and data['price'] > 0):
            return {'message': 'Price must be positive'}, 400
        if 'latitude' in data and not (-90 <= data['latitude'] <= 90):
            return {'message': 'Latitude must be between -90 and 90'}, 400
        if 'longitude' in data and not (-180 <= data['longitude'] <= 180):
            return {'message': 'Longitude must be between -180 and 180'}, 400

        # Update fields only if present in `data`
        for field in ['name', 'description', 'price', 'latitude', 'longitude', 'amenities']:
            if field in data:
                setattr(place, field, data[field])

        place_repo.update(place)
        return place.to_dict(), 200
