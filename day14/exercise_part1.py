import argparse
import re


def binary_to_decimal(n):
    return int(n, 2)


def decimal_to_binary(n):
    return bin(int(n)).replace('0b', '').rjust(36, '0')


def apply_mask(value, mask_map):
    """Apply mask map to a value."""
    result = list(decimal_to_binary(value))
    for idx, v in mask_map.items():
        result[idx] = v
    return binary_to_decimal(''.join(result))


def solve(input_txt: str) -> int:
    """Solve exercise."""
    mem = {}
    for line in input_txt.splitlines():
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
            mask_map = {idx: value for idx, value in enumerate(mask) if value != 'X'}
        else:
            address = int(re.findall(r'\d+', line.split('=')[0].strip())[0])
            value = line.split('=')[1].strip()
            mem[address] = apply_mask(value, mask_map)

    return sum(mem.values())


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
