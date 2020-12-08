import pytest

import exercise_part1
import exercise_part2


def test_solve_part1() -> None:
    expected = 5
    with open('test_input.txt') as f:
        assert exercise_part1.solve(f.read()) == expected


def test_solve_part2() -> None:
    expected = 8
    with open('test_input.txt') as f:
        assert exercise_part2.solve(f.read()) == expected