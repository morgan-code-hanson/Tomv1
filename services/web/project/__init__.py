from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
class Task(db.Model):
    __tablename__="tasks"
    id=db.Column(db.Integer,primary_key=True)
    desc=db.Column(db.String(128),nullable=False)
    def __init__(self, desc):
        self.desc = desc
    @app.route("/")
    def hello_world():
        return jsonify(hello="world")
