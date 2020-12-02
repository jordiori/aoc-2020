import pytest

import exercise_part1
import exercise_part2

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc', 2)
    ],
)
def test_solve_part1(input: str, expected: int) -> None:
    assert exercise_part1.solve(input) == expected


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc', 1)
    ],
)
def test_solve_part2(input: str, expected: int) -> None:
    assert exercise_part2.solve(input) == expected