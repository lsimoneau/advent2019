from itertools import tee


def _pairwise(iterable):
    x, y = tee(iterable)
    next(y, None)
    return list(zip(x, y))

def _rle(password: str):
    count = 1
    previous = ""
    mapping = list()

    for character in password:
        if character != previous:
            if previous:
                mapping.append((previous, count))
            count = 1
            previous = character
        else:
            count += 1
    else:
        mapping.append((character, count))

    return mapping


def check(password: str) -> bool:
    pairs = _pairwise(int(x) for x in password)
    rle = _rle(password)
    return all(y >= x for (x, y) in pairs) and any(x == 2 for (i, x) in rle)


if __name__ == "__main__":
    print(len([x for x in range(357253, 892943) if check(str(x))]))
