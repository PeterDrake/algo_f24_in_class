from union import WeightedQuickUnion


def test_example():
    u = WeightedQuickUnion(8)
    u.union(1, 3)
    u.union(5, 0)
    u.union(0, 6)
    u.union(4, 7)
    u.union(3, 5)
    assert u.parent == [5, 5, 2, 1, 4, 5, 5, 4]
    assert u.count == 3
    assert u.size[2] == 1
    assert u.size[5] == 5
    assert u.size[4] == 2
