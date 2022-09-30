from flask import Flask, request, render_template, json, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Geheimnis123@localhost:5432/Test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'sfjhvdfbhvbkjsdbjbnjhuhrgbiut'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    deadline = db.Column(db.Date)
    is_done = db.Column(db.Boolean)


    # name = db.Column(db.String)
    # email = db.Column(db.String)
    # password = db.Column(db.String)


    def __init__(self, title, description, deadline, is_done):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_done = is_done


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = db.session.query(Task).all()
    return render_template("task/list_task.html", tasks=tasks)


@app.route('/tasks/<int:pk>', methods=['POST', 'GET', 'DELETE'])
def update_task(pk):
    task = db.session.query(Task).get(pk)
    print(request.method)
    if request.method == "GET":
        return render_template("task/update_task.html", task=task)
    if request.method == "POST":
        print(request.form)
        if not task.title == request.form["title"]:
            task.title = request.form["title"]
        if not task.description == request.form["description"]:
            task.description = request.form["description"]
        if not task.deadline == request.form["deadline"]:
            task.deadline = request.form["deadline"]
        task_is_done = True if request.form.get("is_done", "") == 'on' else False
        task.is_done = task_is_done
        print(task.is_done)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list_task'))
    if request.method == 'DELETE':
        print("In Delete")
        task = db.session.query(Task).get(pk)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('list_task'))


@app.route('/task', methods=['POST', 'GET'])
def add_task():
    if request.method == "GET":
        return render_template("task/add_task.html")
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        task = Task(title, description, deadline, is_done=False)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list_task'))


@app.route('/tasks/<int:pk>/delete', methods=['POST'])
def delete_task(pk):
    print('In delete')
    task = db.session.query(Task).get(pk)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('list_task'))


@app.route('/')
def hello_world():
    return render_template("home.html")


if __name__ == '__main__':
    db.create_all()

    app.run()
