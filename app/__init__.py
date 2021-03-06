from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# update user model class -- look into redis model so that you can organize your data that is registered
# See https://www.openshift.com/blogs/use-flask-login-to-add-user-authentication-to-your-python-application
# after that, add different actions for login methods (from user model) when in /login
# then add secured views
from app import views, models