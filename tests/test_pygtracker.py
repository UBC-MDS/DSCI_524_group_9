from pygtracker import __version__
from pygtracker import pygtracker
import pandas as pd
import numpy as np
from pytest import raises

def test_version():
    assert __version__ == '0.1.0'
    
# Start tests for register_courses

def test_register_courses_course_id_valid():
    tracker=pygtracker.GradeTracker()
    df=pd.DataFrame()
    df['course_id']=[555]
    df['assessment_id']=['lab4']
    df['weight']=1

    with raises(ValueError):
        tracker.register_courses(df)

def test_register_courses_assess_valid():
    tracker=pygtracker.GradeTracker()
    df=pd.DataFrame()
    df['course_id']=[522]
    df['assessment_id']=['lab5']
    df['weight']=1
    with raises(ValueError):
        tracker.register_courses(df)

def test_register_courses_weight_valid_1():
    tracker=pygtracker.GradeTracker()
    df=pd.DataFrame()
    df['course_id']=[511, 511, 511, 511,]
    df['assessment_id']=['lab4', 'lab2', 'lab1', 'lab3']
    df['weight']=[.2, .3, .4, .2, ]
    with raises(ValueError):
        tracker.register_courses(df)

def test_register_courses_weight_valid_2():
    tracker=pygtracker.GradeTracker()
    df=pd.DataFrame()
    df['course_id']=[523, 523, 523, 523]
    df['assessment_id']=['lab4', 'lab2', 'lab1', 'lab3']
    df['weight']=[ -.5, .1, .9, .5]
    with raises(ValueError):
        tracker.register_courses(df)

# End tests for register_courses

# Start tests for record_grades

# End tests for record_grades

# Start tests for generate_course_statistics

# End tests for generate_course_statistics

# Start tests for rank_courses

# End tests for rank_courses

# Start tests for rank_students

# End tests for rank_students

# Start tests for suggest_grade_adjustment

# End tests for suggest_grade_adjustments