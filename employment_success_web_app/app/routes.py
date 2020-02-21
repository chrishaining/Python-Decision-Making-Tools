from app import app, db
from app.models import Student, Calculator, SurveyReader
from flask import render_template, request, redirect
import datetime

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/students')
def show_students(): 
    students = Student.query.all()
    # calculator = Calculator()
    # number_of_students = calculator.count_students(students)
    # employed_students = calculator.count_employed_students(students)
    # students_in_software_jobs = calculator.count_students_in_software_jobs(students)
    # percentage_of_employed_students = calculator.calculate_percentage_of_employed_students(students)
    # percentage_in_software_jobs = calculator.calculate_percentage_in_software_jobs(students)
    # non_software = calculator.calculate_percentage_of_students_not_in_software_role(students)
    return render_template('students.html', title='Students', students=students) 
    
    # number_of_students=number_of_students, employed_students=employed_students,
    # students_in_software_jobs=students_in_software_jobs, percentage_of_employed_students=percentage_of_employed_students, percentage_in_software_jobs=percentage_in_software_jobs, non_software=non_software)

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

# function to edit a student
@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    student_to_edit = Student.query.get(student_id)
    db.session.update(student_to_edit)
    db.session.commit()
    return redirect('/students')

# function to delete a student
@app.route('/students/<int:student_id>/delete', methods=['POST'])
def delete_student(student_id):
    student_to_delete = Student.query.get(student_id)
    db.session.delete(student_to_delete)
    db.session.commit()
    return redirect('/students')


@app.route('/statistics')
def show_statistics(): 
    students = Student.query.all()
    calculator = Calculator()
    number_of_students = calculator.count_students(students)
    employed_students = calculator.count_employed_students(students)
    students_in_software_jobs = calculator.count_students_in_software_jobs(students)
    percentage_of_employed_students = calculator.calculate_percentage_of_employed_students(students)
    percentage_in_software_jobs = calculator.calculate_percentage_in_software_jobs(students)
    non_software = calculator.calculate_percentage_of_students_not_in_software_role(students)
    # employed_graph = calculator.bar_graph_of_employed_status(students)
    return render_template('statistics.html', title='Statistics', students=students, number_of_students=number_of_students, employed_students=employed_students,
    students_in_software_jobs=students_in_software_jobs, percentage_of_employed_students=percentage_of_employed_students, percentage_in_software_jobs=percentage_in_software_jobs, non_software=non_software)
    # employed_graph=employed_graph

@app.route('/surveys')
def show_surveys(): 
    # text2 = "I am a little fish. I love to eat maggots. And other fish. Mmm - maggots. Also, flies and algae."
    surveyReader = SurveyReader()
    survey = "I am a little fish. I love to eat maggots. And other fish. Mmm - maggots. Also, flies and algae."
    word_count = surveyReader.word_count(survey)
    return render_template('surveys.html', title='Surveys', survey=survey, word_count=word_count)