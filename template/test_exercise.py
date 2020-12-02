import pytest

import exercise_part1
import exercise_part2

@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        # test cases
    ),
)
def test_solve_part1(input: str, expected: int) -> None:
    assert exercise_part1.solve(input) == expected


@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        # test cases
    ),
)
def test_solve_part2(input: str, expected: int) -> None:
    assert exercise_part2.solve(input) == expected