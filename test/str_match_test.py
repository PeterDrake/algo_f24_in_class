from str_match import str_match

def test_str_match():
    assert str_match("abracadabra","cad") == 4

def test_str_match_beginning():
    assert str_match("abracadabra","abra") == 0

def test_str_match_end():
    assert str_match("abracadabra","dabra") == 6

def test_str_match_not_present():
    assert str_match("abracadabra","yab") == -1
