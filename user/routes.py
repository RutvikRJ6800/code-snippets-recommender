import flask
from app import app, render_template
from user.models import User
from functools import wraps
from flask import session, redirect

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/login')
  
  return wrap

@app.route('/register', methods=['POST'])
def register():
  print("signup called")
  return User().signup()

@app.route('/login', methods=['GET'])
def login():
  print("login called")
  return render_template('login.html'), 200

@app.route('/signup', methods=['GET'])
def signup():
  print("signup called")
  return render_template('signup.html'), 200

@app.route('/auth', methods=['POST'])
def auth():
  print("auth called")
  # make authentication here
  return User().login()


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
  return render_template('newHome.html')


@app.route('/logout', methods=['GET'])
def logout():
  return User().signout()