import pytest

import exercise_part1
import exercise_part2


def test_solve_part1() -> None:
    expected = 4
    with open('test_input.txt') as f:
        assert exercise_part1.solve(f.read()) == expected


@pytest.mark.parametrize(
    ('input_path', 'expected'),
    [
        ('test_input.txt', 32),
        ('test_input2.txt', 126)
    ],
)
def test_solve_part2(input_path: str, expected: int) -> None:
    with open(input_path) as f:
        assert exercise_part2.solve(f.read()) == expected