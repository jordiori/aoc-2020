import pytest

import exercise_part1
import exercise_part2


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('0,3,6', 436),
        ('1,3,2', 1),
        ('2,1,3', 10),
        ('1,2,3', 27),
        ('2,3,1', 78),
        ('3,2,1', 438),
        ('3,1,2', 1836),
    ],
)
def test_solve_part1(input: str, expected: int) -> None:
    assert exercise_part1.solve(input) == expected


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('0,3,6', 175594),
        ('1,3,2', 2578),
        ('2,1,3', 3544142),
        ('1,2,3', 261214),
        ('2,3,1', 6895259),
        ('3,2,1', 18),
        ('3,1,2', 362),
    ],
)
def test_solve_part2(input: str, expected: int) -> None:
    assert exercise_part2.solve(input) == expected
