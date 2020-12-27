import argparse
from typing import List, Dict


def parse_ticket(line_ticket: str) -> List[int]:
    """Parse a string ticket."""
    return [int(x) for x in line_ticket.split(',')]


def parse_restrictions(lines_restrictions: List[str]) -> Dict[str, List[int]]:
    """Parse restrictions."""
    restrictions = {}
    for r in lines_restrictions:
        r_name = r.split(':')[0]
        restrictions[r_name] = []
        values = r.split(':')[1].strip()
        ranges = [[int(v.split('-')[0]), int(v.split('-')[1])] for v in values.split('or')]
        for x in ranges:
            restrictions[r_name].extend(list(range(x[0], x[1] + 1)))
    return restrictions


def solve(input_txt: str) -> int:
    """Solve exercise."""
    sections = input_txt.split('\n\n')
    restrictions = parse_restrictions(sections[0].splitlines())
    my_ticket = parse_ticket(sections[1].splitlines()[1])
    nearby_tickets = [parse_ticket(t) for t in sections[2].splitlines()[1:]]
    invalid_values = []
    # only check nearby_tickets
    for ticket in nearby_tickets:
        for ticket_value in ticket:
            valid = False
            for r in restrictions.values():
                if ticket_value in r:
                    valid = True
            if not valid:
                invalid_values.append(ticket_value)
    return sum(invalid_values)


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