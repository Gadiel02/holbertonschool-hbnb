# resources/user_resource.py
from flask_restx import Resource, Namespace, fields
from flask import request
from app.services.facade import facade

# Namespace para operaciones de usuario
api = Namespace('users', description="Operaciones para manejo de usuarios")

# Modelo de usuario para validación de entrada y salida
user_model = api.model('User', {
    'username': fields.String(required=True, description="Nombre de usuario"),
    'email': fields.String(required=True, description="Correo electrónico"),
    # Agregar más campos si son necesarios
})

@api.route('/')
class UserListResource(Resource):
    @api.marshal_list_with(user_model, code=200, description="Lista de usuarios")
    def get(self):
        """Recuperar todos los usuarios"""
        usuarios = facade.get_all_users()
        return usuarios, 200
    
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model, code=201, description="Usuario creado exitosamente")
    def post(self):
        """Crear un usuario nuevo"""
        usuario_data = request.json
        nuevo_usuario = facade.create_user(usuario_data)
        return nuevo_usuario, 201

@api.route('/<string:user_id>')
@api.param('user_id', 'El identificador único del usuario')
class UserResource(Resource):
    @api.marshal_with(user_model, code=200, description="Usuario encontrado")
    def get(self, user_id):
        """Obtener información de un usuario específico"""
        usuario = facade.get_user(user_id)
        return usuario, 200

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model, code=200, description="Usuario actualizado exitosamente")
    def put(self, user_id):
        """Actualizar los datos de un usuario"""
        nuevos_datos = request.json
        usuario_actualizado = facade.update_user(user_id, nuevos_datos)
        return usuario_actualizado, 200
