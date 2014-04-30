import sys
sys.path.append('/projects/flaskApp/settings.py')
from settings import mysqlConnection

SQLALCHEMY_DATABASE_URI = mysqlConnection

CSRF_ENABLED = True
SECRET_KEY = 'wow-this-is-a-difficult-key'