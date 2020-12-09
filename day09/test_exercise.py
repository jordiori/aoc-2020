import pytest

import exercise_part1
import exercise_part2


def test_solve_part1() -> None:
    preamble = 5
    expected = 127
    with open('test_input.txt') as f:
        assert exercise_part1.solve(f.read(), preamble) == expected


def test_solve_part1() -> None:
    preamble = 5
    expected = 62
    with open('test_input.txt') as f:
        assert exercise_part2.solve(f.read(), preamble) == expected