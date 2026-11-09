import tkinter as tk
from tkinter import ttk, messagebox


class StudentGradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Calculator")
        self.root.geometry("900x700")

        self.students = []
        self.current_subjects = {}

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Student Grade Calculator",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        form = tk.Frame(self.root)
        form.pack(pady=5)

        tk.Label(form, text="Student Name").grid(
            row=0, column=0, sticky="w"
        )
        self.student_name = tk.Entry(form, width=30)
        self.student_name.grid(row=0, column=1)

        tk.Label(form, text="Course Name").grid(
            row=1, column=0, sticky="w"
        )
        self.course_name = tk.Entry(form, width=30)
        self.course_name.grid(row=1, column=1)

        tk.Label(form, text="Number of Subjects (1-10)").grid(
            row=2, column=0, sticky="w"
        )
        self.subject_count = tk.Entry(form, width=10)
        self.subject_count.grid(row=2, column=1, sticky="w")

        tk.Label(form, text="Subject Name").grid(
            row=3, column=0, sticky="w"
        )
        self.subject_name = tk.Entry(form, width=30)
        self.subject_name.grid(row=3, column=1)

        tk.Label(form, text="Mark").grid(
            row=4, column=0, sticky="w"
        )
        self.subject_mark = tk.Entry(form, width=10)
        self.subject_mark.grid(row=4, column=1, sticky="w")

        tk.Button(
            form,
            text="Add Subject",
            command=self.add_subject
        ).grid(row=5, column=0, columnspan=2, pady=5)

        self.tree = ttk.Treeview(
            self.root,
            columns=("Subject", "Mark"),
            show="headings",
            height=8
        )

        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Mark", text="Mark")

        self.tree.column("Subject", width=300)
        self.tree.column("Mark", width=150)

        self.tree.pack(fill="x", padx=20, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(
            btn_frame,
            text="Calculate Result",
            command=self.calculate_result
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Save Student",
            command=self.save_student
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="Clear Form",
            command=self.clear_form
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            btn_frame,
            text="Summary Report",
            command=self.summary_report
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            btn_frame,
            text="Exit",
            command=self.root.destroy
        ).grid(row=0, column=4, padx=5)

        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold")
        )
        self.result_label.pack(pady=10)

        self.feedback_label = tk.Label(
            self.root,
            text="",
            wraplength=700,
            justify="left"
        )
        self.feedback_label.pack(pady=10)

    def get_grade(self, avg):
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        return "Fail"

    def get_feedback(self, name, grade):
        if grade in ["A", "B"]:
            return f"Congratulations, {name}! Excellent work."
        elif grade in ["C", "D"]:
            return f"Good effort, {name}! Keep improving."
        return (
            f"Don't be discouraged, {name}. "
            f"Practice and revision will help you improve."
        )

    def add_subject(self):
        try:
            count = int(self.subject_count.get())

            if not 1 <= count <= 10:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter a valid subject count (1-10) first."
            )
            return

        if len(self.current_subjects) >= count:
            messagebox.showerror(
                "Error",
                f"You can only add {count} subjects."
            )
            return

        subject = self.subject_name.get().strip()
        mark_text = self.subject_mark.get().strip()

        if not subject:
            messagebox.showerror(
                "Error",
                "Subject name cannot be empty."
            )
            return

        if any(
            s.lower() == subject.lower()
            for s in self.current_subjects
        ):
            messagebox.showerror(
                "Error",
                "Duplicate subject name."
            )
            return

        try:
            mark = float(mark_text)

            if not 0 <= mark <= 100:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Mark must be between 0 and 100."
            )
            return

        self.current_subjects[subject] = mark

        self.tree.insert(
            "",
            "end",
            values=(subject, mark)
        )

        self.subject_name.delete(0, tk.END)
        self.subject_mark.delete(0, tk.END)

    def calculate_result(self):
        if not self.current_subjects:
            messagebox.showerror(
                "Error",
                "Add at least one subject."
            )
            return

        avg = (
            sum(self.current_subjects.values())
            / len(self.current_subjects)
        )

        grade = self.get_grade(avg)

        self.result_label.config(
            text=f"Average: {avg:.2f}%   Grade: {grade}"
        )

        self.feedback_label.config(
            text=self.get_feedback(
                self.student_name.get().strip(),
                grade
            )
        )

    def save_student(self):
        name = self.student_name.get().strip()
        course = self.course_name.get().strip()

        if not name:
            messagebox.showerror(
                "Error",
                "Student name required."
            )
            return

        if not all(
            ch.isalpha() or ch.isspace()
            for ch in name
        ):
            messagebox.showerror(
                "Error",
                "Name should contain letters only."
            )
            return

        if not course:
            messagebox.showerror(
                "Error",
                "Course name required."
            )
            return

        if any(ch.isdigit() for ch in course):
            messagebox.showerror(
                "Error",
                "Course name cannot contain numbers."
            )
            return

        try:
            count = int(self.subject_count.get())

            if not 1 <= count <= 10:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Subject count must be between 1 and 10."
            )
            return

        if len(self.current_subjects) != count:
            messagebox.showerror(
                "Error",
                f"You specified {count} subjects "
                f"but added {len(self.current_subjects)}."
            )
            return

        avg = (
            sum(self.current_subjects.values())
            / len(self.current_subjects)
        )

        grade = self.get_grade(avg)

        status = "Pass" if avg >= 40 else "Fail"

        self.students.append({
            "name": name,
            "course": course,
            "modules": dict(self.current_subjects),
            "average": avg,
            "grade": grade,
            "status": status
        })

        messagebox.showinfo(
            "Success",
            f"{name} added successfully.\n\n"
            f"Average: {avg:.2f}%\n"
            f"Grade: {grade}\n"
            f"Status: {status}"
        )

        self.clear_form()

    def clear_form(self):
        self.student_name.delete(0, tk.END)
        self.course_name.delete(0, tk.END)
        self.subject_count.delete(0, tk.END)
        self.subject_name.delete(0, tk.END)
        self.subject_mark.delete(0, tk.END)

        self.current_subjects.clear()

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.result_label.config(text="")
        self.feedback_label.config(text="")

    def summary_report(self):
        if not self.students:
            messagebox.showinfo(
                "Report",
                "No student records available."
            )
            return

        report = tk.Toplevel(self.root)
        report.title("Summary Report")
        report.geometry("800x500")

        frame = tk.Frame(report)
        frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        text = tk.Text(
            frame,
            yscrollcommand=scrollbar.set
        )
        text.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(command=text.yview)

        class_avg = (
            sum(s["average"] for s in self.students)
            / len(self.students)
        )

        highest = max(
            self.students,
            key=lambda s: s["average"]
        )

        lowest = min(
            self.students,
            key=lambda s: s["average"]
        )

        text.insert(
            "end",
            "STUDENT GRADE REPORT\n\n"
        )

        text.insert(
            "end",
            f"Total Students: {len(self.students)}\n\n"
        )

        for s in sorted(
            self.students,
            key=lambda x: x["average"],
            reverse=True
        ):
            text.insert(
                "end",
                f"Name: {s['name']}\n"
            )

            text.insert(
                "end",
                f"Course: {s['course']}\n"
            )

            text.insert(
                "end",
                "Subjects:\n"
            )

            for sub, mark in s["modules"].items():
                text.insert(
                    "end",
                    f"   {sub}: {mark}\n"
                )

            text.insert(
                "end",
                f"Average: {s['average']:.2f}%\n"
            )

            text.insert(
                "end",
                f"Grade: {s['grade']}\n"
            )

            text.insert(
                "end",
                f"Status: {s['status']}\n"
            )

            text.insert(
                "end",
                "-" * 50 + "\n"
            )

        text.insert(
            "end",
            "\nCLASS STATISTICS\n"
        )

        text.insert(
            "end",
            f"Class Average: {class_avg:.2f}%\n"
        )

        text.insert(
            "end",
            f"Highest Student: "
            f"{highest['name']} "
            f"({highest['average']:.2f}%)\n"
        )

        text.insert(
            "end",
            f"Lowest Student: "
            f"{lowest['name']} "
            f"({lowest['average']:.2f}%)\n"
        )

        text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGradeCalculator(root)
    root.mainloop()