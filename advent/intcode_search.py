import advent.intcode as intcode


def __main__():
    with open("input/02.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]

        for input_1 in range(0, 100):
            for input_2 in range(0, 100):
                output = intcode.run(code, input_1, input_2)
                if output == 19690720:
                    print(100 * input_1 + input_2)


if __name__ == "__main__":
    __main__()
