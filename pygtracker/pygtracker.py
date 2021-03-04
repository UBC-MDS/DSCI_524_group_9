# Author: Javairia, Jianru, Yanhua and Vu
import numpy as np
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
        self, course_id, benchmark_course=90, benchmark_lab=85, benchmark_quiz=85
    ):
        """
        Suggest grade adjustment for a particular course based on predefined benchmarks
        to make sure the final grade meets or exceeds these benchmarks.

        Parameters
        ----------
        course_id: str
            The id of the course to be adjusted.
        benchmark_course: float, default 90
            The benchmark of which the average grade for the whole course must meet or exceed.
        benchmark_lab: float, default 85
            The benchmark of which the average grade for each lab must meet or exceed.
        benchmark_quiz: float, default 85
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

        metrics = {
            benchmark_course: "Course benchmark",
            benchmark_lab: "Lab benchmark",
            benchmark_quiz: "Quiz benchmark"
        }

        for benchmark, name in metrics.items():
            if not isinstance(benchmark, float) and not isinstance(benchmark, int):
                raise TypeError(name + " should be a float.")

            if benchmark < 0 or benchmark > 100:
                raise ValueError(name + " should be between 0 and 100 (inclusive)")

        adjusted = self.grades[self.grades['course_id'] == course_id].copy()

        # adjust quizzes or labs
        columns = adjusted.columns.values

        for col in ['course_id', 'student_id']:
            columns = np.delete(columns, np.where(columns == col))

        for column in columns:
                if column.startswith('quiz'):
                    while adjusted[column].mean() < benchmark_quiz:
                        adjusted[column] = adjusted[column].apply(lambda x: min(x + 1, 100))
                else:
                    while adjusted[column].mean() < benchmark_lab:
                        adjusted[column] = adjusted[column].apply(lambda x: min(x + 1, 100))

        # adjust course
        weights = self.courses[self.courses['course_id'] == course_id]

        avg_course = (adjusted[columns] @ weights[columns].T).mean()[0]

        for column in columns:
            print("avg_course", avg_course)

            if avg_course >= benchmark_course:
                break

            avg_component = adjusted[column].mean()

            # how much average course grade increases
            # if all students have max score in this component
            diff = (100 - avg_component) * weights[column][0]

            # if this increase does not make the average course grade
            # higher than the benchmark
            if avg_course + diff < benchmark_course:
                # let everyone have 100 marks
                adjusted[column] =  adjusted[column].apply(lambda x: 100)
                avg_course += diff
            else:
                # increase gradually until it meets the benchmark
                while avg_course < benchmark_course:
                    adjusted[column] = adjusted[column].apply(lambda x: min(x + 1, 100))
                    avg_course = (adjusted[columns] @ weights[columns].T).mean()[0]
                break

        adjusted[columns] = adjusted[columns].apply(lambda x: x * 1.0)
        return adjusted

    def calculate_final_grade(self, course_ids):
        """
        Calculate final grade for all students in a course

        Parameters
        ----------
        course_ids: list of str
            The ids of the courses to calculate the average grade for all students.

        Returns
        -------
        DataFrame
            A dataframe containing final grades for all students in a course:
                course_id: str
                student_id: str
                grade: float
        """

        course_id_col = []
        student_id_col = []
        grade_col = []

        for course_id in course_ids:
            weights = self.courses[self.courses['course_id'] == course_id]
            grades = self.grades[self.grades['course_id'] == course_id]

            columns = grades.columns.values

            for col in ['course_id', 'student_id']:
                columns = np.delete(columns, np.where(columns == col))

            final_grade = grades[columns] @ weights[columns].T.iloc[:,0]

            course_id_col += [course_id] * len(final_grade)
            student_id_col += grades['student_id'].tolist()
            grade_col += final_grade.tolist()

        result_df = pd.DataFrame({
            'course_id': course_id_col,
            'student_id': student_id_col,
            'grade': grade_col
            })

        return result_df
