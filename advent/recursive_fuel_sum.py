import math
from typing import List


def __main__() -> None:
    with open('input/01.txt') as file_input:
        lines = file_input.readlines()
        print(sum_fuel([int(line) for line in lines]))



def fuel(mass: int) -> int:
    total = 0
    increment = _weight_calc(mass)
    while increment > 0:
        total += increment
        increment = _weight_calc(increment)

    return total


def _weight_calc(mass: int) -> int:
    return math.floor(mass / 3) - 2


def sum_fuel(component_weights: List[int]) -> int:
    return sum([fuel(weight) for weight in component_weights])


if __name__ == "__main__":
    __main__()
