# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.config import Config
from app.resources.user_resource import api as user_ns
# Import other resources

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    api = Api(app)
    api.add_namespace(user_ns)
    # Add other namespaces

    return app
