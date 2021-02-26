# Author: Javairia, Jianru, Yanhua and Vu

class GradeTracker():
    """[To be completed: Docstring for the class]
    """
    courses = None
    grades = None

    def __init__(self):
        """see help(GradeTracker)"""
        pass

    # Start: Register the courses

    # End: Register the courses

    # Start: Record the grade for students

    # End: Record the grade for students

    # Start: Summarize the grades by courses

    # End: Summarize the grades by courses

    # Start: Summarise the grades by students

    # End: Summarise the grades by students

    # Start: Suggest grade adjustment
    def suggest_grade_adjustment(course_id, benchmark_course = 0.9, benchmark_lab = 0.85, benchmark_quiz = 0.85)
    """
    Suggest grade adjustment for a particular course based on predefined benchmarks
    to make sure the final grade meets or exceeds these benchmarks

    Parameters
    ----------
    course_id : str
      The id of the course to be adjusted
    benchmark_course : float, default 0.9
      The benchmark of which the average grade for the whole course must meet or exceed
    benchmark_lab : float, default 0.85
      The benchmark of which the average grade for each lab must meet or exceed
    benchmark_quiz : float, default 0.85
      The benchmark of which the average grade for each quiz must meet or exceed  

    Returns
    -------
    DataFrame
      A dataframe containing newly adjusted grades for students in a course. Row Index is
    student id, and Column Index is the assessment id.
    """
        return None
    # End: Suggest grade adjustment