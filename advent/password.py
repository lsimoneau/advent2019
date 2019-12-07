from itertools import tee


def _pairwise(iterable):
    x, y = tee(iterable)
    next(y, None)
    return list(zip(x, y))


def check(password: str) -> bool:
    pairs = _pairwise(int(x) for x in password)
    return all(y >= x for (x, y) in pairs) and any(x == y for (x, y) in pairs)


if __name__ == "__main__":
    print(len([x for x in range(357253, 892943) if check(str(x))]))
