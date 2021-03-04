from pygtracker import __version__
from pygtracker import pygtracker
from pytest import raises
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal, assert_series_equal


def test_version():
    assert __version__ == "0.1.0"


# Start tests for register_courses

# End tests for register_courses

# Start tests for record_grades

# End tests for record_grades

# Start tests for generate_course_statistics


def test_generate_course_statistics_input_not_exist():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.generate_course_statistics(course_ids=[500, "511"])


def test_generate_course_statistics_course_id_boolean():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.generate_course_statistics(course_ids=[True, "511"])


def test_generate_course_statistics_course_id_not_list_of_string():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.generate_course_statistics(course_ids="511")


# the output is equal to the statistics summary calculate mannually
# def test_generate_course_statistics_equal():
# 511_mean = num1
# 522_median = num2

# tracker = pygtracker.GradeTracker()
# output = tracker.generate_course_statistics()

# assert output[output["course_id"]=="511"][1] == 511_mean
# assert output[output["course_id"]=="522"][3] == 522_median

# check the columns of the dataframe that come of the function


def test_generate_course_statistics_output_match():
    tracker = pygtracker.GradeTracker()
    row_num = len(tracker.generate_course_statistics(course_ids=["511", "522"]))
    columns_list = tracker.generate_course_statistics(course_ids=["511", "522"]).columns
    assert columns_list[0] == "course_id"
    assert columns_list[1] == "mean"
    assert columns_list[2] == "1st-quantile"
    assert columns_list[3] == "median"
    assert columns_list[4] == "3rd-quantile"
    assert row_num == 2


# End tests for generate_course_statistics

# Start tests for rank_courses
def test_rank_courses_input_method_type():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.rank_courses(descending=1)


def test_rank_courses_input_method():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.rank_courses(method="avg")


def test_rank_courses_order():
    tracker = pygtracker.GradeTracker()
    assert_series_equal(
        tracker.rank_courses(descending=True).iloc[-1],
        tracker.rank_courses(descending=False).iloc[0],
    )


def test_rank_courses_columns_names_match():
    tracker = pygtracker.GradeTracker()
    columns_list = tracker.rank_courses().columns
    assert columns_list[0] == "course_id"
    assert columns_list[1] == "grade"


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
