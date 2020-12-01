import pytest

import exercise


@pytest.mark.parametrize(
    ('input_text', 'expected'),
    [
        ('1721\n979\n366\n299\n675\n1456\n', 514579)
    ],
)
def test_solve_part1(input_text: str, expected: int) -> None:
    assert exercise.solve_part1(input_text) == expected


@pytest.mark.parametrize(
    ('input_text', 'expected'),
    [
        ('1721\n979\n366\n299\n675\n1456\n', 241861950)
    ],
)
def test_solve_part2(input_text: str, expected: int) -> None:
    assert exercise.solve_part2(input_text) == expected