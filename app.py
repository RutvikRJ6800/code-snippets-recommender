from flask import Flask, render_template, session, redirect
from functools import wraps
from flask_pymongo import PyMongo
import pymongo


app = Flask(__name__)
app.secret_key = b'\xcf\xd0\x9b\xb6\xbe\xa1\x90\x91\x8dh\x17\x1d\xbb\xf4C\xe2'


app.config['MONGO_DBNAME'] = 'ssd'

app.config['MONGO_URI']= 'mongodb+srv://root:rp123123@lab8.qnzi7qu.mongodb.net/ssd?retryWrites=true&w=majority'
try:
    mongo=PyMongo(app)
    db = mongo.db
except:
    print("Error in db connection")

# @app.route('/')
# def home():
#   return "Hello world"


# Routes
from user import routes
from codesnippet import routes

# Decorators
# def login_required(f):
#   @wraps(f)
#   def wrap(*args, **kwargs):
#     if 'logged_in' in session:
#       return f(*args, **kwargs)
#     else:
#       return redirect('/')
  
#   return wrap

@app.route('/')
def home():
    obj = {
      "args":None
    }
    return render_template('home.html', event=obj)
