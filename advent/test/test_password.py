from advent.password import check


def test_check_ok():
    assert check("111111")


def test_check_decreasing():
    assert check("223450") is False


def test_check_repeat():
    assert check("123789") is False
