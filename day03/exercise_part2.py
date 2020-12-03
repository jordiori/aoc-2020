import argparse

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""


def check_slope(input_txt: str, right: int, down: int) -> int:
    """Check number of trees based on the slope."""
    rows = input_txt.splitlines()
    num_trees = 0
    col = 0
    num_cols = len(rows[0])
    for row in range(0, len(rows), down):
        if rows[row][col] == '#':
            num_trees += 1
        col = (col + right) % num_cols
    
    return num_trees

def solve(input_txt: str) -> int:
    """Solve exercise."""
    return (
        check_slope(input_txt, 1, 1) *
        check_slope(input_txt, 3, 1) *
        check_slope(input_txt, 5, 1) *
        check_slope(input_txt, 7, 1) *
        check_slope(input_txt, 1, 2)
    )


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