from dotenv import load_dotenv
from flask import Flask
from importlib import import_module
from os import environ

from .constants import DATABASE_FILE, ENV_FILE
from .extensions import database


def config_enviroment(app: Flask) -> None:
    load_dotenv(ENV_FILE)
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DATABASE_FILE}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })


def config_extensions(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        import_module('app.models')
        database.create_all()
