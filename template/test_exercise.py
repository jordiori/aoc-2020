import pytest

import exercise

@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        # test cases
    ),
)
def test_solve(input: str, expected: int) -> None:
    assert exercise.solve(input) == expected