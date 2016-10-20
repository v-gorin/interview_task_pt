from shellsort import shell_sort
import unittest


class TestsShellSort(unittest.TestCase):

    def test_ok(self):
        data = [5, 6, 4, 3, 8, 9, 10, 234, 123, 543, 234, 654]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_list_1_element(self):
        data = [1]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_list_2_elements(self):
        data = [4, 1]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_list_only_zeroes(self):
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_list_same_values(self):
        data = [5, 5, 5, 5, 5, 5, 5, 5, 5]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_sorted_list(self):
        data = [1, 2, 3, 4]
        self.assertEquals(shell_sort(data), sorted(data))

    def test_empty_list_raise_error(self):
        data = []
        with self.assertRaises(ValueError):
            shell_sort(data)

    def test_list_of_empty_lists_raise_error(self):
        data = [[], [], [], []]
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_list_of_non_empty_lists_raise_error(self):
        data = [[1, 2, 3, 4], [1, 2, 3, 4], [5, 6, 7, 8], [7, 4, 6, 3]]
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_list_of_strings_raise_error(self):
        data = ['4', '3', '1', '2'],
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_list_of_ints_and_strings_raise_error(self):
        data = [1, 2, 3, 'e'],
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_string_raise_error(self):
        data = '5,4,3,2,1'
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_tuple_raise_error(self):
        data = (1, 2, 3, 4, 5, 2, 4, 1, 3),
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_dict_raise_error(self):
        data = {1: 2, 3: 4, 5: 6, 7: 8}
        with self.assertRaises(TypeError):
            shell_sort(data)

    def test_set_raise_error(self):
        data = {5, 4, 3, 2, 6}
        with self.assertRaises(TypeError):
            shell_sort(data)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsShellSort)
    unittest.TextTestRunner(verbosity=2).run(suite)

