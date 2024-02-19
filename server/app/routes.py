from flask import request
from http import HTTPStatus

from . import app, services
from .forms import CreateCollaboratorForm


@app.get('/')
def get_collaborators():
    return {'collaborators': services.find_all_collaboratos()}, HTTPStatus.OK


@app.post('/')
def create_collaborator():
    form = CreateCollaboratorForm(request.form)
    message, category = 'Os dados do formulário são inválidos!', 'danger'
    status_code = HTTPStatus.BAD_REQUEST
    
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        participation = form.participation.data

        if not services.validate_collaborator_participation(participation):
            message = 'A taxa de participação excede o limite!'
            status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        else:
            services.create_collaborator(first_name, last_name, participation)
            message, category = 'O colaborador foi criado com sucesso!', 'success'
            status_code = HTTPStatus.CREATED

    return {'message': message, 'category': category}, status_code


@app.delete('/<int:collaborator_id>')
def delete_collaborator(collaborator_id: int):
    collaborator = services.find_collaborator_by_id(collaborator_id)
    message, category = 'O colaborador foi deletado!', 'success'
    status_code = HTTPStatus.NOT_FOUND

    if collaborator is not None:
        services.delete_collaborator(collaborator)
        status_code = HTTPStatus.OK

    return {'message': message, 'category': category}, status_code
