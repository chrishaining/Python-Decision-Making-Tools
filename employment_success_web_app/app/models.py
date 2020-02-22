from app import db
import datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np 
from PIL import Image

import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from app.part_of_speech import get_part_of_speech

# create a cohort class. this will have an ID, graduation date, and list of students (many students to one cohort). I can also give it a name, though this isn't vital (I could use the id as a sort of name)
class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cohort_name = db.Column(db.String(64), index=True, nullable=False)
    graduation_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow, nullable=True)
    students = db.relationship('Student', backref='cohort', lazy='dynamic')
    surveys = db.relationship('Survey', backref='cohort', lazy='dynamic')


    def __repr__(self):
        return '<Cohort {}>'.format(self.cohort_name)

# create a student class, rather than a graduate class - the student class allows for more extendability (e.g. to monitor dropout rate). For the employed and software_job attributes, I've used Booleans, but an extension might be to create choices (e.g. instead of employed we could have an employment_status that might include further study). Also, it may help to add a choice of cohort.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), index=True, nullable=True)
    employed = db.Column(db.Boolean, default = False, nullable=True)
    start_date = db.Column(db.DateTime(), nullable=True)
    software_job = db.Column(db.Boolean, default=False, nullable=True)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohort.id'))
    
    def __repr__(self):
        return '<Student {} {}>'.format(self.first_name, self.last_name)

# create a survey class. It has a cohort.id foreign key - I chose this over student.id as a survey should be anonymous, though the counter-argument is that now multiple surveys for the same student could be used.
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_one = db.Column(db.String(64), index=True, nullable=True)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohort.id'))
    
    def __repr__(self):
        return '<Survey {}>'.format(self.question_one)

    def count_words(self):
        text_to_read = self.question_one.lower()
        cleaned = re.sub('\W+', ' ', text_to_read)
        tokenized = word_tokenize(cleaned)
        stop_words = stopwords.words('english')
        filtered = [word for word in tokenized if word not in stop_words]
        normalizer = WordNetLemmatizer()
        normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
        bag_of_looking_glass_words = Counter(normalized)
        return bag_of_looking_glass_words.items()

    # def display_count_words(self):
    #     words = self.count_words()
    #     for word, frequency in words:

    #     split_words = ["{}: {}".format(word, frequency) for word, frequency in words.items()]
    #     for key, value in words.items():
    #         return "{}{}".format(key, value)
    #     return "{}{}".format(words.keys(), words.values())
    #     return split_words

      

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
 
    #  function to display students in a bar graph
    def bar_graph_of_employed_status(self, cohort):
        employed_students = self.count_employed_students(cohort)
        not_employed = self.count_students(cohort) - employed_students
        numbers = [employed_students, not_employed]
        titles = ["employed", "not employed"]
        x_values= range(2)
        plt.bar(x_values, numbers)
        ax = plt.subplot()
        length = len(x_values)
        ax.set_xticks(range(length))
        ax.set_xticklabels(titles)
        chart = plt.savefig('chart.png')
        return chart

# five-number summary

#  //////
# def calculate_average_days_to_get_software_job(self, cohort):
#     graduation_date = cohort["graduation_date"]
#     differences = []
#     for student in cohort["students"]:
#         if student["software_job"] == True:
#             difference = student["start_date"] - graduation_date
#             differences.append(difference)
#     average_days = np.mean(differences).days
#     return average_days

#     # return graduation_month.strftime("%B")


# # try to calculate average months to get software job

# def calculate_average_months_to_get_software_job(self, cohort):
#     graduation_date = cohort["graduation_date"]
#     differences = []
#     for student in cohort["students"]:
#         if student["software_job"] == True:
#             difference = relativedelta.relativedelta(student["start_date"], graduation_date)
#             differences.append(difference.months)
#     average_months = np.mean(differences)
#     adjusted_months = round(average_months, 1)
#     return adjusted_months

# # function to calculate the % of students in software role after 1 month.
# # function to calculate the % of students in software role after 3 months.
# # function to calculate the % of students in software role after 6 months.
# # These are actually the same function, but using a different argument.
# def calculate_percentage_of_students_in_software_role(self, cohort, months_after_graduation):
#     employed_graduates = []
#     graduates = count_cohort_graduates(cohort)
#     graduation_date = cohort["graduation_date"]
#     for student in cohort["students"]:
#         if student["software_job"] == True:
#             difference = relativedelta.relativedelta(student["start_date"], graduation_date)
#             if difference.months <= months_after_graduation:
#                 employed_graduates.append(student)
#     percentage = (len(employed_graduates) / graduates) * 100
#     return percentage



# # function to calculate the % of students who do not get a software role. 
    def calculate_percentage_of_students_not_in_software_role(self, cohort):
        non_software_students = []
        total_students = self.count_students(cohort)
        for student in cohort:
            if student.software_job == False:
                non_software_students.append(student)
        percentage = round((len(non_software_students) / total_students) * 100, 1)
        return percentage

# create a survey reader



class SurveyReader:
    # def create_word_cloud(self):
        # maskArray = np.array(Image.open("cloud.png"))
        # maskArray = Image.open("templates/index.html")
        # text1 = open("iliad.txt", "r").read().lower()
        # text1 = open("survey.txt", "r").read().lower()
        # cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
        # return cloud.generate(text1)
        # return maskArray
        # clean_title = title.replace(" ", "")
        # cloud.to_file("%swordCloud.png" % clean_title)

    # importing regex and nltk


# import the text
    def word_count(self, survey):
        text_to_read = survey.question_one
        text1 = open(text_to_read, encoding='utf-8').read().lower()
        cleaned = re.sub('\W+', ' ', text1).lower()
        tokenized = word_tokenize(cleaned)
        stop_words = stopwords.words('english')
        filtered = [word for word in tokenized if word not in stop_words]
        normalizer = WordNetLemmatizer()
        normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
        bag_of_looking_glass_words = Counter(normalized)
        return bag_of_looking_glass_words