# resources/amenity_resource.py
from flask_restx import Resource, Namespace, fields
from flask import request
from facade import facade

api = Namespace('amenities', description="Operaciones relacionadas con amenidades")

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description="Nombre de la amenidad"),
    # Otros campos necesarios para amenidad
})

@api.route('/')
class AmenityListResource(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Obtener la lista de amenidades"""
        return facade.get_all_amenities()
    
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Crear una nueva amenidad"""
        data = request.json
        return facade.create_amenity(data), 201

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Obtener una amenidad por ID"""
        return facade.get_amenity(amenity_id)

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Actualizar una amenidad por ID"""
        data = request.json
        return facade.update_amenity(amenity_id, data)
    