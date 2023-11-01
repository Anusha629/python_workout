from postfix import evaluate

def test_single_operand():
    assert evaluate("9") == 9
def test_add():
    assert evaluate("63+") == 9
def test_sub():
    assert evaluate("63-") == 3
