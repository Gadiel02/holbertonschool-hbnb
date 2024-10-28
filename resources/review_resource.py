# resources/review_resource.py
from flask_restx import Resource, Namespace, fields
from flask import request
from app.services.facade import Facade

# Crear el namespace para las reseñas
api = Namespace('reviews', description="Operaciones relacionadas con reseñas")

# Definir el modelo para la reseña
review_model = api.model('Review', {
    'user_id': fields.String(required=True, description="ID del usuario que hace la reseña"),
    'place_id': fields.String(required=True, description="ID del lugar reseñado"),
    'text': fields.String(description="Texto de la reseña"),
    # Otros campos necesarios para la reseña
})

@api.route('/')
class ReviewListResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Obtener la lista de reseñas"""
        return Facade.get_all_reviews()
    
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self):
        """Crear una nueva reseña"""
        return Facade.create_review(request.json), 201

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Obtener una reseña por ID"""
        return Facade.get_review(review_id)

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Actualizar una reseña por ID"""
        return Facade.update_review(review_id, request.json)

    def delete(self, review_id):
        """Eliminar una reseña por ID"""
        Facade.delete_review(review_id)
        return {'message': 'Reseña eliminada'}, 204
