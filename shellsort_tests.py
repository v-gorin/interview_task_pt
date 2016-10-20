from Shellsort import shell_sort
import unittest


class TestsShellSort(unittest.TestCase):

    def test_ok(self):
        data_set = [
            [999],
            [999, 999],
            [999, 1000],
            [1, 2, 3, 4],
            [0, 0, 0, 0, 0, 0],
            [5, 6, 4, 3, 8, 9, 10, 234, 123, 543, 234, 654]
        ]
        for v in data_set:
            self.assertEquals(shell_sort(v), sorted(v))

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            shell_sort([])

    def test_not_integer_in_list(self):
        with self.assertRaises(TypeError):
            shell_sort([1, 2, 3, 'e'])
            shell_sort(['4', '3', '1', '2'])
            shell_sort(['a', 'b', 'c', 'd'])


if __name__ == "__main__":
    unittest.main()
