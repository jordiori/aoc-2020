import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    bus_times = {
        bus_pos: int(time_bus) for bus_pos, time_bus
        in enumerate(input_txt.splitlines()[1].split(','))
        if time_bus != 'x'
    }
    min_timestamp = 0
    bus_multipliers = {}
    for bus_pos, bus_time in bus_times.items():
        bus_multipliers[bus_pos] = [bus_time*i for i in range(999)]

    for min_timestamp in bus_multipliers[0]:
        for bus_pos in bus_times:
            if not min_timestamp + bus_pos in bus_multipliers[bus_pos]:
                break
        else:
            return min_timestamp
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    if not args.input_file:
        raise ValueError('Missing input_file!')

    with open(args.input_file) as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
