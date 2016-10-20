from shellsort import shell_sort
import unittest


class TestsShellSort(unittest.TestCase):

    def test_ok(self):
        data_set = [
            [999],
            [999, 999],
            [1000, 999],
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
        data_set = [
            [1, 2, 3, 'e'],
            ['4', '3', '1', '2'],
            ['a', 'b', 'c', 'd'],
            [[1, 2, 3, 4], [1, 2, 3, 4], [5, 6, 7, 8], [7, 4, 6, 3]],
            [[], [], [], []]
        ]
        for v in data_set:
            with self.assertRaises(TypeError):
                shell_sort(v)

    def test_not_list(self):
        data_set = [
            '5,4,3,2,1',
            '7 6 3 6 2',
            'somestringwithsomewords',
            (1, 2, 3, 4, 5, 2, 4, 1, 3),
            {1: 2, 3: 4, 5: 6, 7: 8}

        ]
        for v in data_set:
            with self.assertRaises(TypeError):
                shell_sort(v)


if __name__ == "__main__":
    unittest.main()

