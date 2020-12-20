import pytest

import exercise_part1
import exercise_part2


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('939\n7,13,x,x,59,x,31,19', 295)
    ],
)
def test_solve_part1(input: str, expected: int) -> None:
    assert exercise_part1.solve(input) == expected


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('1\n7,13,x,x,59,x,31,19', 1068781),
        ('1\n17,x,13,19', 3417),
        ('1\n67,7,59,61', 754018),
        ('1\n67,x,7,59,61', 779210),
        ('1\n67,7,x,59,61', 1261476),
        ('1\n1789,37,47,1889', 1202161486),
    ],
)
def test_solve_part2(input: str, expected: int) -> None:
    assert exercise_part2.solve(input) == expected