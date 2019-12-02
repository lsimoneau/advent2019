from advent.intcode import compute, run


def test_compute():
    assert compute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]


def test_mult():
    assert compute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]


def test_mult_term():
    assert compute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


def test_more_ops():
    assert compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_whole_program():
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip('\n').split(',')
        code = [int(symbol) for symbol in symbols]
        output = run(code, 12, 2)
        assert output == 5534943


def test_program_doesnt_mutate_input():
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip('\n').split(',')
        code = [int(symbol) for symbol in symbols]
        orig = code.copy()
        run(code, 12, 2)
        assert code == orig
