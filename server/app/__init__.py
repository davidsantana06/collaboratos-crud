from flask import Flask
from importlib import import_module

from .config import config_enviroment, config_extensions


app = Flask(__name__)

config_enviroment(app)
config_extensions(app)

import_module('app.routes')
