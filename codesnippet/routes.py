import flask
from flask import request
from app import app, render_template
from codesnippet.models import Snippet

@app.route('/search', methods=['GET'])
def search():
    query = request.args["query"]
    print(query)

    return Snippet().search(query)

@app.route('/dashboard/upload')
def showUploadForm():
  print("showUploadForm called")  
  return render_template('upload.html')


@app.route('/dashboard/upload/snippet', methods=['POST'])
def addCodeSnippet():
  print("addCodeSnippet called.")
  return Snippet().add()

