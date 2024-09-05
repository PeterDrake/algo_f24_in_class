from gcd import gcd


def test_finds_gcd_when_a_less():
    assert gcd(10, 16) == 2


def test_finds_gcd_when_a_greater():
    assert gcd(20, 12) == 4


def test_finds_gcd_when_a_is_exact_divisor():
    assert gcd(5, 35) == 5
