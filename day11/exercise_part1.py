import argparse
from typing import List, Tuple
from copy import deepcopy


OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


def do_iteration(grid: List[List[str]]) -> Tuple[List[List[int]], bool, int]:
    """Do iteration based on rules."""
    grid_changed = False
    total_occupied = 0
    new_grid = deepcopy(grid)
    for row_id, row in enumerate(grid):
        for seat_id in range(len(row)):
            if grid[row_id][seat_id] == FLOOR:
                continue
            current_occupied = grid[row_id][seat_id] == OCCUPIED
            occupied_seats = 0
            min_seat = max(0, seat_id - 1)
            max_seat = min(len(row) - 1, seat_id + 1)
            min_row = max(0, row_id - 1)
            max_row = min(len(grid) - 1, row_id + 1)

            checked = []
            for r in [min_row, max_row, row_id]:
                for s in [min_seat, max_seat, seat_id]:
                    if r == row_id and s == seat_id or [r, s] in checked:
                        continue
                    checked.append([r, s])
                    occupied_seats += grid[r][s] == OCCUPIED

            if current_occupied and occupied_seats >= 4:
                new_grid[row_id][seat_id] = EMPTY
                grid_changed = True
            if not current_occupied and occupied_seats == 0:
                new_grid[row_id][seat_id] = OCCUPIED
                grid_changed = True

            total_occupied += new_grid[row_id][seat_id] == OCCUPIED

    return new_grid, grid_changed, total_occupied


def solve(input_txt: str) -> int:
    """Solve exercise."""
    grid = []
    for row in input_txt.split():
        grid.append([seat for seat in row])

    # iterate until no changes
    grid_changed = True
    while grid_changed:
        grid, grid_changed, total_occupied = do_iteration(grid)

    return total_occupied

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