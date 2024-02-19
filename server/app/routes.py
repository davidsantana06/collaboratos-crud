from . import app


@app.get('/')
def get_collaborators():
    ...


@app.post('/')
def create_collaborator():
    ...


@app.delete('/')
def delete_collaborator():
    ...
