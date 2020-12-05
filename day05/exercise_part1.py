import argparse


NUM_ROWS = 128
NUM_COLS = 8


def compute_seat_id(boarding_pass: str) -> int:
    """Compute seat ID."""
    rows = list(range(NUM_ROWS))
    cols = list(range(NUM_COLS))
    for character in boarding_pass[:-3]:
        half = len(rows) // 2
        if character == 'F':
            rows = rows[:half]
        elif character == 'B':
            rows = rows[half:]
    for character in boarding_pass[-3:]:
        half = len(cols) // 2
        if character == 'L':
            cols = cols[:half]
        elif character == 'R':
            cols = cols[half:]
    return rows[0] * 8 + cols[0]


def solve(input_txt: str) -> int:
    """Solve exercise."""
    passes = input_txt.splitlines()
    seat_ids = []
    for boarding_pass in passes:
        seat_ids.append(compute_seat_id(boarding_pass))

    return max(seat_ids)


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