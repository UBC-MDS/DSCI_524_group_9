from pygtracker import __version__
from pygtracker import pygtracker
from pytest import raises
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal


def test_version():
    assert __version__ == "0.1.0"


# Start tests for register_courses


def test_register_courses_course_id_invalid():
    tracker = pygtracker.GradeTracker()
    df = generate_df_register_courses([555], ["lab1"], [1])

    with raises(ValueError):
        tracker.register_courses(df)


def test_register_courses_assess_invalid():
    tracker = pygtracker.GradeTracker()
    df = generate_df_register_courses([522], ["lab5"], [1])

    with raises(ValueError):
        tracker.register_courses(df)


def test_register_courses_weight_invalid_not_sum_to_one():
    tracker = pygtracker.GradeTracker()
    df = generate_df_register_courses(
        [511],
        ["lab4", "lab2", "lab1", "lab3"],
        [
            0.2,
            0.3,
            0.4,
            0.2,
        ],
    )

    with raises(ValueError):
        tracker.register_courses(df)


def test_register_courses_weight_invalid_negative():
    tracker = pygtracker.GradeTracker()
    df = generate_df_register_courses(
        [523], ["lab4", "lab2", "lab1", "lab3"], [-0.5, 0.2, 0.7, 0.6]
    )

    with raises(ValueError):
        tracker.register_courses(df)


def test_register_courses_expected_df():
    tracker = pygtracker.GradeTracker()
    df = generate_df_register_courses(
        [523],
        ["lab1", "lab2", "lab3", "lab4", "quiz1", "quiz2"],
        [0.15, 0.15, 0.15, 0.15, 0.2, 0.2],
    )
    tracker.register_courses(df)

    res_df = generate_df_register_courses_output(
        [523],
        ["lab1", "lab2", "lab3", "lab4", "quiz1", "quiz2"],
        [0.15, 0.15, 0.15, 0.15, 0.2, 0.2],
    )

    assert_frame_equal(tracker.courses, res_df)


# End tests for register_courses

# Start tests for record_grades


def test_record_grades_course_id_invalid():
    tracker = pygtracker.GradeTracker()
    df = generate_df_record_grade([577], ["lab2"], [99.1], ["vaden"])

    with raises(ValueError):
        tracker.record_grades(df)


def test_record_grades_assess_invalid():
    tracker = pygtracker.GradeTracker()
    df = generate_df_record_grade([571], ["lab6"], [100], ["selina"])

    with raises(ValueError):
        tracker.record_grades(df)


def test_record_grades_grade_invalid_negative():
    tracker = pygtracker.GradeTracker()
    df = generate_df_record_grade(
        [511], ["xiran"], ["lab4", "lab2", "lab1", "lab3"], [100.1, -77, 99, 88.4]
    )

    with raises(ValueError):
        tracker.record_grades(df)


def test_record_grades_expected_df():
    tracker = pygtracker.GradeTracker()
    df = generate_df_record_grade(
        [552],
        ["fiona"],
        ["lab1", "lab2", "lab3", "lab4", "quiz1", "quiz2"],
        [66.6, 88.8, 77.7, 99.9, 90.9, 67.89],
    )

    tracker.record_grades(df)
    grade_df = generate_df_record_grades_output(
        [552],
        ["fiona"],
        ["lab1", "lab2", "lab3", "lab4", "quiz1", "quiz2"],
        [66.6, 88.8, 77.7, 99.9, 90.9, 67.89],
    )

    assert_frame_equal(tracker.grades, grade_df)


# 4 helper functions to generate dummy input and output df


def generate_df_register_courses(course_id, assessment_id, weight):
    df = pd.DataFrame(
        {
            "course_id": course_id * len(weight),
            "assessment_id": assessment_id,
            "weight": weight,
        }
    )
    return df


def generate_df_register_courses_output(course_id, assessment_id, weight):

    w = np.reshape(weight, (-1, len(assessment_id)))
    c = np.reshape(course_id, (-1, 1))
    df = pd.DataFrame(data=np.hstack((c, w)), columns=["course_id"] + assessment_id)

    df.course_id = df.course_id.astype(int)
    df.course_id = df.course_id.astype(str)
    return df


def generate_df_record_grade(course_id, student_id, assessment_id, grade):
    df = pd.DataFrame(
        {
            "course_id": course_id * len(grade),
            "student_id": student_id * len(grade),
            "assessment_id": assessment_id,
            "grade": grade,
        }
    )
    return df


def generate_df_record_grades_output(course_id, student_id, assessment_id, grade):

    g = np.reshape(grade, (-1, len(assessment_id)))
    c = np.reshape(course_id, (-1, 1))
    s = np.reshape(student_id, (-1, 1))

    df = pd.DataFrame(
        data=np.hstack((c, s, g)),
        columns=["course_id", "student_id"] + assessment_id,
    )
    df[assessment_id] = df[assessment_id].astype(float)
    return df


