import itertools
from advent.intcode import compute, compute_io
from io import StringIO
import asyncio


async def signal(program, settings):
    init = 0
    for setting in settings:
        output = await compute_io([setting, init], program)
        init = output

    return output


async def feedback_signal(program, settings):
    q1 = asyncio.Queue()
    q1.put_nowait(settings[0])
    q1.put_nowait(0)
    q2 = asyncio.Queue()
    q2.put_nowait(settings[1])
    q3 = asyncio.Queue()
    q3.put_nowait(settings[2])
    q4 = asyncio.Queue()
    q4.put_nowait(settings[3])
    q5 = asyncio.Queue()
    q5.put_nowait(settings[4])

    amp_a = asyncio.create_task(compute(program, q1, q2))
    amp_b = asyncio.create_task(compute(program, q2, q3))
    amp_c = asyncio.create_task(compute(program, q3, q4))
    amp_d = asyncio.create_task(compute(program, q4, q5))
    amp_e = asyncio.create_task(compute(program, q5, q1))

    await asyncio.gather(amp_a, amp_b, amp_c, amp_d, amp_e)

    return q1.get_nowait()


async def max_signal(program):
    signals = []
    for settings in itertools.permutations([0, 1, 2, 3, 4]):
        next_sig = await signal(program, settings)
        signals.append(next_sig)

    return max(signals)


async def feedback_max_signal(program):
    signals = []
    for settings in itertools.permutations([5, 6, 7, 8, 9]):
        next_sig = await feedback_signal(program, settings)
        signals.append(next_sig)

    return max(signals)


async def __main__():
    with open("input/06.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        code = [int(symbol) for symbol in symbols]
        print(await feedback_max_signal(code))


if __name__ == "__main__":
    asyncio.run(__main__())
