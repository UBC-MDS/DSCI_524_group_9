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

    # End: Summarize the grades by courses

    # Start: Summarise the grades by students
    def student_ranker(course_id="all", n=10, descending=True):
        """[Calculates the average grade for a specified number of students and ranks them in descending order for a specific course or for the entire program completed thus far]

        Args:
            course_id (int): [the course ID for which the ranking is calculated for by student.
            The default option will calculate the ranking for the entire program]. Defaults to "all".

            n(int): [the number of students to rank]. Defaults to 10.

            ascending(bool): [a boolean value to decide if the rank should be in ascending or descending order.
            The default option is decending order]. Defaults to True.

        Returns:
            [pandas.DataFrame]: [a dataframe containing the rank of a specified number of students in descending or ascending order
            for a given course or for the whole program]
        """
        return student_rank_df

    # End: Summarise the grades by students

    # Start: Suggest grade adjustment

    # End: Suggest grade adjustment