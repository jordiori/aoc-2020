import argparse
from typing import List, Tuple
from copy import deepcopy


OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


def get_occupied_seats(grid: List[List[str]], row_id: int, seat_id: str):
    """Get occupied seats."""
    max_rows = len(grid)
    max_seats = len(grid[0])
    occupied_seats = 0

    # go left
    s = seat_id - 1
    while s >= 0:
        if grid[row_id][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[row_id][s] == OCCUPIED
            break
        s -= 1

    # go right
    s = seat_id + 1
    while s < max_seats:
        if grid[row_id][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[row_id][s] == OCCUPIED
            break
        s += 1

    # go up
    r = row_id - 1
    while r >= 0:
        if grid[r][seat_id] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][seat_id] == OCCUPIED
            break
        r -= 1

    # go down
    r = row_id + 1
    while r < max_rows:
        if grid[r][seat_id] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][seat_id] == OCCUPIED
            break
        r += 1

    # go diagonal left-up
    r = row_id - 1
    s = seat_id - 1
    while r >= 0 and s >= 0:
        if grid[r][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][s] == OCCUPIED
            break
        r -= 1
        s -= 1

    # go diagonal right-up
    r = row_id - 1
    s = seat_id + 1
    while r >= 0 and s < max_seats:
        if grid[r][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][s] == OCCUPIED
            break
        r -= 1
        s += 1

    # go diagonal left-down
    r = row_id + 1
    s = seat_id - 1
    while r < max_rows and s >= 0:
        if grid[r][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][s] == OCCUPIED
            break
        r += 1
        s -= 1

    # go diagonal right-down
    r = row_id + 1
    s = seat_id + 1
    while r < max_rows and s < max_seats:
        if grid[r][s] in [OCCUPIED, EMPTY]:
            occupied_seats += grid[r][s] == OCCUPIED
            break
        r += 1
        s += 1

    return occupied_seats


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

            occupied_seats = get_occupied_seats(grid, row_id, seat_id)

            if current_occupied and occupied_seats >= 5:
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