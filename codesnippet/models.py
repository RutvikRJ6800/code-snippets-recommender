from flask import jsonify, request, session, render_template
from datetime import datetime
from app import db
import uuid

class Snippet:

  """ ----------------------------------
    add new code snippet to database
    -----------------------------------"""
  def add(self):
    keywds = request.form.get("keywords")
    keywds = keywds.replace(" ", "")
    keywds = keywds.split(',')
    timeStr = datetime.now()

    code = request.form.get("codesnippet")
    code = code.strip()
    print("striped code:", code)

    snippet = {
        "_id":uuid.uuid4().hex,
        "username":session["user"]["name"],
        "codeSnippet":code,
        "keywords": keywds,
        "uploadedOn": timeStr.strftime("%d/%m/%Y %H:%M:%S")
    }

    if db.snippets.insert_one(snippet):
      print("snippet added", snippet)
      return jsonify(snippet), 200

    print("snippet adding failed", snippet)
    return jsonify({"error": "could'nt add codesnippet."}), 400

  """ ----------------------------------
    search code snippet from database
    -----------------------------------"""
  def search(self, query):
    item_details = db.snippets.find()
    # 
    #  add proper search functionality here
    # 
    snippet = []
    print("type:item_details:", type(item_details), "type:item:", type(item_details[0]))
    for item in item_details:
      # This does not give a very readable output
      print(item)
      snippet.append(item)

    return render_template('home.html', codesnippets=snippet)
