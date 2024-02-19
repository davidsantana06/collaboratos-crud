from dotenv import load_dotenv
from flask import Blueprint, Flask
from importlib import import_module
from os import listdir, environ

from .constants import DATABASE_FILE, ENV_FILE, MODULE_FOLDER, MODULES_FOLDER, MODULE_PATH
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


def config_modules(app: Flask) -> None:
    for module_name in listdir(MODULES_FOLDER):
        module_folder = MODULE_FOLDER.format(module_name)

        if '__init__.py' in listdir(module_folder):
            module_path = MODULE_PATH.format(module_name)
            module = import_module(module_path)

            for _, item in module.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
