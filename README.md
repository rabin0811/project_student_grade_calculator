# project_student_grade_calculator

## Student Grade Calculator

A Tkinter desktop application that records students, subjects, and marks, calculates grades/averages, and displays results.

- Original location: `D:\Computers Files\work\Student_Grade Calculator`
- Working copy: `D:\PROJECTS_READY\project_student_grade_calculator`
- Stack: Python 3, Tkinter (standard library)

## Folder layout

```text
project_student_grade_calculator/
  scripts/    Student_Grade_Calculator.py
  docs/       Project documentation
```

## Run

```powershell
python scripts\Student_Grade_Calculator.py
```

## Verified status (2026-11-09)

- [x] Script compiled successfully
- [x] Grade/average logic tested
- [x] Tkinter GUI launched successfully
- [ ] No automated test suite

## Notes and limitations

- Desktop GUI only; requires a graphical session.
- Data is held in memory for the session; there is no database.
- Input validation covers subject counts and numeric marks, but this is a learning project rather than a production gradebook.

## Troubleshooting

- **`tkinter` missing**: install the Tk component for your Python distribution (on Windows it is normally included).
- **Window does not open**: run from a desktop session, not a headless terminal.
- **`python` not found**: install Python 3 and ensure it is on `PATH`.
