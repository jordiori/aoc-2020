import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    instructions = input_txt.splitlines()
    facing = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    position = {'x': 0, 'y': 0, 'facing': 0}
    action_mov = {
        'E': {'coord': 'x', 'dir': -1},
        'W': {'coord': 'x', 'dir': 1},
        'N': {'coord': 'y', 'dir': 1},
        'S': {'coord': 'y', 'dir': -1},
    }
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action in action_mov:
            mov = action_mov[action]
            position[mov['coord']] += value * mov['dir']
        elif action in 'R':
            position['facing'] = (position['facing'] - value) % 360
        elif action in 'L':
            position['facing'] = (position['facing'] + value) % 360
        elif action == 'F':
            current_facing = facing[position['facing']]
            mov = action_mov[current_facing]
            position[mov['coord']] += value * mov['dir']

    # return manhattan distance
    return abs(position['x']) + abs(position['y'])


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
