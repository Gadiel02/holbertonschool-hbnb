from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.user import User
from app.repositories.user_repository import UserRepository

api = Namespace('users', description='User operations')

# Modelos de respuesta
error_model = api.model('Error', {
    'message': fields.String(required=True, description='Error message')
})

user_model = api.model('User', {
    'id': fields.String(readonly=True, description='Unique user identifier'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
})

repo = UserRepository()

@api.route('/')
class UserList(Resource):
    @api.doc('create_user')
    @api.expect(user_model)
    @api.response(201, 'User created', user_model)
    @api.response(400, 'Invalid input', error_model)
    def post(self):
        """Create a new user"""
        data = request.json or {}
        if 'first_name' not in data or 'last_name' not in data:
            return {'message': 'Missing required fields'}, 400

        new_user = User(first_name=data['first_name'], last_name=data['last_name'])
        repo.add(new_user)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name
        }, 201

    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = repo.all()
        return [{'id': u.id, 'first_name': u.first_name, 'last_name': u.last_name} for u in users], 200

@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    @api.response(404, 'User not found', error_model)
    def get(self, user_id):
        """Get a user by ID"""
        user = repo.get(user_id)
        if not user:
            api.abort(404, f"User {user_id} not found")
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name}, 200

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model)
    @api.response(404, 'User not found', error_model)
    @api.response(400, 'Invalid input', error_model)
    def put(self, user_id):
        """Update a user by ID"""
        data = request.json or {}
        user = repo.get(user_id)
        if not user:
            api.abort(404, f"User {user_id} not found")

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        repo.update(user)
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name}, 200

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    @api.response(404, 'User not found', error_model)
    def delete(self, user_id):
        """Delete a user by ID"""
        user = repo.get(user_id)
        if not user:
            api.abort(404, f"User {user_id} not found")

        repo.delete(user_id)
        return '', 204
