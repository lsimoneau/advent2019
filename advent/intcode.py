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
        if self.opcode == 3 or self.opcode == 4 or self.opcode == 9:
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


async def compute(program: List[int], user_in=None, user_out=None) -> List[int]:
    program = program + [0] * (100000 - len(program))
    cursor = 0
    relative_base = 0

    # test case for 2102
    while True:
        instruction = Instruction(program[cursor])
        if instruction.opcode == 99:
            return program

        if instruction.modes[2] == 0:
            x = program[cursor + 1]
        elif instruction.modes[2] == 2:
            x = program[cursor + 1] + relative_base
        else:
            x = cursor + 1

        if instruction.size > 2:
            if instruction.modes[1] == 0:
                y = program[cursor + 2]
            elif instruction.modes[1] == 2:
                y = program[cursor + 2] + relative_base
            else:
                y = cursor + 2

        if instruction.size > 3:
            if instruction.modes[0] == 0:
                target = program[cursor + 3]
            elif instruction.modes[0] == 2:
                target = program[cursor + 3] + relative_base
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
            await user_out.put(program[x])
        elif instruction.opcode == 7:
            program[target] = int(program[x] < program[y])
        elif instruction.opcode == 8:
            program[target] = int(program[x] == program[y])
        elif instruction.opcode == 9:
            relative_base += program[x]

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
