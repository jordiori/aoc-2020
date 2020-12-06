import pytest

import exercise_part1
import exercise_part2

def test_solve_part1() -> None:
    expected = 11
    with open('test_input.txt') as f:
        assert exercise_part1.solve(f.read()) == expected


def test_solve_part2() -> None:
    expected = 6
    with open('test_input.txt') as f:
        assert exercise_part2.solve(f.read()) == expected