import asyncio
from advent.intcode import run_io, compute


async def __main__() -> None:
    with open("input/10.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]

        iq = asyncio.Queue()
        oq = asyncio.Queue()
        asyncio.create_task(compute(program, iq, oq))

        iq.put_nowait(i)
        return await oq.get()


        output = await run_io([2], code)
        print(output)


if __name__ == "__main__":
    asyncio.run(__main__())
