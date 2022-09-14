from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/lesson13'  # 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sfjhvdfbhvbkjsdbjbnjhuhrgbiut'

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(30))
    text = db.Column(db.String())
    complete = db.Column(db.Boolean())
    date = db.Column(db.DateTime(timezone=True), default=func.now())


@app.route('/')
def home():
    incomplete = Note.query.filter_by(complete=False).order_by(desc(Note.date)).all()
    complete = Note.query.filter_by(complete=True).order_by(desc(Note.date)).all()
    return render_template('home.html', incomplete=incomplete, complete=complete)


# add notes
@app.route('/add', methods=['POST'])
def add():
    note = Note(title=request.form['todotitle'], text=request.form['todotext'], complete=False)
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('home'))


# completed task
@app.route('/complete/<int:pk>')
def complete(pk):
    note = Note.query.filter_by(id=pk)
    note.complete = True
    db.session.commit()
    return redirect(url_for('home'))


def delete(pk):
    task_to_delete = Note.query.get_or_404(pk)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return 'There was an error while deleting that task'


def update(pk):
    if request.method == 'POST':
        note = Note(id=pk, title=request.form['todotitle'], text=request.form['todotext'], complete=False)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    db.create_all()
    app.run()  # debug=True
