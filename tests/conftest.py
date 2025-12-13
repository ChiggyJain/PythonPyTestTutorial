import pytest


# here in this file we define common fixtures and no test-function-cases definition


# here scope=function is by default then it will be created/destory for each test-function
# each test-function will get a fresh fixture data
@pytest.fixture
def sample_user():
    return {
        "id": 1,
        "name": "Chirag",
        "role": "admin"
    }
