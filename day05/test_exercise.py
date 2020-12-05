import pytest

import exercise_part1
import exercise_part2

@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        ('FBFBBFFRLR', 357),
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
    ),
)
def test_compute_seat_id_part1(input: str, expected: int) -> None:
    assert exercise_part1.compute_seat_id(input) == expected
