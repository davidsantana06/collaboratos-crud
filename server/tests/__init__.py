from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture

from app import create_app


URL = '/collaborators-crud/api/collaborator/'


@fixture
def app() -> Flask:
    return create_app()


@fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
