from app import app
from forms import ContactForm
from forms import RegistrationForm
from forms import LoginForm
from flask import render_template, request, flash, url_for, redirect, incr
import os
import redis


# Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)



@app.route('/')
@app.route('/index')
def index():
	return "hello"

@app.route('/redis_check')
def redis():
	return r.get("cole")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	 # and form.validate()
	User = []
	if request.method == 'POST':
		# how to make a counter for user ids
		# r.incr(form.username.data))

		# how to pass large amounts of data concatenated together
		# r.set("user_object": {"username":form.username.data,"email", form.email.data,"password", form.password.data)
		r.set(form.username.data, unicode(84))
		r.set("username", form.username.data)
		r.set("email", form.email.data)
		r.set("password", form.password.data)
		flash('Information submitted to Redis')
		return redirect(url_for('login'))
	elif request.method == 'GET':
		# if r.get("username") != 0:
			# return r.get("username")
			# return r.get("password")
			# return r.get("email")
		return render_template('register.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
  	flash ('Contacted!')
  	return render_template('base.html', form=form)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user("cole")
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