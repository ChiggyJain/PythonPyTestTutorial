from app.calculator import add


def test_addition_failure_demo():
    # This test is INTENTIONALLY wrong
    assert add(2, 2) == 5
