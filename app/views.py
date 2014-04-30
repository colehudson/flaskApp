# core
from app import app
from flask import render_template, request, flash, url_for, redirect
import redis
# forms
from forms import ContactForm
from forms import RegistrationForm
from forms import LoginForm
# models
from models import User

# Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Login with Flask-login
from flask.ext.login import LoginManager
# start up login manager and grab a userID to set session
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
	return "hello"

@app.route('/redis_check')
def redis():
	return r.get("id_graham")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	 # and form.validate()
	# User = []
	if request.method == 'POST':
		# how to make a counter for user ids
		# r.incr(form.username.data))
		
		user_handle = User()
		user_handle.register()
		# user_handle.id = "foo"
		# user_handle.username = form.username.data
		print user_handle.username
		# user_handle.register()

		flash('Information submitted to Redis')
		return redirect(url_for('login'))
	elif request.method == 'GET':
		return render_template('register.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
  	flash ('Contacted!')
  	return render_template('base.html', form=form)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@login_manager.user_loader
def load_user(userid):
	return r.get(int(userid))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user("cole")
        user_handle = user_loader()
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     user = {'username': 'fedoraAdmin'}
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# from flask import render_template, flash, redirect
# from app import app
# from forms import LoginForm

# # index view function suppressed for brevity

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html', 
#         title = 'Sign In',
#         form = form)