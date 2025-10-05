from string_calculator.calculator import add

def test_returns_zero_for_empty_string():
    assert add("") == 0