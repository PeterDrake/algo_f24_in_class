from brute import BruteForceSearch

def test_matches():
    matcher = BruteForceSearch("cad")
    assert matcher.match("abracadabra") == 4

def test_doesnt_match():
    matcher = BruteForceSearch("lol")
    assert matcher.match("abracadabra") == -1

def test_finds_missing_match_overlapping_end():
    matcher = BruteForceSearch('brad')
    assert matcher.match("abracadabra") == -1

def test_finds_both_same():
    matcher = BruteForceSearch('abracadabra')
    assert matcher.match("abracadabra") == 0
    