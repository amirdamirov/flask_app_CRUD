from app_init.app_factory import create_app
from db_setup.db_conf import db
from app.models import Todo
from flask import request
from flask import jsonify
import os

settings_name = os.getenv("APP_SETTINGS")

app = create_app(settings_name)

@app.route("/")
def test():
    return jsonify({"app" : "work"})

### add items


@app.route("/list",methods=["GET"])
def get_tasks():
    tasks = db.session.query(Todo).all()
    temp = []
    for i in tasks:
        temp_dict = {
            "id" : i.id,
            "name" : i.text,
            "surname" : i.complete
        }
        temp.append(temp_dict)

    return jsonify(temp),200


@app.route("/list", methods = ["POST"])
def add_l():
    data = request.json
    task = Todo(**data)
    db.session.add(task)
    db.session.commit()
    temp_dict = {
        "id" : task.id,
        "text" : task.text,
        "complete" : task.complete
    }

    return jsonify(temp_dict),201

@app.route("/list/<id>", methods=["DELETE"])
def dele_l(id):
    task = db.session.query(Todo).filter_by(id=id).first() 

    if not task:
        return jsonify({"message":"Bele task sihtirib yoxdu"}),404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"result": True}), 202


@app.route("/list/<id>", methods=["PUT"])
def chng_l(id):
    data = request.json
    task = db.session.query(Todo).filter_by(id=id).first() 
    if not task:
        return jsonify({"message":"Bele task sihtirib yoxdu"}),404
    if data.get("text"):
        task.text = data.get("text")
    if data.get("complete"):
        task.complete = data.get("complete")

    db.session.add(task)
    db.session.commit()
    temp_dict = {
        "id" : task.id,
        "text" : task.text,
        "complete" : task.complete           # bir dene sual verek de tayy kechib
    }
    return jsonify(temp_dict),200

@app.route("/list/<id>",methods=["GET"])
def get_task_id(id):
    task = db.session.query(Todo).filter_by(id=id).first()

    if task:
        temp_dict = {
            "id" : task.id,
            "name" : task.text,
            "surname" : task.complete
        }
        return jsonify(temp_dict),200
    else:
        return jsonify({"message" : "User not found"}),404