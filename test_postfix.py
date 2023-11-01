from postfix import evaluate

def test_single_operand():
    assert evaluate("10") == 10
