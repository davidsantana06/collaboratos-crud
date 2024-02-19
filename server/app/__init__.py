from flask import Flask
from .config import *


def create_app() -> Flask:
    app = Flask(__name__)
    config_enviroment(app)
    config_extensions(app)
    config_modules(app)
    return app
