from app import db
from app.models import Student, Cohort

Cohort.query.delete()
Student.query.delete()


cohort = Cohort(cohort_name="Alpha",)
db.session.add(cohort)
db.session.commit()

student = Student(first_name='Bob', last_name="Anderson", employed=True, software_job=True, cohort=cohort)
db.session.add(student)
student2 = Student(first_name='Jenny', last_name="Cashew", employed=True, software_job=False, cohort=cohort)
db.session.add(student2)

db.session.commit()


students = Student.query.all()

student = Student.query.get(1)
cohort = Cohort.query.get(1)

db.session.commit()

print(students)
print(student)
print(student.start_date)
print(student.employed)
print(student.software_job)
print(student.cohort)
print(cohort)
print(cohort.students[0])
print(cohort.students[1])


# type_of_structure = type(cohort.students)
# print(type_of_structure)
# type_of_structure2 = type(cohort.students[0])
# print(type_of_structure2)
# students = Student.query.all()
# print(students)
# student_cohort = Student.query.get(1).cohort
# print(student_cohort)
