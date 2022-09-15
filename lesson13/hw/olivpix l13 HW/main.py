from flask import Flask, request, render_template, json, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/lessons'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'sfvfvjhvdfbhvbkjsdbjbnjhuhrgbiut'
db = SQLAlchemy(app)


class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    term = db.Column(db.Date)
    status = db.Column(db.String)

    def __init__(self, title, description, term):
        self.title = title
        self.description = description
        self.term = term
        self.status = "TODO"


@app.route("/")
def main_page():
    lessons = db.session.query(Lessons).all()
    return render_template("templ.html", lessons=lessons)


@app.route('/add_task', methods=['POST', 'GET'])
def add_user():
    if request.method == "GET":
        task_descr = request.args.get("task")
        return render_template("/add_task.html", task=task_descr, cho=1)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        term = request.form["term"]
        task = Lessons(title, description, term)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main_page'))


@app.route('/edit/<int:pk>', methods=['POST', 'GET'])
def edit(pk):
    task = db.session.query(Lessons).get(pk)
    if request.method == "GET":
        return render_template("/add_task.html", task=task, cho=2)
    if request.method == "POST":
        if not task.title == request.form["title"]:
            task.title = request.form["title"]
        if not task.description == request.form["description"]:
            task.description = request.form["description"]
        if not task.term == request.form["term"]:
            task.term = request.form["term"]
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main_page'))


@app.route('/changestatus/<int:pk>', methods=['POST', 'GET'])
def changestatus(pk):
    task = db.session.query(Lessons).get(pk)
    if task.status == "TODO":
        task.status = "DONE"
    else:
        task.status = "TODO"
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main_page'))


@app.route('/delete/<int:pk>', methods=['POST', 'GET'])
def delete(pk):
    Lessons.query.filter_by(id=pk).delete()
    db.session.commit()
    return redirect(url_for('main_page'))

@app.route('/view/<int:pk>', methods=['POST', 'GET'])
def view(pk):
    task = db.session.query(Lessons).get(pk)
    if request.method == "GET":
        return render_template("/view.html", task=task)


if __name__ == '__main__':
    db.create_all()
    app.run()
