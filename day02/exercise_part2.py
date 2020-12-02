import argparse


# Example:
# 3-4 j: tjjj
# [pos1-pos2] letter: password


def is_password_valid(password: str) -> bool:
    """Check if password is valid."""
    positions, letter, p = password.split()
    pos1, pos2 = positions.split('-')
    letter = letter[0]
    if p[int(pos1) - 1] == letter and p[int(pos2) - 1] != letter:
        return True
    if p[int(pos1) - 1] != letter and p[int(pos2) - 1] == letter:
        return True
    return False

def solve(input_txt: str) -> int:
    """Solve exercise."""
    valid_passwords = 0
    passwords = input_txt.splitlines()
    for p in passwords:
        if is_password_valid(p):
            valid_passwords += 1
    return valid_passwords


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