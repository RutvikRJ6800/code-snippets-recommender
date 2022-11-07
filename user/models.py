from flask import jsonify, request, session, redirect, render_template
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:

  """ ----------------------------------
    start session on successful login
    -----------------------------------"""
  def start_session(self, user):
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  """ ----------------------------------
    create new user
    -----------------------------------"""
  def signup(self):
    user = {
        "_id":uuid.uuid4().hex,
        "name":request.form.get("name"),
        "password":request.form.get("password")
    }

    user["password"] = pbkdf2_sha256.encrypt(user["password"]) # encrypt password

    if db.users.find_one({"name":user["name"]}):
      return jsonify({"error": "User with this username already exist."}), 400 # return error if username is already exist

    if db.users.insert_one(user):
      return jsonify(user), 200

    return jsonify({"error": "Signup failed."}), 400


  def signout(self):
    session.clear()
    print("signout: session cleared")
    return redirect('/')
  
  def login(self):
    user = db.users.find_one({
      "name": request.form.get('name')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      print("login successfull",user)
      return self.start_session(user)
      # return render_template('newHome.html'), 200

    print("invalid login creds")
    
    return jsonify({ "error": "Invalid login credentials" }), 401


