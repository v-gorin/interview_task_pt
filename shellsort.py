import argparse


def list_checker(values, value_type=int):
    """ Check each value in the list have the same specified type

    :param values: list of values
    :param value_type: typo of value
    :return:
    """
    if not isinstance(values, list):
        raise TypeError('{current} is not a list'.format(current=values))
    if len(values) == 0:
        raise ValueError('List is empty')

    for v in values:
        if not isinstance(v, value_type):
            msg = 'Value "{0}" in list has {1}. '\
                  'Expected {2}'.format(v, type(v), value_type)
            raise TypeError(msg)


def shell_sort(num_list):
    """ Shell sort

    :param num_list: list of integer numbers
    :return: sorted list of integers
    """
    list_checker(num_list)

    list_len = len(num_list)
    step = list_len/2

    if list_len == 1:
        return num_list

    while step > 0:
        for start in range(step):
            for i in range(start + step, list_len, step):
                value = num_list[i]
                pos = i
                while pos >= step and num_list[pos - step] > value:
                    num_list[pos] = num_list[pos - step]
                    pos -= step
                num_list[pos] = value
        step /= 2
    return num_list


def cli():
    cli = argparse.ArgumentParser(prog='Shell sort programm',
                                  description='Command line tool for sorting '
                                              'list by Shell method')
    cli.add_argument('-l', '--list', required=True, type=str,
                     help='List of integers separated by coma')
    return cli.parse_args()


def main():
    args = cli()
    num_list = args.list.split(',')
    num_list = [int(n) for n in num_list]
    print shell_sort(num_list)


if __name__ == '__main__':
    main()
