# core
from app import app, db, login_manager
from flask import render_template, request, flash, url_for, redirect, abort, g
import redis
from flask.ext.login import login_user, logout_user, current_user, login_required
# forms
from forms import ContactForm
# from forms import RegistrationForm
# from forms import LoginForm
# models
from models import User, ROLE_USER, ROLE_ADMIN

# Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
@app.route('/index')
def index():
	return "hello"

@app.route('/redis_check')
def redis():
	return r.get("id_graham")

@app.before_request
def before_request():
    g.user = current_user


@app.route('/register', methods=['GET', 'POST'])
@app.before_request
def register():
	if request.method == 'POST':
	    user = User(request.form['username'] , request.form['password'], request.form['email'])
	    db.session.add(user)
	    db.session.commit()
	    flash('User successfully registered')
	    return redirect(url_for('login'))

	elif request.method == 'GET': 
		# form = RegistrationForm()
		return render_template('register.html')


@app.route('/contact', methods=['GET', 'POST'])
# @app.before_request
@login_required
def contact():
  form = ContactForm()
  # print g.user
  if request.method == 'POST':
  	flash ('Contacted!')
  	return render_template('base.html', form=form)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 

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