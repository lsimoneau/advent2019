from advent.recursive_fuel_sum import fuel


def test_simple_fuel():
    assert fuel(14) == 2


def test_big():
    assert fuel(1969) == 966


def test_bigger():
    assert fuel(100756) == 50346
