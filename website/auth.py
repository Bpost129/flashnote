from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  data = request.form
  print(data)
  return render_template('login.html', text="Hey there, ", user="Jim")

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password = request.form.get('password')
    conPassword = request.form.get('conPassword')


  return render_template('sign_up.html')