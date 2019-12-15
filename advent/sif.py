def slices(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def __main__():
    with open("input/07.txt") as file_input:
        pixels = [int(i) for i in file_input.read().strip("\n")]

        layers = slices(pixels, 150)

        layer = min(layers, key=lambda l: l.count(0))

        print(layer.count(1) * layer.count(2))

if __name__ == "__main__":
    __main__()
