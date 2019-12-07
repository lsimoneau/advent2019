from advent.password_groups import check


def test_check_ok():
    assert check("112233")


def test_check_decreasing():
    assert check("223450") is False


def test_check_repeat_group():
    assert check("123444") is False


def test_check_repeat_no_group():
    assert check("111122")
