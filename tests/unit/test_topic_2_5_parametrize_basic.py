import pytest
from app.calculator import add


# Basic Parametrize Syntax
"""
@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (value1, value2, result),
        ...
    ]
)
"""
# single test-function with different parameters of each-case
# 1 test function + different data sets
# reduce duplication of writing same-test-case with different parameters
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
