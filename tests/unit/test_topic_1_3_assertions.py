from app.calculator import is_even


def test_is_even_true():
    assert is_even(4)


def test_is_even_false():
    assert not is_even(5)
