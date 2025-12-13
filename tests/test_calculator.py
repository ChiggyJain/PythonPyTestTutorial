
import pytest
from app.calculator import add, divide


# file-name: start-with test_ is inbuilt discovery for pytest to identify test-file automatically
# function name start-with test_ is inbuilt discovery for pytest to identify test-case automatically inside the file
def test_add_two_positive_number():
    result = add(5,10)
    # assert is the inbuild keyword and its do work like truth condition 
    # (== (equality), != (in-equality), (>=, >, <, <=), in (membership))
    # assert condition-expression-statement
    assert result == 15

def test_divide_success():
    assert divide(10,5) == 2