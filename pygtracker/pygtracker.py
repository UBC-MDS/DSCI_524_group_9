# Author: Javairia, Jianru, Yanhua and Vu


class GradeTracker:
    """
    A grade tracker to help UBC MDS lecturers to manage, analyze and adjust students' grades

    Parameters
    ----------

    Attributes
    ----------
    courses: DataFrame
        The dataframe containing component weights for each course.
    grades: DataFrame
        The dataframe containing grades for each student in each course.
    """

    courses = None
    grades = None

    def __init__(self):
        """see help(GradeTracker)"""
        pass

    def register_courses(self, df):
        """
        Read and store the input dataframe as a pandas DataFrame.

        Parameters
        ----------
        df: DataFrame
            A tidy dataframe:
                course_id: str
                assessment_id: str, ex: lab1, quiz1
                weight: float, ex: 0.2
            All assessment components for a course must sum up to 1.

        Returns
        -------
        None
        """
        return None

    def record_grades(self, df):
        """
        Record grades for students for a specified course and its assessments.

        Parameters
        ----------
        df: DataFrame
            A tidy dataframe:
                course_id: str
                student_id: str
                assessment_id: str
                grade: float

        Returns
        -------
        None
        """
        return None

    def generate_course_statistics(self, course_ids):
        """
        Calculate the summary statistics for specified courses including mean, median and quantiles.

        Parameters
        ----------
        course_ids: list of str
            A list including all course IDs for which the summary statistics are calculated for.

        Returns
        ----------
        DataFrame
            A dataframe containing the summary statistics for specified courses:
                course_id: str
                mean: float
                1st-quantile: float
                median: float
                3rd-quantile: float
        """
        return None

    def rank_courses(self, method="mean", descending=True):
        """
        Calculate students' course grades to rank courses in ascending/descending order by a specified method.

        Parameters
        ----------
        method: {"mean", "1st-quantile", "median", "3rd-quantile"}, default "mean"
            The method applied to rank the courses.
        descending: bool, default True
            A boolean value to decide if the rank should be in descending or ascending order.

        Returns
        -------
        DataFrame
            A dataframe containing the rank for specified courses:
                course_id: str
                rank: int
                grade: float
        """
        return None

    def rank_students(self, course_id="all", n=10, descending=True):
        """
        Calculate the average grade for a specified number of students and ranks them in
        ascending/descending order for a specific course or for the entire program completed thus far.

        Parameters
        ----------
        course_id: str, default "all"
            The course id for which the ranking is calculated for. Default will provide the ranking for
            the entire program completed thus far.
        n: int, default 10
            The number of students to rank.
        descending: bool, default True
            A boolean value to decide if the rank should be in descending or ascending order.

        Returns
        -------
        DataFrame
            A dataframe containing the rank of students by average grade:
                student_id: str
                rank: int
                grade: float
        """
        return None

    def suggest_grade_adjustment(
        self, course_id, benchmark_course=0.9, benchmark_lab=0.85, benchmark_quiz=0.85
    ):
        """
        Suggest grade adjustment for a particular course based on predefined benchmarks
        to make sure the final grade meets or exceeds these benchmarks.

        Parameters
        ----------
        course_id: str
            The id of the course to be adjusted.
        benchmark_course: float, default 0.9
            The benchmark of which the average grade for the whole course must meet or exceed.
        benchmark_lab: float, default 0.85
            The benchmark of which the average grade for each lab must meet or exceed.
        benchmark_quiz: float, default 0.85
            The benchmark of which the average grade for each quiz must meet or exceed.

        Returns
        -------
        DataFrame
            A dataframe containing newly adjusted grades for students in a course:
                student_id: str
                assessment1: float
                assessment2: float
                ...
        """
        if not isinstance(course_id, str):
            raise TypeError("Course id should be a string.")

        return None