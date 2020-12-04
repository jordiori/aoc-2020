import argparse
import re

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def is_valid(passport: str) -> bool:
    """Check if passport is valid."""
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = {p.split(':')[0]:p.split(':')[1] for p in passport.split()}
    missing_req_fields = [rf for rf in required_fields if rf not in fields]
    if missing_req_fields:
        return False
    if len(fields['byr']) != 4 or 1920 > int(fields['byr']) or int(fields['byr']) > 2002:
        return False
    if len(fields['iyr']) != 4 or 2010 > int(fields['iyr']) or int(fields['iyr']) > 2020:
        return False
    if len(fields['eyr']) != 4 or 2020 > int(fields['eyr']) or int(fields['eyr']) > 2030:
        return False
    if re.findall('^[0-9]*', fields['hgt'])[0]:
        hgt = re.findall('^[0-9]*', fields['hgt'])[0]
        hgt_unit = re.findall('[a-z]+', fields['hgt'])
        if not hgt_unit or hgt_unit[0] not in {'cm', 'in'}:
            return False
        if fields['hgt'].endswith('cm') and (150 > int(hgt) or int(hgt) > 193):
            return False
        if fields['hgt'].endswith('in') and (59 > int(hgt) or int(hgt) > 76):
            return False
    if not re.findall('^#[a-f0-9]{6}$', fields['hcl']):
        return False
    if fields['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.findall('^[0-9]{9}$', fields['pid']):
        return False
    return True

def solve(input_txt: str) -> int:
    """Solve exercise."""
    valid = 0
    passports = input_txt.split('\n\n')
    for passport in passports:
        if is_valid(passport):
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