from advent.crossed_wires import Wire


def test_points_visited():
    wire = Wire("U1")
    assert wire.points_visited() == [(0, 1)]


def test_points_visited_with_path():
    wire = Wire("U3")
    assert wire.points_visited() == [(0, 1), (0, 2), (0, 3)]


def test_points_visited_with_turn():
    wire = Wire("U3,L1")
    assert wire.points_visited() == [(0, 1), (0, 2), (0, 3), (-1, 3)]


def test_points_visited_with_right():
    wire = Wire("R1,U3,L1")
    assert wire.points_visited() == [(1, 0), (1, 1), (1, 2), (1, 3), (0, 3)]


def test_points_visited_with_down():
    wire = Wire("R1,U3,L1,D2")
    assert wire.points_visited() == [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (0, 3),
        (0, 2),
        (0, 1),
    ]


def test_intersections():
    wire1 = Wire("R8,U5,L5,D3")
    wire2 = Wire("U7,R6,D4,L4")
    assert wire1.intersection(wire2) == {(3, 3), (6, 5)}

def test_closest_intersection_simple():
    wire1 = Wire("R8,U5,L5,D3")
    wire2 = Wire("U7,R6,D4,L4")

    assert wire1.closest_intersection(wire2) == 6


def test_closest_intersection():
    wire1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    wire2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")

    assert wire1.closest_intersection(wire2) == 159

def test_closest_intersection_2():
    wire1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    wire2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

    assert wire1.closest_intersection(wire2) == 135

def test_closest_intersection_steps():
    wire1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    wire2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")

    assert wire1.closest_intersection(wire2, method="steps") == 610

def test_closest_intersection_steps_2():
    wire1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    wire2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

    assert wire1.closest_intersection(wire2, method="steps") == 410
