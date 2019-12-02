from advent.fuel_sum import sum_fuel, fuel


def test_simple_fuel():
    assert fuel(12) == 2


def test_rounding():
    assert fuel(14) == 2


def test_big():
    assert fuel(1969) == 654


def test_bigger():
    assert fuel(100756) == 33583


def test_sum_fuel():
    assert sum_fuel([12, 14, 1969, 100756]) == 34241
