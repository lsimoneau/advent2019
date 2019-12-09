from io import StringIO
from typing import List
import asyncio

import logging

LOGGER = logging.getLogger(__name__)


class Instruction:
    def __init__(self, inst: int):
        padded = str(inst).zfill(5)
        self.opcode = int(padded[-2:])
        self.modes = int(padded[0]), int(padded[1]), int(padded[2])
        if self.opcode == 3 or self.opcode == 4:
            self.size = 2
        elif self.opcode == 5 or self.opcode == 6:
            self.size = 3
        else:
            self.size = 4


def __main__() -> None:
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        output = asyncio.run(run(code, 12, 2))
        print(output)


async def run(code: List[int], input_1: int, input_2: int) -> int:
    program = code.copy()
    program[1] = input_1
    program[2] = input_2
    output = await compute(program)
    return output[0]


async def run_io(inputs, program):
    iq = asyncio.Queue()
    oq = asyncio.Queue()
    asyncio.create_task(compute(program, iq, oq))
    for i in inputs:
        iq.put_nowait(i)
    return await oq.get()


async def compute_io(input_vals: List[int], program) -> int:
    my_input: asyncio.Queue = asyncio.Queue()
    my_output: asyncio.Queue = asyncio.Queue()

    for i in input_vals:
        my_input.put_nowait(i)

    task = asyncio.create_task(compute(program, my_input, my_output))
    return await my_output.get()


async def compute(program: List[int], user_in=None, user_out=None) -> List[int]:
    program = program.copy()
    cursor = 0

    while True:
        instruction = Instruction(program[cursor])
        if instruction.opcode == 99:
            return program

        if instruction.modes[2] == 0:
            x = program[cursor + 1]
        else:
            x = cursor + 1

        if instruction.modes[1] == 0:
            y = program[cursor + 2]
        else:
            y = cursor + 2

        if instruction.size > 2:
            if instruction.modes[0] == 0:
                target = program[cursor + 3]
            else:
                target = cursor + 3

        if instruction.opcode == 1:
            program[target] = program[x] + program[y]
        elif instruction.opcode == 2:
            program[target] = program[x] * program[y]
        elif instruction.opcode == 3:
            next_input = await user_in.get()
            program[x] = int(next_input)
        elif instruction.opcode == 4:
            user_out.put_nowait(program[x])
        elif instruction.opcode == 7:
            program[target] = int(program[x] < program[y])
        elif instruction.opcode == 8:
            program[target] = int(program[x] == program[y])

        if instruction.opcode == 5:
            if program[x] != 0:
                cursor = program[y]
            else:
                cursor += instruction.size
        elif instruction.opcode == 6:
            if program[x] == 0:
                cursor = program[y]
            else:
                cursor += instruction.size
        else:
            cursor += instruction.size


if __name__ == "__main__":
    __main__()
