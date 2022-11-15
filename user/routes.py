import flask
from app import app, render_template
from user.models import User

@app.route('/register', methods=['POST'])
def signup():
  print("signup called")
  return User().signup()

@app.route('/login', methods=['GET'])
def login():
  print("login called")
  return render_template('login.html'), 200

@app.route('/signup', methods=['GET'])
def sigunp():
  print("sigup called")
  return render_template('login.html'), 200

@app.route('/auth', methods=['POST'])
def auth():
  print("auth called")
  # make authentication here
  return User().login()


@app.route('/dashboard', methods=['GET'])
def dashboard():
  return render_template('newHome.html')


@app.route('/logout', methods=['GET'])
def logout():
  return User().signout()