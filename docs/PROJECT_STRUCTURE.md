# Project Structure

This project is a small Flask application using one main Python file and standard Flask folders for templates and static files.

## Root Files

| Path | Purpose |
| --- | --- |
| `README.md` | Main setup, run, and project overview guide. |
| `requirements.txt` | Python packages needed to run the Flask app. |
| `.gitignore` | Keeps virtual environments, caches, logs, and local files out of git. |
| `.flaskenv` | Optional local Flask environment file. It is ignored by git. |

## Application Files

| Path | Purpose |
| --- | --- |
| `src/main.py` | Flask app setup, SQLAlchemy database setup, `Student` model, and all route functions. |
| `src/db/database.db` | SQLite database used by the app. |
| `src/static/img/hm.jpeg` | Dashboard background image. |
| `src/static/styles/style.css` | Project CSS file. |

## Template Files

| Path | Purpose |
| --- | --- |
| `src/templates/base.html` | Shared layout, navbar, CSS/JS CDN links, and footer. |
| `src/templates/index.html` | Dashboard/home page. |
| `src/templates/students.html` | Displays all student records in a table. |
| `src/templates/add_student.html` | Form for creating a student. |
| `src/templates/edit_student.html` | Form for updating a student. |
| `src/templates/search_student.html` | Displays one searched student. |
| `src/templates/404.html` | Simple not-found page. |

## Recommended Development Structure

Use this layout while working:

```text
student_flaskapp/
├── .venv/                  # local only, ignored by git
├── docs/                   # project documentation
├── src/                    # Flask application
├── README.md
├── requirements.txt
└── .gitignore
```

The current code is intentionally simple. If the app grows, the next clean step would be splitting `src/main.py` into an application package with separate files for routes, models, and configuration.
