# resources/place_resource.py
from flask_restx import Resource, Namespace, fields
from flask import request
from facade import facade

# Crear el namespace para los lugares
api = Namespace('places', description="Operaciones relacionadas con lugares")

# Definir el modelo para el lugar
place_model = api.model('Place', {
    'name': fields.String(required=True, description="Nombre del lugar"),
    'location': fields.String(description="Ubicación"),
    # Añade otros campos necesarios para el lugar
})

@api.route('/')
class PlaceListResource(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """Obtener la lista de lugares"""
        return facade.get_all_places()
    
    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        """Crear un nuevo lugar"""
        return facade.create_place(request.json), 201

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Obtener un lugar por ID"""
        return facade.get_place(place_id)

    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        """Actualizar un lugar por ID"""
        return facade.update_place(place_id, request.json)
    
    def delete(self, place_id):
        """Eliminar un lugar por ID"""
        facade.delete_place(place_id)
        return {'message': 'Lugar eliminado'}, 204
