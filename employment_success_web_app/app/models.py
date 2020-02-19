from app import db
import datetime

# create a student class, rather than a graduate class - the student class allows for more extendability (e.g. to monitor dropout rate). For the employed and software_job attributes, I've used Booleans, but an extension might be to create choices (e.g. instead of employed we could have an employment_status that might include further study). Also, it may help to add a choice of cohort.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    employed = db.Column(db.Boolean, default = False, nullable=True)
    start_date = db.Column(db.DateTime(), nullable=True)
    software_job = db.Column(db.Boolean, default=False, nullable=True)
    
    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)

# I'm going to attempt to do the calculations within a class (the other option would be to do all the functions in routes.py). I'm not sure how to create a class - use normal python or db.Model?
class Calculator:
    def count_students(self, cohort):
        return len(cohort)

    def count_employed_students(self, cohort):
        employed_students = []
        for student in cohort:
            if student.employed == True:
                employed_students.append(student)
        return len(employed_students)

    def count_students_in_software_jobs(self, cohort):
        students_in_software_jobs = []
        for student in cohort:
            if student.software_job == True:
                students_in_software_jobs.append(student)
        return len(students_in_software_jobs)


    # function to calculate the % of students in employment (could be refactored to make a simple, reusable % calculator)
    def calculate_percentage_of_employed_students(self, cohort):
        employed_students = self.count_employed_students(cohort)
        total_students = self.count_students(cohort)
        percentage = round((employed_students / total_students) * 100, 1)
        return percentage

    # function to calculate the % of students in software role - could be refactored
    def calculate_percentage_in_software_jobs(self, cohort):
        employed_students = self.count_students_in_software_jobs(cohort)
        total_students = self.count_students(cohort)
        percentage = round((employed_students / total_students) * 100, 1)
        return percentage
 