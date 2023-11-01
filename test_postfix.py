from postfix import evaluate

def test_single_operand():
    assert evaluate("9") == 9
def test_add():
    assert evaluate("63+") == 9
def test_sub():
    assert evaluate("63-") == 3
def test_sub1():
    assert evaluate("36-") == -3
def test_multiply():
    assert evaluate("23*") == 6
def test_division():
    assert evaluate("82/") == 4

def test_multiple_operations():
    assert evaluate("123+-") == -4

def test_modulus():
    assert evaluate("75%") == 2

def test_exponent():
    assert evaluate("23^") == 8


def test_complex_exp():
    assert evaluate("12*23+-") == -5