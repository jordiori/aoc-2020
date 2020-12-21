import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    turns = {int(x): idx + 1 for idx, x in enumerate(input_txt.split(','))}
    last_value = list(turns.keys())[-1]
    turn_idx = turns[last_value] + 1
    current_value = 0
    while turn_idx < 30000000:
        last_value = current_value
        if current_value in turns:
            current_value = turn_idx - turns[last_value]
        else:
            current_value = 0
        turns[last_value] = turn_idx
        turn_idx += 1
    return current_value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    if not args.input_file:
        raise ValueError('Missing input_file!')

    with open(args.input_file) as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
