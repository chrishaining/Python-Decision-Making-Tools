# the program uses dates so import datetime package. also import relativedata to calculate the number of months between two dates
import datetime
from dateutil import relativedelta

# I'll be using averages, so import numpy
import numpy as np

# how to create a date: x = datetime.datetime(2020, 5, 17)



# CREATING OUR OBJECTS
# create students. This could be as simple objects, or as instances of Student class.
# methodological decision: how to calculate when their employment started? Do we use the date they got a job offer, or the date they started? I will choose start date, as this gives a better reflection of the true cost to a student/potential student (that is, it says how long they were unemployed and without a salary.) I also don't know the exact start dates, so will use a standard day for each. This could be either first day, last day or middle day of month. Since CodeClan finished 15th November, I will use 15th as the date. If the personal is not employed, how will I deal with the start_date? I'll try using None
student1 = {
    "name": "student1",
    "employed": True,
    "start_date": datetime.datetime(2019, 11, 15),
    "software_job": True
}

student2 = {
    "name": "student2",
    "employed": False,
    "start_date": None,
    "software_job": False

}
print(student2)
print(student2["start_date"])

student3 = {
    "name": "student3",
    "employed": True,
    "start_date": datetime.datetime(2020, 1, 15),
    "software_job": True
}

student4 = {
    "name": "student4",
    "employed": True,
    "start_date": datetime.datetime(2020, 2, 15),
    "software_job": True
}

student5 = {
    "name": "student5",
    "employed": True,
    "start_date": datetime.datetime(2020, 3, 15),
    "software_job": False
}

# print(student1["name"])
# print(student1["employed"])
# print(student1["start_date"])
# create list/dictionary of students. could be a simple list/dictionary, or a Cohort class.
cohort1 = {
    "students": [student1, student2, student3, student4, student5],
    "graduation_date": datetime.datetime(2019, 11, 15)

}
print(cohort1)
print(cohort1["students"][4]["employed"])
print(cohort1["students"][1]["employed"])
print(cohort1["students"][1]["start_date"])


# FUNCTIONS
# methodology issue: do we count students who self-excluded themselves from software jobs?

# EXTENSION: function to count the number of students who completed the course (drop-out rate would be useful if we were extending this to multiple cohorts). 
def count_cohort_graduates(cohort):
    return len(cohort["students"])
print(count_cohort_graduates(cohort1))

# EXTENSION: function to count the drop-out rate

# function to count the number of students in employment
def count_employed_graduates(cohort):
    employed_graduates = []
    for graduate in cohort["students"]:
        if graduate["employed"] == True:
            employed_graduates.append(graduate)
    return len(employed_graduates)

print(count_employed_graduates(cohort1))

# function to count the number of students in software role
def count_graduates_in_software_jobs(cohort):
    graduates_in_software_jobs = []
    for graduate in cohort["students"]:
        if graduate["software_job"] == True:
            graduates_in_software_jobs.append(graduate)
    return len(graduates_in_software_jobs)

print(count_graduates_in_software_jobs(cohort1)) #expect 3

# function to calculate the % of students in employment (could be refactored to make a simple, reusable % calculator)
def calculate_percentage_of_employed_graduates(cohort):
    employed_graduates = count_employed_graduates(cohort)
    graduates = count_cohort_graduates(cohort)
    percentage = (employed_graduates / graduates) * 100
    return percentage

print(calculate_percentage_of_employed_graduates(cohort1)) # expect 80

# function to calculate the % of students in software role - could be refactored
def calculate_percentage_in_software_jobs(cohort):
    employed_graduates = count_graduates_in_software_jobs(cohort)
    graduates = count_cohort_graduates(cohort)
    percentage = (employed_graduates / graduates) * 100
    return percentage
print(calculate_percentage_in_software_jobs(cohort1)) #expect 60

# function to calculate the average time it takes for students to get a software job. unit of measurement = months
# there are some measurement decisions to make. What value do people who don't have a software job? I may have to exclude these people from the function. 
# 1. iterate over the months in cohort, and calculate the difference (that month subtract graduate month). Put the difference into a list.
# 2. get the average value of the differences.
# this requires the cohort's month of graduation. There are design decisions here: does the month attach to the cohort or to the student? Less typing if it's the cohort, but will need to restructure the cohort data type. 
def calculate_average_days_to_get_software_job(cohort):
    graduation_date = cohort["graduation_date"]
    differences = []
    for student in cohort["students"]:
        if student["software_job"] == True:
            difference = student["start_date"] - graduation_date
            differences.append(difference)
    average_days = np.mean(differences).days
    return average_days

    # return graduation_month.strftime("%B")

print(calculate_average_days_to_get_software_job(cohort1))

# try to calculate average months to get software job

def calculate_average_months_to_get_software_job(cohort):
    graduation_date = cohort["graduation_date"]
    differences = []
    for student in cohort["students"]:
        if student["software_job"] == True:
            difference = relativedelta.relativedelta(student["start_date"], graduation_date)
            differences.append(difference.months)
    average_months = np.mean(differences)
    adjusted_months = round(average_months, 1)
    return adjusted_months
print(calculate_average_months_to_get_software_job(cohort1))

# function to calculate the % of students in software role after 1 month.
# function to calculate the % of students in software role after 3 months.
# function to calculate the % of students in software role after 6 months.
# These are actually the same function, but using a different argument.
def calculate_percentage_of_students_in_software_role(cohort, months_after_graduation):
    employed_graduates = []
    graduates = count_cohort_graduates(cohort)
    graduation_date = cohort["graduation_date"]
    for student in cohort["students"]:
        if student["software_job"] == True:
            difference = relativedelta.relativedelta(student["start_date"], graduation_date)
            if difference.months <= months_after_graduation:
                employed_graduates.append(student)
    percentage = (len(employed_graduates) / graduates) * 100
    return percentage

print(calculate_percentage_of_students_in_software_role(cohort1, 1)) #expect 20 (i.e. 1 out of 5 graduates)
print(calculate_percentage_of_students_in_software_role(cohort1, 3)) #expect 60 (i.e. 3 out of 5 graduates)


# function to calculate the % of students who do not get a software role. 
def calculate_percentage_of_graduates_not_in_software_role(cohort):
    non_software_graduates = []
    graduates = count_cohort_graduates(cohort)
    for student in cohort["students"]:
        if student["software_job"] == False:
            non_software_graduates.append(student)
    percentage = (len(non_software_graduates) / graduates) * 100
    return percentage

print(calculate_percentage_of_graduates_not_in_software_role(cohort1)) # expect 40 (i.e. 2 out of 5)


