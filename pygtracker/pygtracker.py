# Author: Javairia, Jianru, Yanhua and Vu


class GradeTracker:
  """
  A grade tracker to help UBC lecturers to manage, analyze and adjust students' grades

  Parameters
  ----------

  Attributes
  ----------
  courses : DataFrame
    The dataframe containing component weights for each course
  grades : 
    The dataframe containing grades for each students in each course
  """

  courses = None
  grades = None

  def __init__(self):
    """see help(GradeTracker)"""
    pass

  def register_courses(self, df):
    """
    Read and store the input dataframe as a pandas dataframe.

    Parameters
    ----------
    df: DataFrame
      A tidy dataframe with course_id, assessments (lab1, quiz1, etc.) and their weights (eg, 0.2).
      All assessment component for a course must sump up to 1.

    Returns
    -------
    None
    """
    return None

  def record_grades(self, df):
    """
    Record grades for students for specific courses and assessments

    Parameters
    ----------
    df: pandas DataFrame
      A tidy dataframe with course_id, student_id, assessment_id and grades

    Returns
    -------
    None
    """
    return None

  def generate_course_statistics(self, course_ids):
    """
    Calculate the statistics summary for specified courses, including mean, median and quantiles
        
    Parameters
    ----------
    course_id: list
        A list includes course IDs for which the statistics summary are calculated. 
    
    Returns
    ----------
    DataFrame
        A dataframe containing the statistics summary for specified courses. 
        Row index is course id. Each row will include mean, 1st-quantile, median, 3rd-quantile for the specified course.
    """
    return course_statistics_df


  def rank_course(self, method="mean", descending=True):
    """
    Calculate students' course grades to rank courses in descending order by specified method
    
    Parameters
    ----------
    method: str, default "mean"
        The method applied to rank the courses. The default option is mean
        Possible Options: "mean", "1st-quantile", "median", "3rd-quantile"
    descending: bool, default True
        A boolean value to decide if the rank should be in descending or ascending order, by default it is descending order
    
    Returns
    -------
    DataFrame
        A dataframe containing the ranking for all courses. 
    """
    return course_ranker_df
    
  def rank_students(self, course_id="all", n=10, descending=True):
    """
    Calculates the average grade for a specified number of students
    and ranks them in ascending/descending order for a specific course or
    for the entire program completed thus far.

    Parameters
    ----------
    course_id: int or str, default "all"
        The course id for which the ranking is calculated for
        by student. Default will provide the ranking for the entire program completed thus far
    n: int, default 10
        The number of students to rank
    descending: bool, default True
        A boolean value to decide if the rank should be in descending or ascending order, by default it is descending order

    Returns
    -------
    DataFrame
        A dataframe containing the rank of students by average grade. Row index is student id, and Column Index is the rank.
    """
    return None

  def suggest_grade_adjustment(self, course_id, benchmark_course=0.9, benchmark_lab=0.85, benchmark_quiz=0.85):
    """
    Suggest grade adjustment for a particular course based on predefined benchmarks
    to make sure the final grade meets or exceeds these benchmarks

    Parameters
    ----------
    course_id: str
      The id of the course to be adjusted
    benchmark_course: float, default 0.9
      The benchmark of which the average grade for the whole course must meet or exceed
    benchmark_lab: float, default 0.85
      The benchmark of which the average grade for each lab must meet or exceed
    benchmark_quiz: float, default 0.85
      The benchmark of which the average grade for each quiz must meet or exceed  

    Returns
    -------
    DataFrame
      A dataframe containing newly adjusted grades for students in a course. Row Index is
    student id, and Column Index is the assessment id.
    """
    return None
