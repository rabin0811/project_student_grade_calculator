# Student Grade Calculator — Technical Notes

## Overview

A Tkinter desktop application that records students, subjects, and marks, calculates grades and averages, and displays results.

## Folder structure

```text
scripts/
  Student_Grade_Calculator.py    Runnable application
archive/
  Student_Grade Calculator/      Original archive copy
docs/
  Assignment brief PDF
  Student report and supporting documents
  Draw.io program-flow diagram
```

## Run

```powershell
python scripts\Student_Grade_Calculator.py
```

## How it works

1. Enter the number of students and subjects.
2. Enter each student's name and marks.
3. The app calculates totals, averages, and grades.
4. Results are displayed in the Tkinter interface.

## Verification evidence (2026-11-09)

| Check | Result |
|---|---|
| Python compile | Passed |
| Grade/average logic | Tested |
| Tkinter GUI | Launched successfully |
| Automated tests | None |

## Limitations

- Desktop GUI only; requires a graphical session.
- Data is held in memory for the session; there is no database.
- Input validation is basic and intended for coursework use.
- The archive copy is preserved for reference; use `scripts/Student_Grade_Calculator.py` as the entry point.
