import argparse


def solve(input_txt: str) -> int:
    """Solve exercise."""
    instructions = input_txt.splitlines()
    accumulator = 0
    idx = 0
    visited_instructions = []
    while idx not in visited_instructions:
        visited_instructions.append(idx)
        ins, offset = instructions[idx].split()
        if ins == 'jmp':
            if offset[0] == '+':
                idx += int(offset[1:])
            elif offset[0] == '-':
                idx -= int(offset[1:])
            continue
        if ins == 'acc':
            if offset[0] == '+':
                accumulator += int(offset[1:])
            elif offset[0] == '-':
                accumulator -= int(offset[1:])
        idx += 1
    
    return accumulator


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