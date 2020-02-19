from app import db
import datetime

# create a student class, rather than a graduate class - the student class allows for more extendability (e.g. to monitor dropout rate). For the employed and software_job attributes, I've used Booleans, but an extension might be to create choices (e.g. instead of employed we could have an employment_status that might include further study). Also, it may help to add a choice of cohort.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64), index=True)
    employed = db.Column(db.Boolean, default = False, nullable=True)
    start_date = db.Column(db.DateTime(), nullable=True)
    software_job = db.Column(db.Boolean, default=False, nullable=True)
    
    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)
