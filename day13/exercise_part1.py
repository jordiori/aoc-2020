import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    min_time = int(input_txt.splitlines()[0])
    time_buses = [
        int(time_bus) for time_bus in input_txt.splitlines()[1].split(',') if time_bus != 'x'
    ]
    time_found = False
    current_time = min_time - 1
    while not time_found:
        current_time += 1
        for time_bus in time_buses:
            if current_time % time_bus == 0:
                time_found = True
                break
    # busId * wait minutes
    return time_bus * (current_time - min_time)


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
