# Author: Javairia, Jianru, Yanhua and Vu


class GradeTracker:
    """[To be completed: Docstring for the class]"""

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
    def course_statistics(course_ids):
    """
        Calculates the statistics summary for specified courses, including mean, median and quantiles
        
    Parameters
    ----------
    course_id: list
        A list includes course IDs for which the statistics summary are calculated]. 
    
    Returns
    ----------
    DataFrame
        A dataframe containing the statistics summary for specified courses, each row contains one course
    """
    return course_statistics_df


    def course_ranker(method="mean", descending=True):
    """
        Calculate students' course grades to rank courses in descending order by specified method
    
    Parameters
    ----------
    method: string, default "mean"
        The method applied to rank the courses. The default option is mean
        Possible Options: "mean", "median", "75-quantile"
    
    descending: boolean, default True
        To decide if the rank should be in ascending or descending order.
        The default option is decending order
    
    Returns
    -------
    DataFrame
        A dataframe containing the rank for all courses
    """
    return course_ranker_df
    
    # End: Summarize the grades by courses

    # Start: Summarise the grades by students
    def rank_students(course_id="all", n=10, descending=True):
        """Calculates the average grade for a specified number of students
        and ranks them in ascending/descending order for a specific course or
        for the entire program completed thus far.

        Parameters
        ----------
        course_id : int or str, default "all"
            The course id for which the ranking is calculated for
            by student. Default will provide the ranking for the entire program completed thus far
        n : int, default 10
            The number of students to rank
        descending : bool, default True
            A boolean value to decide if the rank should be in descending or ascending order, by default it is descending order

        Returns
        -------
        DataFrame
            A dataframe containing the rank of students by average grade. Row index is student id, and Column Index is the rank.
        """
        return None

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
