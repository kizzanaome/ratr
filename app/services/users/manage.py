import os
import click
from flask.cli import FlaskGroup
from flask_script import Manager, Command  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from user_app import create_app
from models import db


def create_flask_app(info=None):

    config_name = "development"
    app = create_app(config_name)
    migrate = Migrate(app, db)
    manager = Manager(app)
    return app


# manager.add_command('db', MigrateCommand)

@click.group(cls=FlaskGroup, create_app=create_flask_app)
def cli():
    pass

if __name__ == '__main__':
    cli()
