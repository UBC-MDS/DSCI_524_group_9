from pygtracker import __version__
from pygtracker import pygtracker
from pytest import raises
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal

def test_version():
    assert __version__ == '0.1.0'
    
# Start tests for register_courses

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
def test_suggest_grade_adjustment_course_id_not_string():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(course_id=None)

def test_suggest_grade_adjustment_benchmark_course_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course="80"
            )

def test_suggest_grade_adjustment_benchmark_lab_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=80,
            benchmark_lab="90"
            )

def test_suggest_grade_adjustment_benchmark_quiz_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=80,
            benchmark_lab=90,
            benchmark_quiz="90"
            )

def test_suggest_grade_adjustment_benchmark_course_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=150,
            benchmark_lab=90,
            benchmark_quiz=90
            )

def test_suggest_grade_adjustment_benchmark_course_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=-2,
            benchmark_lab=90,
            benchmark_quiz=90
            )

def test_suggest_grade_adjustment_benchmark_lab_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=90,
            benchmark_lab=150,
            benchmark_quiz=90
            )

def test_suggest_grade_adjustment_benchmark_lab_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=90,
            benchmark_lab=-2,
            benchmark_quiz=90
            )

def test_suggest_grade_adjustment_benchmark_quiz_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=90,
            benchmark_lab=90,
            benchmark_quiz=150
            )

def test_suggest_grade_adjustment_benchmark_quiz_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511",
            benchmark_course=90,
            benchmark_lab=90,
            benchmark_quiz=-2
            )

def test_suggest_grade_adjustment_no_adjustment_needed():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id='511',
        benchmark_course=85,
        benchmark_lab=85,
        benchmark_quiz=85
        )

    assert_frame_equal(new_grades, tracker.grades[tracker.grades['course_id'] == '511'])

def test_suggest_grade_adjustment_adjust_labs():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id='511',
        benchmark_course=85,
        benchmark_lab=95,
        benchmark_quiz=85
        )

    expected_grades = generate_expected_grades([95, 95, 95, 95, 85, 85])
    assert_frame_equal(new_grades, expected_grades)

def test_suggest_grade_adjustment_adjust_quiz():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id='511',
        benchmark_course=85,
        benchmark_lab=85,
        benchmark_quiz=90
        )

    expected_grades = generate_expected_grades([90, 90, 90, 90, 90, 90])
    assert_frame_equal(new_grades, expected_grades)

def test_suggest_grade_adjustment_adjust_course():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id='511',
        benchmark_course=98,
        benchmark_lab=85,
        benchmark_quiz=90
        )

    expected_grades = generate_expected_grades([100, 100, 100, 100, 100, 90])
    assert_frame_equal(new_grades, expected_grades)

def generate_input_suggest_grade_adjustment():
    tracker = pygtracker.GradeTracker()
    tracker.courses = pd.DataFrame(np.array([['511', 0.15, 0.15, 0.15, 0.15, 0.2, 0.2]]),
                   columns=['course_id', 'lab1', 'lab2', 'lab3', 'lab4', 'quiz1', 'quiz2'])
    tracker.grades = pd.DataFrame(np.array([['511', 'studentA', 90, 90, 90, 90, 85, 85]]),
                   columns=['course_id', 'student_id', 'lab1', 'lab2', 'lab3', 'lab4', 'quiz1', 'quiz2'])
    tracker.courses = convert_dtypes_to_float(tracker.courses)
    tracker.grades = convert_dtypes_to_float(tracker.grades)

    return tracker

def generate_expected_grades(grades):
    expected_grades = pd.DataFrame(np.array([['511', 'studentA'] + grades]),
                   columns=['course_id', 'student_id', 'lab1', 'lab2', 'lab3', 'lab4', 'quiz1', 'quiz2'])
    expected_grades = convert_dtypes_to_float(expected_grades)

    return expected_grades

def convert_dtypes_to_float(df):
    new_dtypes = {}

    for column in df.columns:
        if column != 'course_id' and column != 'student_id':
            new_dtypes[column] = np.float64
    
    df = df.astype(new_dtypes)

    return df

# End tests for suggest_grade_adjustments