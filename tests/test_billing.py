from billing import charge


def test_standard_charge():
    assert charge(10, False) == 30


def test_premium_charge():
    assert charge(10, True) == 20
