import re
import os
import argparse


def my_function(file_path, pattern, after=0, before=0):
    """ Implementation of functionality of 'grep -A NUM -B NUM pattern file'.

    :param file_path: path to file
    :param pattern: str pattern
    :param after: numbers of lines to be printed after matched line
    :param before: numbers of lines to be printed before matched line
    :return:
    """
    res = []
    step = 0
    sep = '--\n'
    with open(file_path, 'r') as open_file:
        lines = open_file.readlines()

    if not lines:
        return ''

    for i in range(len(lines)):
        if re.search(pattern, lines[i]):
            if not any([before, after]):
                res.append(lines[i])
                continue

            bef = i-before if i-before > step else step
            step = i + 1
            aft = i + after + 1

            if before and not after:
                res.extend(lines[bef:i+1] + [sep])
            elif before and after:
                res.extend([sep] + lines[bef:i])

            if after:
                res.append(lines[i])
                add_sep = True
                for line in lines[i+1:aft]:
                    if re.search(pattern, line):
                        add_sep = False
                        break
                    res.append(line)
                if add_sep:
                    res.append(sep)

    if not res:
        return ''

    res = res[0: len(res)-1] if res[len(res)-1] == sep else res
    res = res[1:] if res[0] == sep else res
    if not res[len(res)-1].endswith('\n'):
        res[len(res)-1] += '\n'

    # check all
    res2 = [e for e in res if e != sep]
    if res2 == lines:
        return ''.join(res2)
    return ''.join(res)


def cli():
    cli = argparse.ArgumentParser(
            prog='Print matched line and lines before and after',
            description='Implementation of command '
                        '"grep -A NUM -B NUM pattern file"')

    cli.add_argument('-F', '--file', required=True, type=str,
                     help='path to file')
    cli.add_argument('-P', '--pattern', required=True, type=str,
                     help='pattern')
    cli.add_argument('-A', '--after', required=False, type=int,
                     help='Amount of lines after context')
    cli.add_argument('-B', '--before', required=False, type=int,
                     help='Amount of lines before context')
    return cli.parse_args()


def main():
    args = cli()
    input_file = os.path.abspath(args.file)
    print my_function(input_file, str(args.pattern),
                      int(args.after), int(args.before))

if __name__ == "__main__":
    main()
