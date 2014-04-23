from app import app
from forms import RegistrationForm
@app.route('/')
@app.route('/index')
def index():
	return "hellow"

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = Registration(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data, form.password.data)
		db_session.add(user)
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)



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