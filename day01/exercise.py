import argparse


def solve_part1(input_txt: str) -> int:
    """Solve exercise part 1."""
    expenses = input_txt.splitlines()
    for idx1 in range(len(expenses) - 1):
        for idx2 in range(1, len(expenses)):
            exp1 = int(expenses[idx1])
            exp2 = int(expenses[idx2])
            if exp1 + exp2 == 2020:
                return exp1 * exp2


def solve_part2(input_txt: str) -> int:
    """Solve exercise part 2."""
    expenses = input_txt.splitlines()
    for idx1 in range(len(expenses) - 2):
        for idx2 in range(1, len(expenses) - 1):
            for idx3 in range(2, len(expenses)):
                exp1 = int(expenses[idx1])
                exp2 = int(expenses[idx2])
                exp3 = int(expenses[idx3])
                if exp1 + exp2 + exp3 == 2020:
                    return exp1 * exp2 * exp3


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    if not args.input_file:
        raise ValueError('Missing input_file!')

    with open(args.input_file) as f:
        print(f'Part 1: {solve_part1(f.read())}')
    with open(args.input_file) as f:
        print(f'Part 2: {solve_part2(f.read())}')


if __name__ == '__main__':
    main()