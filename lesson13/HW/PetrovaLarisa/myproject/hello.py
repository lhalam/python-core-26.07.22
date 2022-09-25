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
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'sfjhvdfbhvbkjsdbjbnjhuhrgbiut'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    deadline = db.Column(db.Date)
    complete = db.Column(db.Boolean)

    def __init__(self, name, description, deadline, complete):
        self.name = name
        self.description =  description
        self.deadline = deadline
        self.complete = complete

    def __repr__(self):
        return self.name

@app.route('/')
def list_task():
    #show all tasks
    tasks = Task.query.all()
    return render_template("hello.html", tasks = tasks)


@app.route('/task', methods=["POST", "GET"])
#add new item
def add_task():
    if request.method == 'GET':
        return render_template("add.html")
    if request.method == 'POST':
            name = request.form["name"]
            description = request.form["description"]
            deadline = request.form["deadline"]
            complete = False
            task = Task(name, description, deadline, complete)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('add_task'))

@app.route('/edit/<int:task_id>', methods = ['GET', 'POST'])
#edit item
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if request.method == 'POST':
        task.name = request.form["name"]
        task.description = request.form["description"]
        task.deadline = request.form["deadline"]
        task.complete = False
        db.session.commit()
        return redirect(url_for('list_task'))
    else:
        return render_template("post_edit.html", task = task)


@app.route('/update/<int:task_id>')
#update task
def update(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('list_task'))

@app.route('/delete/<int:task_id>')
#delete task
def delete(task_id):
    task = Task.query.filter_by(id = task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('list_task'))

with app.test_request_context():

    url_for('static', filename='style.css')

if __name__ == '__main__':
    db.create_all()

    app.run()
