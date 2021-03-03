from pygtracker import __version__
from pygtracker import pygtracker
import pandas as pd
import numpy as np

# reading in the test csv file
courses = pd.read_csv("tests/test_data/course_info.csv")
grades = pd.read_csv("tests/test_data/student_info.csv")

# defining an instance of the class
gradetracker = pygtracker.GradeTracker()


def test_version():
    assert __version__ == "0.1.0"


# Start tests for register_courses

# End tests for register_courses

# Start tests for record_grades

# End tests for record_grades

# Start tests for generate_course_statistics

# End tests for generate_course_statistics

# Start tests for rank_courses

# End tests for rank_courses

# Start tests for rank_students

# tests that the user inputs the right number of students
def test_ranks_students_num_of_students_match():
    assert (
        gradetracker.rank_students(n=4).shape[0]
    ) == 4, "Number of students don't match"


# raises an error when a course id is not a part of the dataset
def test_rank_students_course_input_not_exist():
    with raises(NameError):
        gradetracker.rank_students(course_id="500", n=4)


# dataframe is equal to an example dataframe
def test_df_equal():
    example_df = pd.DataFrame(
        {"student_id": "nameofstudent", "rank": 1, "grade": "addgradehere"}, index=[1]
    )
    assert example_df.equals(gradetracker.rank_students(course_id="511", n=1))


# check the columns of the dataframe that come of the function
def test_rank_students_columns_names_match():
    assert gradetracker.rank_students(course_id="511", n=1).columns[0] == "student_id"
    assert gradetracker.rank_students(course_id="511", n=1).columns[1] == "rank"
    assert gradetracker.rank_students(course_id="511", n=1).columns[2] == "grade"


# End tests for rank_students

# Start tests for suggest_grade_adjustment

# End tests for suggest_grade_adjustments
