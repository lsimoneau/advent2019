import asyncio
from advent.intcode import run_io


async def __main__() -> None:
    with open("input/08.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        output = await run_io([2], code)
        print(output)


if __name__ == "__main__":
    asyncio.run(__main__())
