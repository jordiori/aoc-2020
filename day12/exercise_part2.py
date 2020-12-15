import argparse
from typing import Dict, Union


INITIAL_WAYPOINT = {'x': -10, 'y': 1}


def solve(input_txt: str) -> int:
    """Solve exercise."""
    instructions = input_txt.splitlines()
    waypoint = {'x': INITIAL_WAYPOINT['x'], 'y': INITIAL_WAYPOINT['y']}
    position = {'x': 0, 'y': 0}
    rotation = {
        'L': {0: [1, 1], 90: [1, -1], 180: [-1, -1], 270: [-1, 1]},
        'R': {0: [1, 1], 90: [-1, 1], 180: [-1, -1], 270: [1, -1]}
    }
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
            waypoint[mov['coord']] += value * mov['dir']
        elif action in rotation:
            if value % 180 != 0:
                # change coords
                waypoint['x'], waypoint['y'] = waypoint['y'], waypoint['x']
            waypoint['x'] *= rotation[action][value][0]
            waypoint['y'] *= rotation[action][value][1]
        elif action == 'F':
            position['x'] += waypoint['x'] * value
            position['y'] += waypoint['y'] * value

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
