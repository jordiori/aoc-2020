import argparse
from typing import List, Dict


def parse_rule(rule: str) -> Dict[str, int]:
    """Parse rule."""
    # clean rule and split
    bags = rule.replace(',', '').replace('.', '').split('contain')[1].split()
    if 'no' in bags and 'other' in bags:
        return []
    return {
        ''.join(bags[idx-2:idx]): int(bags[idx-3])
        for idx, word in enumerate(bags) if 'bag' in word
    }


def compute_number_bags(all_rules: Dict[str, Dict[str, int]], inside_bags: Dict[str, int]) -> int:
    """Compute number of bags."""
    num_bags = 0
    if not inside_bags:
        return 0

    for bag_name, bag_times in inside_bags.items():
        bag = all_rules[bag_name]
        num_bags += bag_times + bag_times * compute_number_bags(all_rules, bag)

    return num_bags


def solve(input_txt: str) -> int:
    """Solve exercise."""
    rules = input_txt.splitlines()
    all_rules = {}
    for rule in rules:
        bag_name = ''.join(rule.split('bags')[0].split())
        all_rules[bag_name] = parse_rule(rule)

    return compute_number_bags(all_rules, all_rules['shinygold'])


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