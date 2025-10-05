from string_calculator.calculator import add

def test_returns_zero_for_empty_string():
    assert add("") == 0

def test_returns_single_number_value():
    assert add("1") == 1

def test_adds_two_numbers():
    assert add("1,2") == 3
