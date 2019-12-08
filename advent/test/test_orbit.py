from advent.orbit import Orbit

INPUT = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
""".splitlines()

ORBITS = {
    "L": "K",
    "K": "J",
    "J": "E",
    "F": "E",
    "E": "D",
    "I": "D",
    "D": "C",
    "C": "B",
    "H": "G",
    "G": "B",
    "B": "COM",
}

TRANSFER = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".splitlines()

def test_count_by_object():
    assert Orbit(ORBITS).count_by_object("D") == 3

def test_count_by_object_2():
    assert Orbit(ORBITS).count_by_object("L") == 7

def test_count_total():
    assert Orbit(ORBITS).count_total() == 42

def test_parse():
    assert Orbit.parse(INPUT).count_total() == 42

def test_transfer_dist():
    assert Orbit.parse(TRANSFER).dist('SAN', 'YOU') == 4
