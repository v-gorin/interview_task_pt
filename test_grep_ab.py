from grep_ab import my_function
import unittest
import os


class TestsGrepAB(unittest.TestCase):

    def setUp(self):
        self.command = "grep -A {A} -B {B} '{pattern}' {file}"

    def test_passing_regular_expression(self):
        A = 4
        B = 3
        pattern = r'^-'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_passing_not_matched_pattern(self):
        A = 4
        B = 3
        pattern = r'^"I am'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_ok(self):
        A = 3
        B = 3
        pattern = r'of'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_match_all(self):
        A = 3
        B = 3
        pattern = r'.*'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_match_separator(self):
        A = 3
        B = 3
        pattern = r'\-\-'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_only_matched_lines(self):
        A = 0
        B = 0
        pattern = r'Interpret'
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_empty_file(self):
        A = 4
        B = 3
        pattern = r'second'
        file = 'test_data/test_empty_file.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_non_existed_file(self):
        with self.assertRaises(IOError):
            my_function('test_data/test_non_existed_file.txt', 'test')

    def test_all_lines_same(self):
        A = 3
        B = 3
        pattern = r'same'
        file = 'test_data/test_all_lines_same.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

    def test_empty_pattern(self):
        A = 3
        B = 3
        pattern = r''
        file = 'test_data/test_ok_file_1.txt'
        out = os.popen(self.command.format(A=A, B=B,
                                           pattern=pattern, file=file))
        string_cli_out = out.read()
        string_my_out = my_function(file, pattern, A, B)
        self.assertEquals(string_cli_out, string_my_out)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsGrepAB)
    unittest.TextTestRunner(verbosity=2).run(suite)
