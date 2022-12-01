import flask
from flask import request, session, redirect
from app import app, render_template
from codesnippet.models import Snippet
from functools import wraps

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/login')
  
  return wrap

@app.route('/search', methods=['GET'])
def search():
    query = request.args["query"]
    print("query ==",query)

    return Snippet().search(query)

@app.route('/dashboard/upload')
@login_required
def showUploadForm():
  print("showUploadForm called")  
  return render_template('upload.html')


@app.route('/dashboard/upload/snippet', methods=['POST'])
@login_required
def addCodeSnippet():
  print("addCodeSnippet called.")
  return Snippet().add()

