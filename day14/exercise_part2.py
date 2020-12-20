import argparse
import re


def binary_to_decimal(n):
    return int(n, 2)


def decimal_to_binary(n):
    return bin(int(n)).replace('0b', '').rjust(36, '0')


def apply_mask(base_address, mask_map):
    """Apply mask map to an address."""
    result = list(decimal_to_binary(base_address))
    addresses = []
    for idx, v in mask_map.items():
        result[idx] = v
    X_ids = sorted([idx for idx, value in mask_map.items() if value == 'X'], reverse=True)
    if not X_ids:
        return [binary_to_decimal(''.join(result))]
    for X in X_ids:
        if not addresses:
            # add first addresses
            for val in range(2):
                new_address = list(''.join(result).replace('X', '0'))
                new_address[X] = str(val)
                addresses.append(''.join(new_address))
        else:
            current_address = addresses.copy()
            for addr in current_address:
                for val in range(2):
                    new_address = list(addr)
                    new_address[X] = str(val)
                    if ''.join(new_address) not in addresses:
                        addresses.append(''.join(new_address))
    # return addresses in decimal
    return [binary_to_decimal(a) for a in addresses]


def solve(input_txt: str) -> int:
    """Solve exercise."""
    mem = {}
    for line in input_txt.splitlines():
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
            mask_map = {idx: value for idx, value in enumerate(mask) if value != '0'}
        else:
            base_address = int(re.findall(r'\d+', line.split('=')[0].strip())[0])
            value = line.split('=')[1].strip()
            addresses = apply_mask(base_address, mask_map)
            for addr in addresses:
                mem[addr] = int(value)
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
