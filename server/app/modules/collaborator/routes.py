from flask import jsonify, request
from http import HTTPStatus

from . import collaborator
from .forms import *
from .services import *


@collaborator.get('/')
def get():
    return {'collaborators': find_all_collaboratos()}, HTTPStatus.OK


@collaborator.post('/')
def create():
    form = CreateForm(request.form, meta={'csrf': False})
    message, category = 'Os dados do formulário são inválidos!', 'danger'
    status_code = HTTPStatus.BAD_REQUEST
    
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        participation = form.participation.data

        if not validate_participation(participation):
            message = 'A taxa de participação excede o limite!'
            status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        else:
            create_collaborator(first_name, last_name, participation)
            message, category = 'O colaborador foi criado com sucesso!', 'success'
            status_code = HTTPStatus.CREATED

    return {'message': message, 'category': category}, status_code


@collaborator.delete('/<int:collaborator_id>')
def delete(collaborator_id: int):
    collaborator = find_collaborator_by_id(collaborator_id)
    message, category = 'O colaborador foi deletado!', 'success'
    status_code = HTTPStatus.NOT_FOUND

    if collaborator is not None:
        delete_collaborator(collaborator)
        status_code = HTTPStatus.OK

    return {'message': message, 'category': category}, status_code
