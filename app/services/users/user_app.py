from flask import Flask
from models import db
from config import app_config
from blueprint import users

def create_app(config_name):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(app_config)
    app.config['SQLALCHAMEY_TRACK_NOTIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(users)
