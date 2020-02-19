from app import app, db
from app.models import Student
from flask import render_template, request, redirect
import datetime

@app.route('/')
def index():
    # return "Welcome to this stat app!"
    return render_template('index.html', title='Home')

@app.route('/students')
def show_students(): # MODIFIED
    students = Student.query.all()
    return render_template('students.html', title='Students', students=students)

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

