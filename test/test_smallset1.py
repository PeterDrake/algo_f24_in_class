from smallset1 import mySet


def test_add_works():
    a = mySet()
    a.add(1)
    a.add(4)
    assert a.contains(1) == True
    assert a.contains(4) == True

def test_remove_works():
    a = mySet()
    a.add(10)
    a.remove(10)
    assert a.contains(10) == False

def test_contains_works():
    a = mySet()
    a.add(12)
    assert a.contains(12) == True
    assert a.contains(11) == False
