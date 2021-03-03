from pygtracker import __version__
from pygtracker import pygtracker
from pytest import raises

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
        tracker.suggest_grade_adjustment(None)

def test_suggest_grade_adjustment_benchmark_course_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment("511", "0.8")

def test_suggest_grade_adjustment_benchmark_lab_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment("511", 0.8, "0.9")

def test_suggest_grade_adjustment_benchmark_quiz_not_float():
    tracker = pygtracker.GradeTracker()
    with raises(TypeError):
        tracker.suggest_grade_adjustment("511", 0.8, 0.9, "0.9")

def test_suggest_grade_adjustment_benchmark_course_more_than_one():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", 1.5, 0.9, 0.9)

def test_suggest_grade_adjustment_benchmark_course_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", -0.2, 0.9, 0.9)

def test_suggest_grade_adjustment_benchmark_lab_more_than_one():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", 0.9, 1.5, 0.9)

def test_suggest_grade_adjustment_benchmark_lab_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", 0.9, -0.2, 0.9)

def test_suggest_grade_adjustment_benchmark_quiz_more_than_one():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", 0.9, 0.9, 1.5)

def test_suggest_grade_adjustment_benchmark_quiz_less_than_zero():
    tracker = pygtracker.GradeTracker()
    with raises(ValueError):
        tracker.suggest_grade_adjustment("511", 0.9, 0.9, -0.2)
# End tests for suggest_grade_adjustments