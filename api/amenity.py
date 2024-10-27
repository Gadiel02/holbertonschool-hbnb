# app/api/amenity.py
from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.amenity import Amenity
from app.repositories.amenity_repository import AmenityRepository

api = Namespace('amenities', description='Operations related to amenities')

amenity_model = api.model('Amenity', {
    'id': fields.String(required=True, description='Unique identifier of the amenity'),
    'name': fields.String(required=True, description='Amenity name'),
})

amenity_repo = AmenityRepository()

@api.route('/')
class AmenityList(Resource):
    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.response(201, 'Amenity created')
    def post(self):
        """Create a new amenity"""
        data = request.json
        new_amenity = Amenity(name=data['name'])
        amenity_repo.add(new_amenity)
        return new_amenity.to_dict(), 201

    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return [amenity.to_dict() for amenity in amenity_repo.all()], 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.doc('get_amenity')
    @api.response(200, 'Amenity found')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get an amenity by ID"""
        amenity = amenity_repo.get(amenity_id)
        return amenity.to_dict() if amenity else {'message': 'Amenity not found'}, 404

    @api.doc('update_amenity')
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an amenity by ID"""
        amenity = amenity_repo.get(amenity_id)
        if not amenity:
            return {'message': 'Amenity not found'}, 404

        amenity.name = request.json.get('name', amenity.name)
        amenity_repo.update(amenity)
        return amenity.to_dict(), 200
