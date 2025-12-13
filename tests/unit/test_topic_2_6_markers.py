import sys
import pytest
from app.calculator import add


# here unit is custom-market which is defined in pytest.ini file and this test-function have label-name=unit
@pytest.mark.unit
def test_add_unit_marker1():
    assert add(2, 2) == 4

# here unit is custom-market which is defined in pytest.ini file and this test-function have label-name=unit
@pytest.mark.unit
def test_add_unit_marker2():
    assert add(2, 3) == 5    


# here slow is custom-market which is defined in pytest.ini file and this test-function have label-name=slow
@pytest.mark.slow
def test_add_slow_marker1():
    assert add(100, 200) == 300

# here slow is custom-market which is defined in pytest.ini file and this test-function have label-name=slow
@pytest.mark.slow
def test_add_slow_marker2():
    assert add(100, 200) == 300    


# here mark.skip is inbuilt means, this test-function will be not executed in any scenario
@pytest.mark.skip(reason="Temporarily disabled")
def test_skip_example():
    assert False    

# here mark.skipif is inbuilt means, this test-function will be executed in any scenario whose system-platform is not windows-32 bit only
@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True    

@pytest.mark.xfail(reason="Known bug: division rounding issue")
def test_known_failure():
    assert 0.1 + 0.2 == 0.3