from flask import Flask, request, render_template, json, url_for, redirect
from Flask_Bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'sfjhvdfbhvbkjsdbjbnjhuhrgbiut'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@app.route('/users', methods=['GET'])
def list_user():
    users = db.session.query(User).all()
    return render_template("user/list_user.html", users=users)


@app.route('/user/<int:pk>', methods=['POST', 'GET'])
def update_user(pk):
    user = db.session.query(User).get(pk)
    if request.method == "GET":
        return render_template("user/update_user.html", user=user)
    if request.method == "POST":
        if not user.name == request.form["name"]:
            user.name = request.form["name"]
        if not user.email == request.form["email"]:
            user.email = request.form["email"]
        if not user.password == request.form["password"]:
            user.password = request.form["password"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list_user'))


@app.route('/user', methods=['POST', 'GET'])
def add_user():
    if request.method == "GET":
        return render_template("user/add_user.html")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list_user'))


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/add/<name>')
def hello_add(name):
    return f'Hello, {name} ADD!'


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    s = a + b
    return f'a+b={s}'


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    # return request.method
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        print(request.content_type)

        if request.content_type == "application/x-www-form-urlencoded":
            a = int(request.form["a"])
            b = int(request.form["b"])
            s = a + b
            return f'{a=} {b=} a+b={s}'

        if request.content_type == "application/json":
            data = json.loads(request.get_data())

            return str(eval(f"{data['a']}{data['operator']}{data['b']}"))


if __name__ == '__main__':
    db.create_all()

    app.run()
