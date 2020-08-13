from flask import Flask, request, jsonify
import json
from service import ToDoService
from models import Schema

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

#@app.route("/<name>")
#def hello_name(name):
#    return "Hello, " + name + "!"

@app.route("/todo", methods=["POST"])
def todo_create():
    #return params
    #print(json)
    #print("yes")
    #return jsonify({"msj":"hello"})
    return jsonify(ToDoService().create(request.json))

@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))

@app.route("/todo/<item_id>", methods=["PUT"])
def update_items(item_id):
    return jsonify(ToDoService().update(item_id, request.json))

@app.route("/todo", methods=["GET"])
def list_item():
    return jsonify(ToDoService().list_all())

if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='127.0.0.1', port=8080)