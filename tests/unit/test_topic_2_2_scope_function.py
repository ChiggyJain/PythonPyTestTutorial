import pytest


# here scope=function is by default then it will be created/destory for each test-function
# each test-function will get a fresh fixture data
@pytest.fixture(scope="function")
def counter():
    return {"count": 0}


def test_counter_increment_1(counter):
    counter["count"] += 1
    assert counter["count"] == 1


def test_counter_increment_2(counter):
    counter["count"] += 1
    assert counter["count"] == 1
