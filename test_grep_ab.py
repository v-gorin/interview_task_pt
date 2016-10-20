from grep_ab import my_function
import unittest


class TestsGrepAB(unittest.TestCase):

    def test_ok(self):
        pass

    def test_empty_file(self):
        pass

    def test_non_existed_file(self):
        with self.assertRaises(IOError):
            my_function('test_data/test_non_existed_filed', 'test')

    def test_all_lines_same(self):
        pass

    def test_not_matched_pattern(self):
        pass

    def test_empty_pattern(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsGrepAB)
    unittest.TextTestRunner(verbosity=2).run(suite)
