
from app.calculator import add


def test_add_two_positive_number():
    result = add(5,10)
    assert result == 15