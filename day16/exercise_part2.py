import argparse
from typing import List, Dict
from itertools import permutations


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


def filter_invalid_tickets(
    nearby_tickets: List[List[int]], restrictions: Dict[str, List[int]]
) -> List[List[int]]:
    """Filter invalid tickets."""
    valid_tickets = nearby_tickets.copy()
    for ticket in nearby_tickets:
        for ticket_value in ticket:
            valid = False
            for r in restrictions.values():
                if ticket_value in r:
                    valid = True
                    break
            else:
                if not valid:
                    valid_tickets.remove(ticket)
                    break
    return valid_tickets


def find_field_order(
    valid_tickets: List[List[int]], restrictions: Dict[str, List[int]]
) -> List[str]:
    """Find valid field order."""
    invalid_pos = {}
    for order_id, r_order in enumerate(permutations(restrictions.keys())):
        # check that permutation is valid
        for idx, invalid_value in invalid_pos.items():
            if r_order[idx] in invalid_value:
                break
        else:
            order_valid = True
            for ticket in valid_tickets:
                for idx, r in enumerate(r_order):
                    if ticket[idx] not in restrictions[r]:
                        order_valid = False
                        break
                if not order_valid:
                    if idx in invalid_pos:
                        invalid_pos[idx].append(r)
                    else:
                        invalid_pos[idx] = [r]
                    break
            if order_valid:
                return list(r_order)
    return list(r_order)


def solve(input_txt: str) -> int:
    """Solve exercise."""
    sections = input_txt.split('\n\n')
    restrictions = parse_restrictions(sections[0].splitlines())
    my_ticket = parse_ticket(sections[1].splitlines()[1])
    nearby_tickets = [parse_ticket(t) for t in sections[2].splitlines()[1:]]
    valid_tickets = filter_invalid_tickets(nearby_tickets, restrictions)
    field_order = find_field_order(valid_tickets, restrictions)
    print(field_order)
    return 0


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