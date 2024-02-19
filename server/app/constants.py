from os import path


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))

ENV_FILE = path.join(ROOT_FOLDER, '.env')
DATABASE_FILE = path.join(ROOT_FOLDER, 'database.sqlite3')

APP_FOLDER = path.join(ROOT_FOLDER, 'app')
MODULES_FOLDER = path.join(APP_FOLDER, 'modules')
MODULE_FOLDER = path.join(MODULES_FOLDER, '{}')
MODULE_PATH = 'app.modules.{}'
