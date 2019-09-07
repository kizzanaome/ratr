from flask import Flask
from modes import db
from . import config



def create_app(config_name):
    app = Flask(__name__)
    app.config[
        'SQLALCHAMEY_DATABASE_URL'] = "postgresql://postgres:1460@localhost:5432/postgres"
    app.config['SQLALCHAMEY_TRACK_NOTIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app
