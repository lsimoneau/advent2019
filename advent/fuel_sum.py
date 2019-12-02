import math
from typing import List


def __main__() -> None:
    with open('input/01.txt') as file_input:
        lines = file_input.readlines()
        print(sum_fuel([int(line) for line in lines]))



def fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


def sum_fuel(component_weights: List[int]) -> int:
    return sum([fuel(weight) for weight in component_weights])


if __name__ == "__main__":
    __main__()
