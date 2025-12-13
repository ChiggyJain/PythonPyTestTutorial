
# here sample_user is fixture and scope is given at function level and its defined in conftest.py file
# here sample_user is fixture and its become parameter of this test-function-cases 
def test_shared_user_name(sample_user):
    assert sample_user["name"] == "Chirag"


# here sample_user is fixture and scope is given at function level and its defined in conftest.py file
# here sample_user is fixture and its become parameter of this test-function-cases
def test_shared_user_role(sample_user):
    assert sample_user["role"] == "admin"
