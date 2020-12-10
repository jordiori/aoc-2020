import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    adapters = sorted([int(x) for x in input_txt.splitlines()])
    current_joltage = 0
    # last one has always difference of 3
    jolt_diff = {1: 0, 2: 0, 3: 1}
    for adapter in adapters:
        difference = adapter - current_joltage
        jolt_diff[difference] += 1
        current_joltage = adapter

    return jolt_diff[1] * jolt_diff[3]


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