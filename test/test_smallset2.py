from smallset2 import SmallSet

def test_adds():
    a = SmallSet()
    a.add(5)
    assert a.contains(5) == True
    assert a.contains(4) == False

def test_removes():
    a = SmallSet()
    a.add(5)
    a.add(99)
    assert a.contains(99) == True
    a.remove(99)
    assert a.contains(99) == False