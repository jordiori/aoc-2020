"""Day 01 - Part 1"""
import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    expenses = input_txt.splitlines()
    for idx1 in range(len(expenses) - 1):
        for idx2 in range(1, len(expenses)):
            exp1 = int(expenses[idx1])
            exp2 = int(expenses[idx2])
            if exp1 + exp2 == 2020:
                return exp1 * exp2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    if not args.input_file:
        raise ValueError('Missing input_file!')

    with open(args.input_file) as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()