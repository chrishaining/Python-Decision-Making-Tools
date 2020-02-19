## Decision Making Tools

This is a collection of programs to help make informed decisions.

__employment_success_analyst.py__ calculates various metrics of the success rate for training courses, in terms of the number and percentage of graduates who get relevant jobs. It calculates:
* average time (in days and months) to get a relevant job
* for a given number of months following graduation, the percentage of graduates in relevant employment

## Methodology and Warning
There is a problem with calculating how long it takes a graduate to get a job: it excludes the possibility that some people will not get a job or have not got a job yet. It's possible that, at the time of measurement, a particular student has not yet got a software job. So they will not be included in the calculation of "time taken to get a software job". But if they get a job after the time of measurement, they might change the result considerably, given that their result is the highest (so far). However, this is a limitation of using recent data. An obvious way to avoid this limitation would be to wait until all the people had reached retirement age (or died): but by that time the data would be less useful.

## Possible extensions
* refactor the code - there's lots of scope for reusable code
* create classes (student class, cohort class)
* create a master function that covers multiple cohorts
* get user input. Using the terminal, this this might be a bit too much effort for a user, so a web app might be more appropriate.
* five-number summary, to show the range of unemployment times

---
# Web app 

The web app is based on the functions from __employment_success_analyst.py__. It uses the Flask framework.

## Problems and solutions
There were problems trying to migrate the database, and the following error message came up:

```INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    ERROR [root] Error: Target database is not up to date.```

To fix this, I followed instructions found on [Stack Overflow](https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date):
```flask db stamp head
    $ flask db migrate
    $ flask db upgrade```
