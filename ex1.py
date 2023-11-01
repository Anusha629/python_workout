from workout import panagram 

def test_is_panagram():
    assert panagram("the quick brown fox jumps over the lazy dog")
    
def test_is_not_panagram():
    assert not panagram("the quick brown fox jumped over the lazy dog")
    
def test_empty_is_not_panagram():
    assert not panagram("")
    
    
