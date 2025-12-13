import pytest


# A reusable function that prepares data or state before a test runs.
# Fixture name will be become function argument for test-case
# (Finds fixture function -> Runs fixture first -> Injects return value into test -> Runs test -> Cleans up (if needed))
@pytest.fixture
def sample_user():
    return {
        "id": 1,
        "name": "Chirag",
        "role": "admin"
    }

# here sample_user argument is fixture and automatically injected in this test-case
def test_user_name(sample_user):
    assert sample_user["name"] == "Chirag"

# here sample_user argument is fixture and automatically injected in this test-case
def test_user_role(sample_user):
    assert sample_user["role"] == "admin"    