import argparse


"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) - optional
"""


def solve(input_txt: str) -> int:
    """Solve exercise."""
    valid = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = input_txt.split('\n\n')
    for passport in passports:
        fields = {p.split(':')[0]:p.split(':')[1] for p in passport.split()}
        missing_req_fields = [rf for rf in required_fields if rf not in fields]
        if not missing_req_fields:
            valid += 1

    return valid

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