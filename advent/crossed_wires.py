from typing import List, Tuple


class Wire:
    def __init__(self, definition: str):
        self.directions = definition.split(",")

    def points_visited(self) -> List[Tuple[int, int]]:
        location = (0, 0)
        points = []
        for direction in self.directions:
            if direction[0] == "U":
                new_points = [
                    (location[0], x)
                    for x in range(
                        location[1] + 1, location[1] + int(direction[1:]) + 1
                    )
                ]
                location = new_points[-1]
                points.extend(new_points)
            if direction[0] == "D":
                new_points = [
                    (location[0], x)
                    for x in range(
                        location[1] - 1, location[1] - int(direction[1:]) - 1, -1
                    )
                ]
                location = new_points[-1]
                points.extend(new_points)
            elif direction[0] == "L":
                new_points = [
                    (x, location[1])
                    for x in range(
                        location[0] - 1, location[0] - int(direction[1:]) - 1, -1
                    )
                ]
                location = list(new_points)[-1]
                points.extend(new_points)
            elif direction[0] == "R":
                new_points = [
                    (x, location[1])
                    for x in range(
                        location[0] + 1, location[0] + int(direction[1:]) + 1
                    )
                ]
                location = list(new_points)[-1]
                points.extend(new_points)

        return points

    def intersection(self, other):
        return set(self.points_visited()).intersection(other.points_visited())

    def closest_intersection(self, other, method: str = "distance"):
        if method == "distance":
            return min([abs(x[0]) + abs(x[1]) for x in self.intersection(other)])
        elif method == "steps":
            my_path = self.points_visited()
            other_path = other.points_visited()

            return min(
                [
                    my_path.index(x) + other_path.index(x) + 2
                    for x in self.intersection(other)
                ]
            )


if __name__ == "__main__":
    with open("input/03.txt") as file:
        LINES = [line.strip("\n") for line in file.readlines()]
        print(Wire(LINES[0]).closest_intersection(Wire(LINES[1]), method="steps"))
