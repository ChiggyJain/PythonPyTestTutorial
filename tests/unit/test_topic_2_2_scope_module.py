import pytest


# scope=module means shared generated fixture for each test-file including all defined test-function-cases
# Same fixture instance is reused for all test-case in this file only
@pytest.fixture(scope="module")
def shared_counter():
    return {"count": 0}


def test_shared_counter_first(shared_counter):
    shared_counter["count"] += 1
    assert shared_counter["count"] == 1


def test_shared_counter_second(shared_counter):
    shared_counter["count"] += 1
    assert shared_counter["count"] == 2
