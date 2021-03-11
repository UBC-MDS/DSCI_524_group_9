# Author: Javairia, Jianru, Yanhua and Vu
import numpy as np
import pandas as pd

assessment_list = [
    "lab1",
    "lab2",
    "lab3",
    "lab4",
    "milestone1",
    "milestone2",
    "milestone3",
    "milestone4",
    "feedback",
    "quiz1",
    "quiz2",
]

course_list = [
    511,
    512,
    513,
    521,
    522,
    523,
    524,
    525,
    531,
    532,
    541,
    542,
    551,
    552,
    553,
    554,
    561,
    562,
    563,
    571,
    572,
    573,
    574,
    575,
    591,
]


def check_in_mds(ids, mds_list):
    return set(ids).issubset(mds_list)


class GradeTracker:

    courses = None
    grades = None

    def __init__(self):
        pass

    def register_courses(self, df):

        input_courses = df.course_id.tolist()
        if not check_in_mds(input_courses, course_list):
            error_input = [x for x in input_courses if x not in course_list]
            raise ValueError(
                "Oops, your dataframe has non-MDS Course(s) DSCI "
                + str(error_input)[1:-1]
            )

        input_assess = df.iloc[:, 1].tolist()
        if not check_in_mds(input_assess, assessment_list):
            error_input = [x for x in input_assess if x not in assessment_list]
            raise ValueError(
                f"Oops, your dataframe has non-MDS assessment(s) {str(error_input)[1:-1]}"
            )

        if sum(df.weight.values < 0) > 0 or sum(df.weight.values > 1) > 0:
            err_w = [w for _, w in df.weight.items() if w < 0 or w > 1]
            raise ValueError(
                f"One of the weight={err_w}, which is not within the range 0 to 1."
            )

        for course_id, sum_weight in (
            df.groupby("course_id").sum("weight").weight.items()
        ):
            if sum_weight != 1:
                raise ValueError(f"The sum of weights of DSCI {course_id} should be 1.")

        self.courses = df.pivot_table(
            index="course_id", columns="assessment_id", values="weight", fill_value=0
        ).reset_index()
        self.courses.columns.name = None
        self.courses.course_id = self.courses.course_id.astype(str)

    def record_grades(self, df):

        input_courses = df.course_id.tolist()
        if not check_in_mds(input_courses, course_list):
            error_input = [x for x in input_courses if x not in course_list]
            raise ValueError(
                "Oops, your dataframe has non-MDS Course(s) DSCI "
                + str(error_input)[1:-1]
            )

        input_assess = df.assessment_id.tolist()
        if not check_in_mds(input_assess, assessment_list):
            error_input = [x for x in input_assess if x not in assessment_list]
            raise ValueError(
                f"Oops, your dataframe has non-MDS assessment(s) {str(error_input)[1:-1]}"
            )

        if sum(df.grade.values < 0) > 0 or sum(df.grade.values > 100) > 0:
            err_g = [g for _, g in df.grade.items() if g < 0 or g > 100]
            raise ValueError(
                f"One of the grade={err_g}, which is not valid to be 0 to 100 (inclusive)."
            )

        self.grades = df.pivot_table(
            index=["course_id", "student_id"],
            columns="assessment_id",
            values="grade",
            fill_value=0,
        ).reset_index()
        self.grades.columns.name = None
        self.grades.course_id = self.grades.course_id.astype(str)

    def generate_course_statistics(self, course_ids):

        course_list = list(self.courses["course_id"])

        # check input type
        if type(course_ids) != list:
            raise TypeError("course_ids should be a list of str")

        for i in range(len(course_ids)):
            if type(course_ids[i]) != str:
                raise TypeError("course_ids should be a list of str")

        # check input existence
        if set(course_ids).issubset(set(course_list)) is False:
            error_input = [x for x in course_ids if x not in course_list]
            raise ValueError("Course(s) " + ",".join(error_input) + " doesn't exit.")

        final_grade = self.calculate_final_grade(course_ids)

        statistics = list()

        for course in course_ids:
            course_grade = final_grade[final_grade["course_id"] == course]["grade"]
            course_statistics = {
                "course_id": course,
                "mean": course_grade.mean(),
                "1st-quantile": course_grade.quantile(q=0.25),
                "median": course_grade.median(),
                "3rd-quantile": course_grade.quantile(q=0.75),
            }
            statistics.append(course_statistics)

        statistics_summary = pd.DataFrame(statistics)

        return statistics_summary

    def rank_courses(self, method="mean", descending=True):

        # check input type
        if type(descending) != bool:
            raise TypeError("descending should be a boolean value")

        possible_method = ["mean", "1st-quantile", "median", "3rd-quantile"]
        if method not in possible_method:
            raise ValueError(
                "Method only accepts 'mean', '1st-quantile', 'median' or '3rd-quantile'"
            )

        course_list = list(self.courses["course_id"])

        course_rank_df = pd.DataFrame()

        course_rank_df = self.generate_course_statistics(course_list)[
            ["course_id", method]
        ].sort_values(by=method, ascending=(not descending))
        course_rank_df.columns = ["course_id", "grade"]

        return course_rank_df

    def rank_students(self, course_id="all", n=3, ascending=False):
        # check if ascending is a boolean
        if not isinstance(ascending, bool):
            raise TypeError("Ascending value should be a boolean.")
        # check if course id is a string
        if not isinstance(course_id, str):
            raise TypeError("Course id should be a string.")
        # check if n is an integer and is less than the total
        if not isinstance(n, int):
            raise TypeError("N value should be a integer.")
        # check that the number of students is a positive number
        if not n >= 0:
            raise ValueError("N value should be a positive number greater than zero")

        # call helper function and get the dataframe
        course_and_grade_df = self.calculate_final_grade(
            self.courses["course_id"].unique().tolist()
        )

        # check if course_id is part of courses list
        if not (
            course_id in (course_and_grade_df["course_id"].unique().tolist() + ["all"])
        ):
            raise ValueError("Course ID is not a part of the courses dataset.")

        if course_id == "all":
            # calculates the mean grade and sorts the values
            ranking = pd.DataFrame(
                course_and_grade_df.pivot(
                    index="course_id", columns="student_id", values="grade"
                )
                .mean(axis=0)
                .sort_values(ascending=ascending)
            ).reset_index()
            # renames the column
            ranking = ranking.rename(columns={0: "grade"})
            # add a rank column
            ranking["rank"] = ranking["grade"].rank(ascending=ascending)
            # filter by number of students
            final_ranking = ranking.head(n)

        else:
            # filter based on specified course
            filtered = course_and_grade_df[
                course_and_grade_df["course_id"].isin([course_id])
            ]
            # sort the values
            ranking = filtered.drop(columns="course_id").sort_values(
                by="grade", ascending=ascending
            )
            # add a rank column
            ranking["rank"] = ranking["grade"].rank(ascending=ascending)
            # filter by number of students
            final_ranking = ranking.head(n)

        return final_ranking

    def suggest_grade_adjustment(
        self, course_id, benchmark_course=90, benchmark_lab=85, benchmark_quiz=85
    ):
        if not isinstance(course_id, str):
            raise TypeError("Course id should be a string.")

        metrics = {
            benchmark_course: "Course benchmark",
            benchmark_lab: "Lab benchmark",
            benchmark_quiz: "Quiz benchmark",
        }

        for benchmark, name in metrics.items():
            if not isinstance(benchmark, float) and not isinstance(benchmark, int):
                raise TypeError(name + " should be a float.")

            if benchmark < 0 or benchmark > 100:
                raise ValueError(name + " should be between 0 and 100 (inclusive)")

        adjusted = self.grades[self.grades["course_id"] == course_id].copy()

        # get assessments that belong to this course
        temp = self.courses[self.courses["course_id"] == course_id].T[1:]
        temp = temp[temp[0] != 0]  # filter assessment with 0
        columns = list(temp.index.values)

        # adjust quizzes or labs
        for column in columns:
            if column.startswith("quiz"):
                while adjusted[column].mean() < benchmark_quiz:
                    adjusted[column] = adjusted[column].apply(lambda x: min(x + 1, 100))
            else:
                while adjusted[column].mean() < benchmark_lab:
                    adjusted[column] = adjusted[column].apply(lambda x: min(x + 1, 100))

        # adjust course
        weights = self.courses[self.courses["course_id"] == course_id]

        avg_course = (adjusted[columns] @ weights[columns].T).mean()[0]

        for column in columns:
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
                adjusted[column] = adjusted[column].apply(lambda x: 100)
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
        course_id_col = []
        student_id_col = []
        grade_col = []

        for course_id in course_ids:
            weights = self.courses[self.courses["course_id"] == course_id]
            grades = self.grades[self.grades["course_id"] == course_id]

            columns = grades.columns.values

            for col in ["course_id", "student_id"]:
                columns = np.delete(columns, np.where(columns == col))

            final_grade = grades[columns] @ weights[columns].T.iloc[:, 0]

            course_id_col += [course_id] * len(final_grade)
            student_id_col += grades["student_id"].tolist()
            grade_col += final_grade.tolist()

        result_df = pd.DataFrame(
            {
                "course_id": course_id_col,
                "student_id": student_id_col,
                "grade": grade_col,
            }
        )

        return result_df
