from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        print('logged in')
        return redirect(url_for('views.home'))
      else:
        print('incorrect password')
    else:
      print('user doesnt exist')


  return render_template('login.html')

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password = request.form.get('password')
    con_password = request.form.get('con_password')

    user = User.query.filter_by(email=email).first()
    if user:
      print('email already exists')

    if email and first_name and password and con_password and (password == con_password):
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(password))
      db.session.add(new_user)
      db.session.commit()
      print('user created!')
      return redirect(url_for('views.home'))


  return render_template('sign_up.html')