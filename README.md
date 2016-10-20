# interview_task_pt

Install requirements
    'pip install -r requirements.txt --upgrade'

1. **Shell sort**

 Use 'python shellsort.py --help' to know how to use it
 
 Use 'coverage run test_shellsort.py && coverage report shellsort.py' 
 to run unit tests and show code coverage
 
2. **Grep function**

 Use 'python grep_ab.py --help' to know how to use it
 
 Use 'coverage run test_grep_ab.py && coverage report grep_ab.py' 
 to run unit tests and show code coverage
 
  Known issues:
      1. If text contains string '--\n' tests failed
      2. Grep utility is hanging during the run of "grep -A 4 -B 3 '--' test_ok_file_1.txt"