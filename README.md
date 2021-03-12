# pygtracker 

![](https://github.com/UBC-MDS/pygtracker/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pygtracker/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pygtracker) ![Release](https://github.com/UBC-MDS/pygtracker/actions/workflows/release.yml/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pygtracker/badge/?version=latest)](https://pygtracker.readthedocs.io/en/latest/?badge=latest)

## Package Overview
`pygtracker` is a Python package that allows UBC MDS lecturers to record, analyze and adjust grades for students in a particular program. Users can record grades from each course, generate a summary report to determine which class is more challenging than the rest, or identify students who may need help. Finally, the package can suggest ways to adjust the grades for students to ensure the average grades match predefined benchmarks. 

## Python Ecosystem
There are existing packages to manage students' grades in the Python ecosystem. For example, [grades-report](https://pypi.org/project/grades-report/) is a package purely generating statistics from all grades. In addition, [edx-bulk-grades](https://pypi.org/project/edx-bulk-grades/) aids lecturers in grading and modifying students' grades in bulk. However, these packages are lacking useful features that are unique to the MDS program, such as identifying students / courses that are much different from their peers or adjusting grades to make sure they conform to MDS standard. As a result, we come up with this useful tool which helps UBC MDS lecturers have a better control of student performance.

## Features
This package contains seven functions: `register_courses`, `record_grades`, `calculate_final_grade`, `generate_course_statistics`, `rank_courses`, `rank_students` and `suggest_grade_adjustment`.

The main components of this package are:

- Register courses
  - Read/store the courses information as a dataframe
- Record grades for students
  - Read/store the students' grades for each assessment as a dataframe
- Calculate the final grade
  - Provide the final grade for each student in each course using the courses information and students' grade
- Generate course statistics
  - Provide grade statistics on the courses, including mean, 1st quantile, median and 3rd quantile
- Rank courses
  - Provide the rankings of courses based on courses' average grades
- Rank students
  - Provide the rankings of students based on their average grades for the selected course (or the whole program).
- Suggest grade adjustment
  - Suggest grade adjustments for any course based on predefined benchmarks
  
## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pygtracker
```

## Dependencies

- You can find all dependencies in [pyproject.toml](https://github.com/UBC-MDS/pygtracker/blob/main/pyproject.toml) file

## Usage

A [toy dataset](https://github.com/UBC-MDS/pygtracker/tree/main/tests/test_data) is used to showcase the usage of the functions. Any csv file containing the grades and courses for the UBC MDS program may be used. 

```python
# import packages 
from pygtracker import pygtracker 
import os 

# call an instance of the class
tracker = pygtracker.GradeTracker()

# read in the toy dataset 
courses = pd.read_csv(os.path.join(".", "tests", "test_data", "course_info.csv"))
grades = pd.read_csv(os.path.join(".", "tests", "test_data", "student_info.csv"))

# read and stores data as a dataframe 
tracker.register_courses(courses)
tracker.record_grades(grades)
```

```python
# generates a dataframe with summary statistics for a specified course 
tracker.generate_course_statistics(["511"])
```
|    |   course_id |   mean |   1st-quantile |   median |   3rd-quantile |
|---:|------------:|-------:|---------------:|---------:|---------------:|
|  0 |         511 |  87.87 |          86.91 |       88 |          88.96 |

```python
# generates a dataframe for course ranking by grade 
tracker.rank_courses()
```
|    |   course_id |   grade |
|---:|------------:|--------:|
|  0 |         522 |   91.29 |
|  1 |         511 |   87.87 |

```python 
# generates a dataframe with student ranking by grade 
tracker.rank_students()
```
|    | student_id   |   grade |   rank   |
|---:|:-------------|--------:|---------:|
|  0 | joel         |   91.81 |      1.0 |
|  1 | tom          |   90.09 |      2.0 |
|  2 | mike         |   88.29 |      3.0 |

```python
# calculates the adjustment for a course for a specified benchmark 
tracker.suggest_grade_adjustment("511", benchmark_course=100)
```
|    |   course_id | student_id   |   feedback |   lab1 |   lab2 |   lab3 |   lab4 |   milestone1 |   milestone2 |   milestone3 |   milestone4 |   quiz1 |   quiz2 |
|---:|------------:|:-------------|-----------:|-------:|-------:|-------:|-------:|-------------:|-------------:|-------------:|-------------:|--------:|--------:|
|  0 |         511 | joel         |          0 |    100 |    100 |    100 |    100 |            0 |            0 |            0 |            0 |     100 |     100 |
|  1 |         511 | mike         |          0 |    100 |    100 |    100 |    100 |            0 |            0 |            0 |            0 |     100 |     100 |
|  2 |         511 | tiff         |          0 |    100 |    100 |    100 |    100 |            0 |            0 |            0 |            0 |     100 |     100 |
|  3 |         511 | tom          |          0 |    100 |    100 |    100 |    100 |            0 |            0 |            0 |            0 |     100 |     100 |


## Documentation

The official documentation is hosted on Read the Docs: https://pygtracker.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/pygtracker/graphs/contributors).

- Javairia Raza
- Jianru Deng
- Tran Doan Khanh Vu
- Yanhua Chen

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
