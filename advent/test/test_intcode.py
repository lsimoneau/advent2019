from advent.intcode import compute, run, run_io
import asyncio
import pytest

pytestmark = pytest.mark.asyncio


async def test_compute():
    assert await compute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]


async def test_mult():
    assert await compute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]


async def test_mult_term():
    assert await compute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


async def test_more_ops():
    assert await compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


async def test_parameter_modes():
    assert await compute([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]


async def test_negative_numbers():
    assert await compute([1101, 100, -1, 4, 0]) == [1101, 100, -1, 4, 99]


async def test_input():
    assert await run_io([42], [3, 0, 4, 0, 99]) == 42


async def test_equals():
    assert await run_io([8], [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]) == 1
    assert await run_io([9], [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]) == 0


async def test_less_than():
    assert await run_io([7], [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]) == 1
    assert await run_io([8], [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]) == 0
    assert await run_io([9], [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]) == 0


async def test_less_than_immediate():
    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    assert await run_io([7], program) == 1
    assert await run_io([8], program) == 0
    assert await run_io([9], program) == 0


async def test_equals_immediate():
    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    assert await run_io([7], program) == 0
    assert await run_io([8], program) == 1
    assert await run_io([9], program) == 0


async def test_jump():
    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    assert await run_io([0], program) == 0
    assert await run_io([8], program) == 1
    assert await run_io([9], program) == 1


async def test_jump_immediate():
    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    assert await run_io([0], program) == 0
    assert await run_io([8], program) == 1
    assert await run_io([9], program) == 1


async def test_big_program_jump():
    program = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]

    assert await run_io([0], program) == 999
    assert await run_io([8], program) == 1000
    assert await run_io([9], program) == 1001


async def test_whole_program():
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        output = await run(code, 12, 2)
        assert output == 5534943


async def test_program_doesnt_mutate_input():
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        orig = code.copy()
        await run(code, 12, 2)
        assert code == orig
