# Routes Guide

All routes are defined in `src/main.py`.

| Route | Method | Function | Purpose |
| --- | --- | --- | --- |
| `/` | GET | `index` | Shows the dashboard page. |
| `/students` | GET | `students` | Shows all student records. |
| `/add_student/` | GET | `add_student` | Shows the add student form. |
| `/add_student/` | POST | `add_student` | Saves a new student. |
| `/search_student` | POST | `search_student` | Searches for one student by ID from the navbar search form. |
| `/edit_student/<student_id>` | GET | `edit_student` | Shows the edit form for one student. |
| `/edit_student/<student_id>` | POST | `edit_student` | Updates one student. |
| `/delete_student/<student_id>` | POST | `delete_student` | Deletes one student. |

## Template Flow

| Action | Template |
| --- | --- |
| Dashboard | `index.html` |
| List students | `students.html` |
| Add student | `add_student.html` |
| Edit student | `edit_student.html` |
| Search result | `search_student.html` |
| Missing student | `404.html` |

## Important Notes

- HTML forms only submit GET and POST in this app, so edit and delete actions use POST.
- The search form expects a numeric student ID.
- If a student is not found, Flask returns the not-found page.
