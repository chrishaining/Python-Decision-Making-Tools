from app import app, db
from app.models import Student, Calculator
from flask import render_template, request, redirect
import datetime

@app.route('/')
def index():
    # return "Welcome to this stat app!"
    return render_template('index.html', title='Home')

@app.route('/students')
def show_students(): # MODIFIED
    students = Student.query.all()
    calculator = Calculator()
    number_of_students = calculator.count_students(students)
    employed_students = calculator.count_employed_students(students)
    students_in_software_jobs = calculator.count_students_in_software_jobs(students)
    percentage_of_employed_students = calculator.calculate_percentage_of_employed_students(students)
    percentage_in_software_jobs = calculator.calculate_percentage_in_software_jobs(students)
    return render_template('students.html', title='Students', students=students, number_of_students=number_of_students, employed_students=employed_students,
    students_in_software_jobs=students_in_software_jobs, percentage_of_employed_students=percentage_of_employed_students, percentage_in_software_jobs=percentage_in_software_jobs)

    
     





# function to add a student
@app.route('/students', methods=['POST'])
def create():
    studentFirstName = request.form['first_name']
    studentLastName = request.form['last_name']
    # studentEmployed = request.form['employed'] disabled until I can work out how to use booleans with forms
    # studentStartDate = request.form['start_date']
    studentStartDate = datetime.datetime(2019, 12, 12) # having to cheat as I haven't yet figured out how to add datetime in a form

    # studentSoftwareJob = request.form['software_job'] disabled until I can work out how to use booleans with forms
    # newStudent = Student(first_name=studentFirstName, last_name=studentLastName, employed=studentEmployed, start_date=studentStartDate, software_job=studentSoftwareJob)
    newStudent = Student(first_name=studentFirstName, last_name=studentLastName, start_date=studentStartDate)
    db.session.add(newStudent)
    db.session.commit()
    return redirect('/students')

# function to count students
# @app.route('/students', methods=['GET'])
# def count():
#     calculator = Calculator()
#     students = Student.query.all()
#     number_of_students = calculator.count_students(students)
#     return render_template('students.html', title='Students', students=students, number_of_students=number_of_students)
