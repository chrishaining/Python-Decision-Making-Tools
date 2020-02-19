from app import db
from app.models import Student


Student.query.delete()

student = Student(first_name='Bob', last_name="Anderson", employed=True, software_job=True)
db.session.add(student)
db.session.commit()


students = Student.query.all()

student = Student.query.get(1)

db.session.commit()

print(students)
print(student)
print(student.start_date)
print(student.employed)
print(student.software_job)