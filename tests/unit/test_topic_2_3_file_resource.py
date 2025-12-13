import pytest
import os


# here scope=function is by default then it will be created/destory for each test-function
# each test-function will get a fresh fixture data
@pytest.fixture
def temp_file():
    # Before yield → SETUP/Opening process
    file_path = "temp_test_file.txt"
    with open(file_path, "w") as f:
        f.write("test data")
    # TEST RUNS    
    yield file_path
    # TEARDOWN/Shutdown process
    os.remove(file_path)


def test_file_content(temp_file):
    with open(temp_file) as f:
        assert f.read() == "test data"
