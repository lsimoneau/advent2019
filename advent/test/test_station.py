from advent.station import parse_map, best_station


def test_parse_map():
    asteroids = """\
.#..#
.....
#####
....#
...##
        """
    locs = parse_map(asteroids)
    assert locs == [
        (1, 0),
        (4, 0),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (4, 3),
        (3, 4),
        (4, 4),
    ]


def test_best_station():
    asteroids = """\
.#..#
.....
#####
....#
...##
        """

    assert best_station(asteroids) == 8


def test_best_station_2():
    asteroids = """\
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
        """

    assert best_station(asteroids) == 33


def test_best_station_3():
    asteroids = """\
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
        """

    assert best_station(asteroids) == 35


def test_best_station_4():
    asteroids = """\
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
        """

    assert best_station(asteroids) == 210
