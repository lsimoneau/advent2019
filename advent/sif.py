def slices(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def __main__():
    with open("input/07.txt") as file_input:
        pixels = [int(i) for i in file_input.read().strip("\n")]
