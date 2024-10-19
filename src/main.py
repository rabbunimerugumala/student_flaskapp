from flask import Flask,render_template
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

# create a flask app
app = Flask(__name__)

db_path =Path().cwd() / "src/db/database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'+str(db_path)
db = SQLAlchemy(app)

#database models

class Student(db.Model):
    id = db.Column(db.Integer ,primary_key= True )
    first_name = db.Column(db.String(100),nullable= False)



@app.get('/')
def index():
    return render_template("index.html")

@app.get("/students")
def students():
    data = Student.query.all()

    return render_template("students.html",students=data)

@app.get("/add_student")
def add_student():
    return render_template("add_student.html")



# if __name__ == '__main__':
#     app.run(debug=True)
