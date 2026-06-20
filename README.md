# Student Management Flask App

A simple student management web application built with Flask, Jinja templates, Bootstrap, Flask-SQLAlchemy, and SQLite.

The app lets team members:

- View the dashboard page.
- Add a student.
- List all students.
- Search one student by ID.
- Edit a student record.
- Delete a student record.

## Tech Stack

- Python 3.12 recommended
- Flask 3
- Flask-SQLAlchemy
- SQLite database
- Jinja2 templates
- Bootstrap 5, Bootstrap Icons, and Font Awesome from CDN
- CSS from `src/static/styles/style.css`

## Project Structure

```text
Student-Management-Flask-App/
|-- README.md
|-- requirements.txt
|-- docs/
|   |-- DATABASE.md
|   |-- PROJECT_STRUCTURE.md
|   `-- ROUTES.md
`-- src/
    |-- main.py
    |-- db/
    |   `-- database.db
    |-- static/
    |   |-- img/
    |   |   `-- hm.jpeg
    |   `-- styles/
    |       `-- style.css
    `-- templates/
        |-- 404.html
        |-- add_student.html
        |-- base.html
        |-- edit_student.html
        |-- index.html
        |-- search_student.html
        `-- students.html
```

## Clone the Project

```powershell
git clone <repository-url>
cd student_flaskapp
```

Replace `<repository-url>` with the real GitHub/GitLab repository URL.

## Create a Virtual Environment

Use a fresh virtual environment. Do not use or commit `myenv/`, `venv/`, or `.venv/`.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows Command Prompt:

```bat
python -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

To deactivate the environment:

```powershell
deactivate
```

## Run the Flask App

You can run the project in two simple ways.

### Option 1: Run Directly With `--app`

From the project root:

```powershell
flask --app src.main run --debug
```

Open this URL in the browser:

```text
http://127.0.0.1:5000
```

Alternative run command:

```powershell
python -m flask --app src.main run --debug
```

### Option 2: Run With `.flaskenv`

The project can also use a `.flaskenv` file so you do not need to type `--app src.main` every time.

Create a `.flaskenv` file in the project root:

```text
FLASK_APP=src.main
FLASK_DEBUG=True
```

For Windows PowerShell, your local run flow becomes:

```powershell
cd C:\Users\rabbu\OneDrive\Documents\coding\flask_projects\student_flaskapp
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask run
```

For Windows Command Prompt:

```bat
cd C:\Users\rabbu\OneDrive\Documents\coding\flask_projects\student_flaskapp
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
flask run
```

For macOS/Linux:

```bash
cd student_flaskapp
source .venv/bin/activate
pip install -r requirements.txt
flask run
```

After running `flask run`, open:

```text
http://127.0.0.1:5000
```

If `flask run` does not detect `.flaskenv`, make sure `python-dotenv` is installed:

```powershell
pip install python-dotenv
```

`python-dotenv` is already included in `requirements.txt`, so normally `pip install -r requirements.txt` is enough.

## Fast Local Run Commands

Use these commands when you want to run the app quickly on your local machine.

First time setup:

```powershell
cd C:\Users\rabbu\OneDrive\Documents\coding\flask_projects\student_flaskapp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
flask run
```

Everyday run after setup:

```powershell
cd C:\Users\rabbu\OneDrive\Documents\coding\flask_projects\student_flaskapp
.\.venv\Scripts\Activate.ps1
flask run
```

If `python -m venv .venv` does not work, check which Python commands are available:

```powershell
python --version
py -0
```

Then create the virtual environment with one of these commands:

```powershell
python -m venv .venv
py -3.11 -m venv .venv
py -3.12 -m venv .venv
```

Use `py -3.12 -m venv .venv` only when Python 3.12 is installed. If you see `No suitable Python runtime found`, use `python -m venv .venv` or install Python from https://www.python.org/downloads/.

## Database Setup

The app uses SQLite at:

```text
src/db/database.db
```

The `Student` model is defined in `src/main.py`. When the Flask app starts, `db.create_all()` creates the required table if it does not already exist.

Main columns:

- `id`: primary key
- `first_name`: required
- `last_name`: required
- `email`: required and unique
- `age`: integer
- `created_at`: created timestamp
- `bio`: text

More details are in [docs/DATABASE.md](docs/DATABASE.md).

## Main Pages

- `/` - dashboard
- `/students` - all students
- `/add_student/` - add student form
- `/search_student` - search result page after submitting the navbar search form
- `/edit_student/<student_id>` - edit one student
- `/delete_student/<student_id>` - delete one student using POST

More details are in [docs/ROUTES.md](docs/ROUTES.md).

## Common Problems

If `flask` is not recognized, activate the virtual environment and install dependencies again:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

If the database has old test data, stop the server, back up `src/db/database.db` if needed, then remove the database file. Start the app again and Flask-SQLAlchemy will recreate the table.

## Team Notes

- Commit source code, templates, static assets, documentation, and `requirements.txt`.
- Do not commit virtual environments such as `.venv/`, `venv/`, or `myenv/`.
- Keep database changes intentional because `src/db/database.db` is currently tracked as the sample SQLite database for this project.

