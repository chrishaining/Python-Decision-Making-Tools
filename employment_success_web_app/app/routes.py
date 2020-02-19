from app import app
from app.models import Student
from flask import render_template

@app.route('/')
def index():
    # return "Welcome to this stat app!"
    return render_template('index.html', title='Home')

@app.route('/students')
def show_students(): # MODIFIED
    students = Student.query.all()
    return render_template('students.html', title='Students', students=students)