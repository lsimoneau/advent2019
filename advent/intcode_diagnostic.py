from io import StringIO
import advent.intcode as intcode


def __main__():
    with open("input/04.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        my_input = StringIO()
        my_output = StringIO()

        my_input.write('5\n')
        my_input.seek(0)
        intcode.compute(code, my_input, my_output)
        print(my_output.getvalue())



if __name__ == "__main__":
    __main__()
