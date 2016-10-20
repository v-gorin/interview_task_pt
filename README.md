# interview_task_pt

## TODO list

- [x] Implementation of the shell sort method
- [x] write unit tests for the shell sort method
- [ ] write tests for the shell sort method
- [x] Implementation of the command `grep -A NUM -B NUM pattern file`
- [x] write unit tests for grep implementation
- [ ] write tests for grep implementation

## Install requirements
    'pip install -r requirements.txt --upgrade'

## Tasks
### Shell sort

 Use `python shellsort.py --help` to know how to use it
 
 Use `coverage run test_shellsort.py && coverage report shellsort.py` 
 to run unit tests and show code coverage
 
### Grep function

 Use `python grep_ab.py --help` to know how to use it
 
 Use `coverage run test_grep_ab.py && coverage report grep_ab.py` 
 to run unit tests and show code coverage
 
## Known issues
* Grep utility is hanging during the run of `grep -A 4 -B 3 '--' test_ok_file_1.txt`
* Tests failed if pattern == '\\-\\-'