# End tests for record_grades

# Start tests for generate_course_statistics

# End tests for generate_course_statistics

# Start tests for rank_courses

# End tests for rank_courses

# Start tests for rank_students

# tests that the user inputs the right number of students
def test_rank_students_num_of_students_match():
    tracker = generate_input_calculate_final_grade()
    assert (tracker.rank_students(n=4).shape[0]) == 4, "Number of students don't match"


# raises an error when the number of students is negative
def test_rank_students_num_of_students_negative():
    tracker = generate_input_calculate_final_grade()
    with raises(ValueError):
        tracker.rank_students(n=-4)


# raises an error when the ascending arguemnt is not a boolean
def test_rank_students_ascending_input_not_bool():
    gradetracker = pygtracker.GradeTracker()
    with raises(TypeError):
        gradetracker.rank_students(course_id="511", ascending="True")


# raise an error when the number of students is not an integer
def test_rank_students_n_input_not_integer():
    gradetracker = pygtracker.GradeTracker()
    with raises(TypeError):
        gradetracker.rank_students(n="4")


# raise an error with the course input is not a string
def test_rank_students_course_input_not_string():
    gradetracker = pygtracker.GradeTracker()
    with raises(TypeError):
        gradetracker.rank_students(course_id=511)


# dataframe is equal to an example dataframe when running for 1 course
def test_rank_students_one_course_df_equal():
    tracker = generate_input_calculate_final_grade()
    rank_df = tracker.rank_students(course_id="511", n=1, ascending=False)

    example_df = pd.DataFrame(
        {"student_id": "joel", "grade": 90.82, "rank": 1.0}, index=[3]
    )

    assert_frame_equal(rank_df, example_df)


# dataframe is equal to an example dataframe - when running for all courses
def test_rank_students_all_courses_df_equal():
    tracker = generate_input_calculate_final_grade()
    rank_df = tracker.rank_students(course_id="all", n=1, ascending=False)

    example_df = pd.DataFrame(
        {"student_id": "joel", "grade": 91.81, "rank": 1.0}, index=[0]
    )

    assert_frame_equal(rank_df, example_df)


# output of grades dataframe should only have values between 1 - 100
def test_rank_students_grade_result_between_0_100():
    tracker = generate_input_calculate_final_grade()
    rank_df = tracker.rank_students(course_id="all", n=1, ascending=False)
    assert (
        True if 0 <= rank_df["grade"][0] <= 100 else False
    ), "Grade is not between 0 and 100"


# End tests for rank_students

# Start tests for suggest_grade_adjustment
def test_suggest_grade_adjustment_course_id_not_string():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(course_id=None)


def test_suggest_grade_adjustment_benchmark_course_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(course_id="511", benchmark_course="80")


def test_suggest_grade_adjustment_benchmark_lab_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=80, benchmark_lab="90"
        )


def test_suggest_grade_adjustment_benchmark_quiz_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=80, benchmark_lab=90, benchmark_quiz="90"
        )


def test_suggest_grade_adjustment_benchmark_course_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=150, benchmark_lab=90, benchmark_quiz=90
        )


def test_suggest_grade_adjustment_benchmark_course_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=-2, benchmark_lab=90, benchmark_quiz=90
        )


def test_suggest_grade_adjustment_benchmark_lab_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=90, benchmark_lab=150, benchmark_quiz=90
        )


def test_suggest_grade_adjustment_benchmark_lab_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=90, benchmark_lab=-2, benchmark_quiz=90
        )


def test_suggest_grade_adjustment_benchmark_quiz_more_than_one_hundred():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=90, benchmark_lab=90, benchmark_quiz=150
        )


def test_suggest_grade_adjustment_benchmark_quiz_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment(
            course_id="511", benchmark_course=90, benchmark_lab=90, benchmark_quiz=-2
        )


def test_suggest_grade_adjustment_no_adjustment_needed():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id="511", benchmark_course=85, benchmark_lab=85, benchmark_quiz=85
    )

    assert_frame_equal(new_grades, tracker.grades[tracker.grades["course_id"] == "511"])


def test_suggest_grade_adjustment_adjust_labs():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id="511", benchmark_course=85, benchmark_lab=95, benchmark_quiz=85
    )

    expected_grades = generate_expected_grades([95, 95, 95, 95, 85, 85])
    assert_frame_equal(new_grades, expected_grades)


def test_suggest_grade_adjustment_adjust_quiz():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id="511", benchmark_course=85, benchmark_lab=85, benchmark_quiz=90
    )

    expected_grades = generate_expected_grades([90, 90, 90, 90, 90, 90])
    assert_frame_equal(new_grades, expected_grades)


