important_settings import mysqlConnection, SECRET_KEY

# note have to install mysql connector: pip install mysql-python
SQLALCHEMY_DATABASE_URI = mysqlConnection

CSRF_ENABLED = True
