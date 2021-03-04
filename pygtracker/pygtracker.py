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
        course_list=[511, 512, 513, 521, 522, 523, 524, 525, 531, 532, 541, 542, 551, 552, 553, 554, 561, 562, 563, 571, 572, 573, 574, 575, 591]
        input_courses=df.iloc[:, 0].tolist()
        if not set(input_courses).issubset(course_list): 
            error_input = [x for x in input_courses if x not in course_list]
            raise ValueError("Oops, your dataframe has non-MDS Course(s) DSCI " + str(error_input)[1:-1])
            
        
        assessment_list = ['lab1', 'lab2', 'lab3', 'lab4', 'milestone1', 'milestone2', 'milestone3', 'milestone4', 'feedback', 'quiz1', 'quiz2']
        input_assess=df.iloc[:, 1].tolist()
        if not set(input_assesss).issubset(assessment_list):
            error_input = [x for x in input_assess if x not in assessment_list]
            raise ValueError(f"Oops, your dataframe has non-MDS assessment(s) {str(error_input)[1:-1]}")
        
        if sum(df.iloc[:, 2]<0)>0 or sum(df.iloc[:, 2] >1)>0:
            raise ValueError('The weights in your dataframe should be between 0 and 1 (inclusive)')


        self.courses=df.pivot_table(index='course_id', columns='assessment_id', values='weight',fill_value=0).reset_index()
        self.courses.columns.name=None
        self.courses.course_id=self.courses.course_id.astype(str)  

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
        return None