def test_suggest_grade_adjustment_adjust_course():
    tracker = generate_input_suggest_grade_adjustment()
    new_grades = tracker.suggest_grade_adjustment(
        course_id="511", benchmark_course=98, benchmark_lab=85, benchmark_quiz=90
    )

    expected_grades = generate_expected_grades([100, 100, 100, 100, 100, 90])
    assert_frame_equal(new_grades, expected_grades)


def test_calculate_final_grade_511():
    tracker = generate_input_calculate_final_grade()

    final_grade = tracker.calculate_final_grade(["511"])
    expected_final_grade = generate_expected_final_grades(
        "511", [84.66, 88.34, 87.66, 90.82]
    )

    assert_frame_equal(final_grade, expected_final_grade)


def test_calculate_final_grade_522():
    tracker = generate_input_calculate_final_grade()

    final_grade = tracker.calculate_final_grade(["522"])
    expected_final_grade = generate_expected_final_grades(
        "522", [95.52, 87.92, 88.92, 92.8]
    )

    assert_frame_equal(final_grade, expected_final_grade)


def generate_input_suggest_grade_adjustment():
    tracker = pygtracker.GradeTracker()
    tracker.courses = pd.DataFrame(
        np.array([["511", 0.15, 0.15, 0.15, 0.15, 0.2, 0.2]]),
        columns=["course_id", "lab1", "lab2", "lab3", "lab4", "quiz1", "quiz2"],
    )
    tracker.grades = pd.DataFrame(
        np.array([["511", "studentA", 90, 90, 90, 90, 85, 85]]),
        columns=[
            "course_id",
            "student_id",
            "lab1",
            "lab2",
            "lab3",
            "lab4",
            "quiz1",
            "quiz2",
        ],
    )
    tracker.courses = convert_dtypes_to_float(tracker.courses)
    tracker.grades = convert_dtypes_to_float(tracker.grades)

    return tracker


def generate_input_calculate_final_grade():
    tracker = pygtracker.GradeTracker()
    tracker.courses = pd.DataFrame(
        np.array(
            [
                ["511", 0.15, 0.15, 0.15, 0.15, 0.2, 0.2, 0, 0, 0, 0, 0],
                ["522", 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.2, 0.3, 0.2],
            ]
        ),
        columns=[
            "course_id",
            "lab1",
            "lab2",
            "lab3",
            "lab4",
            "quiz1",
            "quiz2",
            "milestone1",
            "milestone2",
            "milestone3",
            "milestone4",
            "feedback",
        ],
    )

    tracker.grades = pd.DataFrame(
        np.array(
            [
                ["511", "tom", 100, 100, 79.2, 83.6, 75.6, 75.6, 0, 0, 0, 0, 0],
                ["511", "tiff", 87.6, 100, 81.2, 89.2, 100, 73.2, 0, 0, 0, 0, 0],
                ["511", "mike", 84.4, 79.6, 75.2, 98.8, 84.8, 100, 0, 0, 0, 0, 0],
                ["511", "joel", 100, 100, 99.6, 71.2, 96.8, 79.2, 0, 0, 0, 0, 0],
                ["522", "tom", 0, 0, 0, 0, 0, 0, 100, 97.6, 80, 100, 100],
                ["522", "tiff", 0, 0, 0, 0, 0, 0, 100, 77.2, 76.8, 100, 85.6],
                ["522", "mike", 0, 0, 0, 0, 0, 0, 92, 75.6, 97.6, 84.4, 98.8],
                ["522", "joel", 0, 0, 0, 0, 0, 0, 98.4, 85.6, 96.8, 100, 82.4],
            ]
        ),
        columns=[
            "course_id",
            "student_id",
            "lab1",
            "lab2",
            "lab3",
            "lab4",
            "quiz1",
            "quiz2",
            "milestone1",
            "milestone2",
            "milestone3",
            "milestone4",
            "feedback",
        ],
    )
    tracker.courses = convert_dtypes_to_float(tracker.courses)
    tracker.grades = convert_dtypes_to_float(tracker.grades)

    return tracker


def generate_expected_grades(grades):
    expected_grades = pd.DataFrame(
        np.array([["511", "studentA"] + grades]),
        columns=[
            "course_id",
            "student_id",
            "lab1",
            "lab2",
            "lab3",
            "lab4",
            "quiz1",
            "quiz2",
        ],
    )
    expected_grades = convert_dtypes_to_float(expected_grades)

    return expected_grades


def generate_expected_final_grades(course_id, grades):
    expected_final_grades = pd.DataFrame(
        {
            "course_id": [course_id] * len(grades),
            "student_id": ["tom", "tiff", "mike", "joel"],
            "grade": grades,
        }
    )

    return expected_final_grades


def convert_dtypes_to_float(df):
    new_dtypes = {}

    for column in df.columns:
        if column != "course_id" and column != "student_id":
            new_dtypes[column] = np.float64

    df = df.astype(new_dtypes)

    return df


# End tests for suggest_grade_adjustments
