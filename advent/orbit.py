import re
import logging
from typing import Dict

LOGGER = logging.getLogger(__name__)


class Orbit:
    def __init__(self, orbit_dict: Dict[str, str]):
        self.orbital_map = orbit_dict

    def count_by_object(self, obj: str):
        try:
            parent = self.orbital_map[obj]
            return 1 + self.count_by_object(parent)
        except KeyError:
            return 0

    def count_total(self) -> int:
        return sum(map(self.count_by_object, self.orbital_map.keys()))

    def dist(self, orig: str, dest: str) -> int:
        obj_a = self.orbital_map[orig]
        obj_b = self.orbital_map[dest]

        dist = 0
        for x in self.parents(obj_a):
            dist += 1
            odist = 0
            for y in self.parents(obj_b):
                odist += 1
                if x == y:
                    return dist + odist

        return -1


    def parents(self, obj):
        try:
            parent = self.orbital_map[obj]
            yield parent
            yield from self.parents(parent)
        except KeyError:
            pass


    @classmethod
    def parse(cls, lines):
        pattern = re.compile(r'^(\w+)\)(\w+)$')
        orbital_map = {}

        for line in lines:
            matches = pattern.match(line)
            if matches:
                orbital_map[matches.group(2)] = matches.group(1)

        return cls(orbital_map)


if __name__ == "__main__":
    with open("input/05.txt") as file_input:
        LINES = file_input.readlines()
        #print(Orbit.parse(LINES).count_total())
        print(Orbit.parse(LINES).dist('YOU','SAN'))
