from os import path


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
ENV_FILE = path.join(ROOT_FOLDER, '.env')
DATABASE_FILE = path.join(ROOT_FOLDER, 'database.sqlite3')
