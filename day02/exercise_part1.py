import argparse


# Example:
# 3-4 j: tjjj
# [min-max] letter: password


def is_password_valid(password: str) -> bool:
    """Check if password is valid."""
    interval, letter, p = password.split()
    min_num, max_num = interval.split('-')
    letter = letter[0]
    num_letter = 0
    for l in p:
        if l == letter:
            num_letter += 1
    return (num_letter >= int(min_num) and num_letter <= int(max_num))

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