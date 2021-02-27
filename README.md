# pygtracker 

![](https://github.com/UBC-MDS/pygtracker/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pygtracker/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pygtracker) ![Release](https://github.com/UBC-MDS/pygtracker/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pygtracker/badge/?version=latest)](https://pygtracker.readthedocs.io/en/latest/?badge=latest)

## Package Overview
`pygtracker` is a Python package that allows UBC MDS lecturers to record, analyze and adjust grades for students in a particular program. Users can record grades from each course, generate a summary report to determine which class is more challenging than the rest, or identify students who may need help. Finally, the package can suggest ways to adjust the grades for students to ensure the average grade matches a predefined benchmark. It contains six functions: `register_courses`, `record_grades`, `generate_course_statistics`, `rank_courses`, `rank_students` and `suggest_grade_adjustment`.

The main components of this package are:

- Register courses
  - Read/store the courses information as a dataframe
- Record grades for students
  - Read/store the students' grades for each assessment as a dataframe
- Generate course statistics
  - Provide grade statistics on the courses, including mean, 1st quantile, median and 3rd quantile
- Rank courses
  - Provide the rankings of courses based on courses' average grades
- Rank students
  - Provide the rankings of students based on their average grades for the selected course (or the whole program).
- Suggest grade adjustment
  - Suggest grade adjustments for any course based on predefined benchmarks

There are existing packages to manage students' grades in the Python ecosystem. For example, [grades-report](https://pypi.org/project/grades-report/) is a package purely generating statistics from all grades. In addition, [edx-bulk-grades](https://pypi.org/project/edx-bulk-grades/) aids lecturers in grading and modifying students' grades in bulk. However, these packages are lacking useful features that are unique to the MDS program, such as identifying students / courses that are much different from their peers or adjusting grades to make sure they conform to MDS standard. As a result, we come up with this useful tool which helps UBC MDS lecturers have a better control of student performance.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pygtracker
```

## Features

- TODO

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://pygtracker.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/jianructose/pygtracker/graphs/contributors).

- Javairia Raza
- Jianru Deng
- Tran Doan Khanh Vu
- Yanhua Chen

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
