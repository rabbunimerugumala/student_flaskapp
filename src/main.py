import traceback
from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# create flask app.
app = Flask(__name__)

# ! Giving the path to the data base.
db_path = Path().cwd() / "src/db/database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + str(db_path)
db = SQLAlchemy(app)

#! route to index function
@app.get('/')
def index():
    return render_template("index.html")


# ! database models.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bio = db.Column(db.Text)

# route function to the
@app.get("/students")
def students():
    data = Student.query.all()
    return render_template("students.html", students=data)


@app.route('/add_student/', methods=('GET', 'POST'))
def add_student():
    if request.method == 'POST':
        first_name: str = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        age = int(request.form.get('age'))
        bio = request.form.get('bio', '')
        student = Student(first_name=first_name, last_name=last_name, email=email, age=age, bio=bio)

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add_student.html')


@app.route("/search_student", methods=('GET', 'POST'))
def search_student():
    if request.method == "POST":
        student_id = request.form.get('student_id', '')

        student = Student.query.filter(Student.id == student_id).first()
        # print(student.id)
        return render_template('search_student.html', student=student)

    # return render_template('search_student.html', student=None)
    return render_template('404.html', student=None)
    # return render_template('search_student.html')


@app.route('/edit_student/<int:student_id>', methods=('GET', 'POST'))
def edit_student(student_id):
    student = Student.query.filter(Student.id == student_id).first()
    if request.method == 'POST':
        student.first_name: str = request.form.get('first_name', '')
        student.last_name = request.form.get('last_name', '')
        student.email = request.form.get('email', '')
        student.age = int(request.form.get('age'))
        student.bio = request.form.get('bio', '')
        db.session.commit()
        return redirect(url_for('students'))

    return render_template('edit_student.html', student=student)


@app.post('/delete_student/<int:student_id>')
def delete_student(student_id):
    student = Student.query.filter(Student.id == student_id).first()
    if student is not None:
        db.session.delete(student)
        db.session.commit()

        return redirect(url_for('students'))
    return render_template("404.html")














