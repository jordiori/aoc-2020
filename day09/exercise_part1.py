import argparse
from typing import List


PREAMBLE = 25


def has_sum(preamble: List[int], num: int) -> bool:
    """Check if sum exists in preamble."""
    for n1 in preamble[:-1]:
        for n2 in preamble[1:]:
            if num == n1 + n2 and n1 != n2:
                return True
    return False


def solve(input_txt: str, p: int = PREAMBLE) -> int:
    """Solve exercise."""
    numbers = [int(x) for x in input_txt.splitlines()]
    preamble = numbers[:p]
    for number in numbers[p:]:
        if not has_sum(preamble, number):
            return number
        preamble.pop(0)
        preamble.append(number)


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