from flask.testing import FlaskClient
from http import HTTPStatus
from typing import Dict, Tuple
from werkzeug.test import TestResponse
import json

from . import *


def dictionaryize_response_data(response: TestResponse) -> Tuple[Dict[str, object], int]:
    return json.loads(response.data), response.status_code


def create_collaborator_data(first_name: str, last_name: str, participation: float) -> Dict[str, object]:
    return {'first-name': first_name, 'last-name': last_name, 'participation': participation}


def test_get_collaborators(client: FlaskClient) -> None:
    data, status_code = dictionaryize_response_data(client.get(URL))

    assert status_code == HTTPStatus.OK
    assert 'collaborators' in data


def test_create_collaborator_valid_input(client: FlaskClient) -> None:
    data, status_code = dictionaryize_response_data(
        client.post(URL, data=create_collaborator_data('Valid', 'Input', 1))
    )

    assert status_code == HTTPStatus.CREATED
    assert data.get('message') == 'O colaborador foi criado com sucesso!'
    assert data.get('category') == 'success'


def test_create_collaborator_invalid_input(client: FlaskClient) -> None:
    data, status_code = dictionaryize_response_data(
        client.post(URL, data=create_collaborator_data('Invalid', 'Input', 0))
    )

    assert status_code == HTTPStatus.BAD_REQUEST
    assert data.get('message') == 'Os dados do formulário são inválidos!'
    assert data.get('category') == 'danger'


def test_delete_collaborator(client: FlaskClient) -> None:
    data, status_code = dictionaryize_response_data(client.delete(URL + '999'))

    assert status_code == HTTPStatus.NOT_FOUND
    assert data.get('message') == 'O colaborador não foi encontrado.'
    assert data.get('category') == 'info'
