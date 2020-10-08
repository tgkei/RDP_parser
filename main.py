from argparse import ArgumentParser
from scanner import Scanner
from parser import Parser
from testcase import TESTCASE


def arg_parse():
    cli_parser = ArgumentParser(description='Process some integers.')
    cli_parser.add_argument('testcase', type=int,
                            help='Enter Test case number [1|2|3|4]')
    args = cli_parser.parse_args()
    return args.testcase


def main():
    test_case = arg_parse()
    test_input = TESTCASE[test_case]
    print(f"Test case: {test_case}: {test_input}")

    print("Start Parser")
    scanner = Scanner(test_input)
    scanner.tokenize()

    parser = Parser(scanner)
    parser.pD()
    if parser.is_matched:
        print("String matched")


if __name__ == "__main__":
    main()
