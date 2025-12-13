import pytest


# here in this file we define common fixtures and no test-function-cases definition
# tests/conftest.py means visible to All tests
# tests/unit/conftest.py means visible to Only unit tests
# tests/integration/conftest.py means visible to Only integration tests

# here scope=function is by default then it will be created/destory for each test-function
# each test-function will get a fresh fixture data
@pytest.fixture
def sample_user():
    return {
        "id": 1,
        "name": "Chirag",
        "role": "admin"
    }
