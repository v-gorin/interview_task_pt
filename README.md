# interview_task_pt

## TODO list

- [x] Implementation of the shell sort method
- [x] write unit tests for the shell sort method
- [x] write tests for the shell sort method
- [x] Implementation of the command `grep -A NUM -B NUM pattern file`
- [x] write unit tests for grep implementation
- [ ] write tests for grep implementation

#### Nice to have
 - [ ] Tests for programs , when we call them using CLI

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
 
### Run tests

Use `python run_test.py --show-plan` to print all existed tests wich will be run.
Also can be used parameter group to show tests in test group.

Use `python run_test.py` or `python run_test.py --group=<group_name>`
In first case all tests will be run.
In second case we ca choose which group will be run.

`group` parameter may be equal:

* shell - to run all shell sort tests
* shell_positive - to run all shell positive tests
* shell_negative - to run all shell negative tests
* Can be specified name of specific test
 
## Known issues
* Grep utility is hanging during the run of `grep -A 4 -B 3 '--' test_ok_file_1.txt`
* Unit tests for grep_ab failed if pattern == '\\-\\-'