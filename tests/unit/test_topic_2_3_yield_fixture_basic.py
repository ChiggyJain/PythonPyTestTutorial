import pytest


# here scope=function is by default then it will be created/destory for each test-function
# each test-function will get a fresh fixture data
@pytest.fixture
def resource():
    print("\nSETUP: creating resource")
    data = {"status": "active"}
    yield data
    print("\nTEARDOWN: cleaning resource")
    data.clear()

def test_resource_usage(resource):
    assert resource["status"] == "active"
    