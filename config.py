from mysql_settings import mysqlConnection

# note have to install mysql connector: pip install mysql-python
SQLALCHEMY_DATABASE_URI = mysqlConnection

CSRF_ENABLED = True
SECRET_KEY = 'wow-this-is-a-difficult-key'