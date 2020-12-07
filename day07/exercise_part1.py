import argparse
from typing import List, Dict


def parse_rule(rule: str) -> List[str]:
    """Parse rule."""
    # clean rule and split
    bags = rule.replace(',', '').replace('.', '').split('contain')[1].split()
    if 'no' in bags and 'other' in bags:
        return []
    return [''.join(bags[idx-2:idx]) for idx, word in enumerate(bags) if 'bag' in word]


def has_shinygold_bag(all_rules: Dict[str, List[str]], inside_bags: List[str]) -> int:
    """Compute if has shinygold bag."""
    if 'shinygold' in inside_bags:
        return 1
    if not inside_bags:
        return 0

    for bag_name in inside_bags:
        bag = all_rules[bag_name]
        if has_shinygold_bag(all_rules, bag):
            return 1
    return 0


def solve(input_txt: str) -> int:
    """Solve exercise."""
    rules = input_txt.splitlines()
    all_rules = {}
    for rule in rules:
        bag_name = ''.join(rule.split('bags')[0].split())
        all_rules[bag_name] = parse_rule(rule)

    # get number of shinygold bags
    num_shiny_bags = 0
    for bag_name, inside_bags in all_rules.items():
        num_shiny_bags += has_shinygold_bag(all_rules, inside_bags)
    return num_shiny_bags


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