# Database Guide

The app uses SQLite through Flask-SQLAlchemy.

## Database Location

```text
src/db/database.db
```

In `src/main.py`, the path is built from the location of `main.py`, so the app can run from the project root without depending on a hard-coded absolute path.

## Table

SQLAlchemy creates one table from the `Student` model.

| Column | Type | Required | Notes |
| --- | --- | --- | --- |
| `id` | Integer | Yes | Primary key. |
| `first_name` | String(100) | Yes | Student first name. |
| `last_name` | String(100) | Yes | Student last name. |
| `email` | String(80) | Yes | Must be unique. |
| `age` | Integer | No | Student age. |
| `created_at` | DateTime | No | Filled automatically by the database. |
| `bio` | Text | No | Extra information about the student. |

## How Data Is Created

1. User opens `/add_student/`.
2. User submits the form.
3. Flask reads form values from `request.form`.
4. The app creates a `Student(...)` object.
5. `db.session.add(student)` stages the record.
6. `db.session.commit()` saves it into SQLite.

## How Data Is Read

- `/students` reads all students with `Student.query.order_by(Student.id.desc()).all()`.
- `/search_student` reads one student by submitted ID.
- `/edit_student/<student_id>` loads one student before showing the edit form.

## How Data Is Updated

1. User opens `/edit_student/<student_id>`.
2. The existing student is loaded from the database.
3. User submits new form values.
4. The route updates the model fields.
5. `db.session.commit()` saves the changes.

## How Data Is Deleted

1. A POST request is sent to `/delete_student/<student_id>`.
2. The student is loaded by ID.
3. `db.session.delete(student)` marks it for deletion.
4. `db.session.commit()` removes it from SQLite.

## Recreating the Database

For a local reset:

1. Stop the Flask server.
2. Back up `src/db/database.db` if the data is important.
3. Delete `src/db/database.db`.
4. Start the Flask app again.

The app calls `db.create_all()` on startup, so the table is recreated automatically.
