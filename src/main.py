from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy.sql import func

app = Flask(__name__)

# Keep the database path relative to this file so the app works from any terminal location.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db" / "database.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH.as_posix()}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.get('/')
def index():
    """Show the application dashboard page."""
    return render_template("index.html")


class Student(db.Model):
    """Student table used by the CRUD screens."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bio = db.Column(db.Text)


with app.app_context():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db.create_all()


@app.get("/students")
def students():
    """Display all student records."""
    data = Student.query.order_by(Student.id.desc()).all()
    return render_template("students.html", students=data)


@app.route('/add_student/', methods=('GET', 'POST'))
def add_student():
    """Create a new student from the add-student form."""
    if request.method == 'POST':
        first_name: str = request.form.get('first_name', '').strip()
        last_name: str = request.form.get('last_name', '').strip()
        email: str = request.form.get('email', '').strip()
        age = int(request.form.get('age', 0))
        bio: str = request.form.get('bio', '').strip()

        student = Student(first_name=first_name, last_name=last_name, email=email, age=age, bio=bio)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add_student.html')


@app.route("/search_student", methods=('GET', 'POST'))
def search_student():
    """Find students by ID, roll number, first name, last name, or full name."""
    if request.method == "POST":
        query = request.form.get('query') or request.form.get('student_id', '')
        query = query.strip()

        if not query:
            return render_template(
                'search_student.html',
                students=[],
                query=query,
                message='Please enter a student name, ID, or roll number.',
            )

        roll_prefix = '21030-EE-'
        id_query = query[len(roll_prefix):] if query.upper().startswith(roll_prefix) else query
        students = []

        if id_query.isdigit():
            student = Student.query.filter_by(id=int(id_query)).first()
            if student:
                students = [student]
        else:
            name_query = f'%{query}%'
            students = Student.query.filter(
                or_(
                    Student.first_name.ilike(name_query),
                    Student.last_name.ilike(name_query),
                    (Student.first_name + ' ' + Student.last_name).ilike(name_query),
                    Student.email.ilike(name_query),
                )
            ).order_by(Student.id.desc()).all()

        if not students:
            return render_template(
                'search_student.html',
                students=[],
                query=query,
                message=f'No student found for "{query}".',
            )

        return render_template('search_student.html', students=students, query=query, message=None)

    return render_template('search_student.html', students=[], query='', message=None)


# Flask forms can submit only GET/POST directly, so this route uses POST for updates.
@app.route('/edit_student/<int:student_id>', methods=('GET', 'POST'))
def edit_student(student_id):
    """Edit an existing student record."""
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        student.first_name = request.form.get('first_name', '').strip()
        student.last_name = request.form.get('last_name', '').strip()
        student.email = request.form.get('email', '').strip()
        student.age = int(request.form.get('age', 0))
        student.bio = request.form.get('bio', '').strip()
        db.session.commit()
        return redirect(url_for('students'))

    return render_template('edit_student.html', student=student)


@app.post('/delete_student/<int:student_id>')
def delete_student(student_id):
    """Delete a student record from the list page."""
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()

    return redirect(url_for('students'))
