from flask import Flask, request, render_template, url_for, json, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, MetaData, ForeignKey, text
metadata = MetaData()
app = Flask(__name__)
Bootstrap(app)
#engine = create_engine("postgresql://postgres:1@localhost:5432/todolist")
#print(engine)
# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/todolist'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'sfjhvdfbhvbkjsdbjbnjhuhrgbiut'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    deadline = db.Column(db.Date)

    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline

    def __repr__(self):
        return self.name

@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/task', methods=["POST", "GET"])
def add_task():
    if request.method == 'GET':
        return render_template("add.html")
    if request.method == 'POST':
            name = request.form["name"]
            description = request.form["description"]
            deadline = request.form["deadline"]
            tasks = Task(name, description, deadline)
            db.session.add(tasks)
            db.session.commit()
            return redirect(url_for('add_task'))


@app.route('/tasks', methods = ["GET"])
def list_task():
    tasks = db.session.query(Task).all()
    return render_template("hello.html", tasks=tasks)


with app.test_request_context():

    url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()
