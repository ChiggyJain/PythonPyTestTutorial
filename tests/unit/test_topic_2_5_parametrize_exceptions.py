import pytest
from app.calculator import divide


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
    "a, b",
    [
        (10, 0),
        (5, 0),
        (-1, 0),
    ]
)
def test_divide_by_zero_parametrized(a, b):
    with pytest.raises(ValueError):
        divide(a, b)
