from typing import List, Tuple
from math import atan2


def parse_map(textmap: str) -> List[Tuple[int, int]]:
    asteroids = []
    for row_num, row in enumerate(textmap.splitlines()):
        for col_num, char in enumerate(row):
            if char == "#":
                asteroids.append((col_num, row_num))

    return asteroids


def best_station(textmap: str) -> int:
    asteroids = parse_map(textmap)
    return max([_can_see(a, asteroids) for a in asteroids])


def _can_see(vantage, asteroids):
    x, y = vantage
    angles = [atan2(y2 - y, x2 - x) for (x2, y2) in asteroids]
    return len(set(angles))

def __main__():
    with open("input/09.txt") as file_input:
        asteroids = file_input.read()
        print(best_station(asteroids))


if __name__ == "__main__":
    __main__()
