from flask import Flask
from .config import config_enviroment, config_extensions, config_modules


def create_app() -> Flask:
    app = Flask(__name__)
    config_enviroment(app)
    config_extensions(app)
    config_modules(app)
    return app
