import pytest

import exercise_part1
import exercise_part2


@pytest.mark.parametrize(
    ('input_path', 'expected'),
    [
        ('test_input.txt', 37),
    ],
)
def test_solve_part1(input_path: str, expected: int) -> None:
    with open(input_path) as f:
        assert exercise_part1.solve(f.read()) == expected


@pytest.mark.parametrize(
    ('input_path', 'expected'),
    [
        ('test_input.txt', 26),
    ],
)
def test_solve_part2(input_path: str, expected: int) -> None:
    with open(input_path) as f:
        assert exercise_part2.solve(f.read()) == expected