import argparse


MOVE_RIGHT = 3


def solve(input_txt: str) -> int:
    """Solve exercise."""
    rows = input_txt.splitlines()
    num_trees = 0
    col = 0
    num_cols = len(rows[0])
    for row in rows:
        if row[col] == '#':
            num_trees += 1
        col = (col + MOVE_RIGHT) % num_cols
    
    return num_trees


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