from proboscis import test
from proboscis.asserts import assert_equal

from shellsort import shell_sort


@test(groups=['shell', 'shell_positive'])
class TestShellPositive():

    @test(groups=['check_return_sorted_list'])
    def check_return_sorted_list(self):
        test_list = [4, 23, 8, 42, 16, 15]
        builtin_sorted_list = sorted(test_list)
        shell_sorted_list = shell_sort(test_list)

        assert_equal(builtin_sorted_list, shell_sorted_list,
                     "List {0} != {1}".format(builtin_sorted_list,
                                              shell_sorted_list))

    @test(groups=['check_list_of_one_element'])
    def check_list_of_one_element(self):
        test_list = [0]
        shell_sorted_list = shell_sort(test_list)

        assert_equal(test_list, shell_sorted_list,
                     "List {0} != {1}".format(test_list, shell_sorted_list))

    @test(groups=['check_already_sorted_list'])
    def check_already_sorted_list(self):
        test_list = [18, 27, 36, 45, 54, 63, 72, 81]
        shell_sorted_list = shell_sort(test_list)

        assert_equal(test_list, shell_sorted_list,
                     "List {0} != {1}".format(test_list, shell_sorted_list))

    @test(groups=['check_list_two_elements'])
    def check_list_two_elements(self):
        test_list = [20, 16]
        builtin_sorted_list = sorted(test_list)
        shell_sorted_list = shell_sort(test_list)

        assert_equal(builtin_sorted_list, shell_sorted_list,
                     "List {0} != {1}".format(builtin_sorted_list,
                                              shell_sorted_list))

    @test(groups=['check_list_of_zeroes'])
    def check_list_of_zeroes(self):
        test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shell_sorted_list = shell_sort(test_list)
        assert_equal(test_list, shell_sorted_list,
                     "List {0} != {1}".format(test_list, shell_sorted_list))

    # @test(groups=['check_list_max_length'])
    # def check_list_max_length(self):
    #     # the maximum size of list for 32bit system is 536,870,912
    #     list_len = 536870912
    #     test_list = [random.randint(i, i + 10000) for i in xrange(list_len)]
    #     builtin_sorted_list = sorted(test_list)
    #     shell_sorted_list = shell_sort(test_list)
    #
    #     assert_equal(builtin_sorted_list, shell_sorted_list,
    #                  "List {0} != {1}".format(builtin_sorted_list,
    #                                           shell_sorted_list))


@test(groups=['shell', 'shell_negative'])
class TestShellNegative():

    @test(groups=['check_str_to_sort'])
    def check_str_to_sort(self):
        test_data = "1,2,3,4,5,6,7,8"
        try:
            shell_sort(test_data)
        except TypeError:
            pass
        else:
            raise BaseException

    @test(groups=['check_dict_to_sort'])
    def check_dict_to_sort(self):
        test_data = {1: 2, 4: 3, 6: 1, 2: 4, 5: 9, 7: 8, 3: 5}
        try:
            shell_sort(test_data)
        except TypeError:
            pass
        else:
            raise BaseException

    @test(groups=['check_set_to_sort'])
    def check_set_to_sort(self):
        test_data = {1, 4, 6, 3, 5, 7, 3}
        try:
            shell_sort(test_data)
        except TypeError:
            pass
        else:
            raise BaseException

    @test(groups=['check_empty_list'])
    def check_empty_list(self):
        test_list = []
        try:
            shell_sort(test_list)
        except ValueError:
            pass
        else:
            raise BaseException
