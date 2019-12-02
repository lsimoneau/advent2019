from typing import List


def __main__() -> None:
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip('\n').split(',')
        code = [int(symbol) for symbol in symbols]
        output = run(code, 12, 2)
        print(output)


def run(code: List[int], input_1: int, input_2: int) -> int:
    program = code.copy()
    program[1] = input_1
    program[2] = input_2
    output = compute(program)
    return output[0]


def compute(program: List[int]) -> List[int]:
    cursor = 0
    opcode = 0

    while True:
        opcode = program[cursor]
        if opcode == 99:
            return program

        x, y, target = program[cursor + 1], program[cursor + 2], program[cursor + 3]
        if opcode == 1:
            program[target] = program[x] + program[y]
        elif opcode == 2:
            program[target] = program[x] * program[y]

        cursor += 4


if __name__ == "__main__":
    __main__()
