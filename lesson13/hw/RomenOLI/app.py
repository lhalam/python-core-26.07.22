from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:123@localhost/lesson13'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'sdfsdfsdf'
db = SQLAlchemy(app)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    expiration_date = db.Column(db.Date)
    done = db.Column(db.Boolean)

    def __init__(self, name, description, expiration_date, done):
        self.name = name
        self.description = description
        self.expiration_date = expiration_date
        self.done = done

    def __repr__(self):
        return self.name


@app.route('/')
def index():
    tasks = db.session.query(Tasks).all()
    not_done = db.session.query(Tasks).filter(Tasks.done == False).all()
    return render_template("home.html", tasks=len(tasks), not_done=len(not_done))


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = db.session.query(Tasks).all()
    return render_template("task/list_tasks.html", tasks=tasks)


@app.route('/task/checked/<int:pk>', methods=['GET'])
def checked_task(pk):
    task = db.session.query(Tasks).get(pk)
    task.done = not task.done
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('list_tasks'))


@app.route('/task', methods=['POST', 'GET'])
def add_task():
    if request.method == 'GET':
        return render_template('task/add_task.html')
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        expiration_date = request.form['expiration_date']
        done = True
        task = Tasks(name, description, expiration_date, done)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list_tasks'))


@app.route('/task/del/<int:pk>', methods=['GET', 'POST'])
def delete_task(pk):
    task = db.session.query(Tasks).get(pk)
    if request.method == 'GET':
        return render_template('task/delete_task.html', task=task)
    elif request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('list_tasks'))


@app.route('/task/<int:pk>', methods=['GET', 'POST'])
def update_task(pk):
    task = db.session.query(Tasks).get(pk)
    if request.method == 'GET':
        return render_template('task/update_task.html', task=task)
    elif request.method == 'POST':
        flag = False
        if not task.name == request.form["name"]:
            task.name = request.form["name"]
            flag = True
        if not task.description == request.form["description"]:
            task.description = request.form["description"]
            flag = True
        if not task.expiration_date == datetime.strptime(request.form["expiration_date"], '%Y-%m-%d').date():
            task.expiration_date = datetime.strptime(request.form["expiration_date"], '%Y-%m-%d').date()
            flag = True
        done = False if request.form.get("done") == None else True
        if not task.done == done:
            task.done = done
            flag = True
        if flag:
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('list_tasks'))


if __name__ == "__main__":
    db.create_all()
    app.run()
