import argparse
from typing import List, Tuple


def are_corrupted(instructions: List[str]) -> Tuple[bool, int]:
    """Check if instructions are corrupted. Return bool and value of accumulator."""
    accumulator = 0
    idx = 0
    visited_instructions = []

    while idx not in visited_instructions and idx != len(instructions):
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

    if idx in visited_instructions:
        return True, accumulator
    return False, accumulator


def solve(input_txt: str) -> int:
    """Solve exercise."""
    instructions = input_txt.splitlines()
    nop_and_jmp = [idx for idx, ins in enumerate(instructions) if ins.split()[0] in ['nop', 'jmp']]
    opposite_op = {'nop': 'jmp', 'jmp': 'nop'}

    for idx in nop_and_jmp:
        new_inst = instructions.copy()
        ins, offset = new_inst[idx].split()
        new_inst[idx] = f'{opposite_op[ins]} {offset}'
        corrupted, accumulator = are_corrupted(new_inst)
        if not corrupted:
            return accumulator

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