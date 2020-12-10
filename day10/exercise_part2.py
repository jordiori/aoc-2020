import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    adapters = sorted([int(x) for x in input_txt.splitlines()])
    # insert 0
    adapters.insert(0, 0)
    max_adapter = max(adapters)
    combis = {}
    for adapter in adapters:
        combis[adapter] = [jolt for jolt in range(adapter + 1, adapter + 4) if jolt in adapters]

    combinations = {}
    def get_combinations(start_value: int) -> int:
        """Get number of combinations."""
        if start_value == max_adapter:
            return 1
        if combinations.get(start_value) is not None:
            return combinations.get(start_value)

        num_combinations = 0
        for v in combis[start_value]:
            num_combinations += get_combinations(v)

        combinations[start_value] = num_combinations
        return num_combinations

    return get_combinations(0)


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