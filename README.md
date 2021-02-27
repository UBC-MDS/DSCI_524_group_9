# pygtracker 

![](https://github.com/jianructose/pygtracker/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/jianructose/pygtracker/branch/main/graph/badge.svg)](https://codecov.io/gh/jianructose/pygtracker) ![Release](https://github.com/jianructose/pygtracker/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pygtracker/badge/?version=latest)](https://pygtracker.readthedocs.io/en/latest/?badge=latest)

## Package Overview
`pygtracker` is a Python package that allows UBC lecturers to record, analyze and adjust grades for students in a particular program. Users can record grades from each course, generate a summary report to determine which class is more challenging than the rest, or identify students who may need help. Finally, the package can suggest ways to adjust the grades for students to ensure the average grade matches a predefined benchmark. It contains five functions: `register_courses`, `record_grades`, `summarize_courses`, `rank_students` and `suggest_grade_adjustment`.

The main components of this package are:

- Register courses
  - Read/store the courses information as a dataframe
- Record grades for students
  - Read/store the students' grade for each assessment as a data frame
- Summarize grades by courses
  - Provide summary statistics on the courses 
  - Provide the ranking of courses based on courses' average grade
- Summarise grades by students
  - Provide the ranking of students' average grades for the course selected (or the whole program).
- Suggest grade adjustment
  - Suggest grade adjustments for any course based on predefined benchmarks

As far as we know, we are the first package in the Python ecosystem providing these functionality for UBC lecturers.

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
