import pytest
from string_calculator.calculator import add

def test_returns_zero_for_empty_string():
    assert add("") == 0

def test_returns_single_number_value():
    assert add("1") == 1

def test_adds_two_numbers():
    assert add("1,2") == 3

def test_adds_multiple_numbers():
    assert add("1,2,3,4") == 10
    
def test_supports_newline_as_delimiter():
    assert add("1\n2,3") == 6

def test_supports_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_raises_exception_for_negatives():
    with pytest.raises(Exception) as e:
        add("-1,2,-3")
    assert "negative numbers not allowed -1,-3" in str(e.value)
