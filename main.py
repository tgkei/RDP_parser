from sys import setrecursionlimit
from argparse import ArgumentParser
from scanner import Scanner
from parser import PARSER
from testcase import TESTCASE
from time import time


setrecursionlimit(99999999)


def arg_parse():
    cli_parser = ArgumentParser(description='Process some integers.')
    cli_parser.add_argument('-i', '--input', type=int, default=1,
                            help='Enter Test case number [1|2|3|4]')
    cli_parser.add_argument('-p', '--problem', type=int, default=1,
                            help="Enter problem number [1|2]")
    args = cli_parser.parse_args()
    return args.input, args.problem


def main():
    test_case, problem = arg_parse()
    test_input = TESTCASE[test_case]

    if test_case in [1, 2, 3, 4]:
        print(f"Test case: {test_case}: {test_input}")

    print("Start Parser")
    scanner = Scanner(test_input)
    scanner.tokenize()

    st = time()
    parser = PARSER[problem](scanner)
    parser.pD()
    if parser.is_matched:
        print("String matched")
    et = time()
    print(f"time spent: {et - st}")


if __name__ == "__main__":
    main()
