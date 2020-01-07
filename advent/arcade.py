import advent
import numpy as np
import asyncio
from intcode import compute
import os
import time

def render(screen):
    clear_console = 'clear' if os.name == 'posix' else 'CLS'
    outstr = ""

    for row in screen:
        for elem in row:
            if elem == 1:
                output += "#"
            elif elem == 2:
                output += "@"
            elif elem == 3:
                output += "_"
            elif elem == 4:
                output += "*"
            elif elem == 0:
                output += " "
    
        output += "\n"
    
    os.system(clear_console)

    sys.stdout.write(outstr)
    sys.stdout.flush()
    time.sleep(0.1)


async def __main__() -> None:
    with open("input/11.txt") as file_input:
        symbols = file_input.read().strip("\n").split(",")
        symbols[0] = 2
        code = [int(symbol) for symbol in symbols]

        iq = asyncio.Queue()
        oq = asyncio.Queue()
        task = asyncio.create_task(compute(code, iq, oq))

        screen = np.zeros((24,40))
        
        x = await oq.get()
        y = await oq.get()
        tile_id = await oq.get()
        screen[y][x] = tile_id
        
        while not oq.empty():
            x = await oq.get()
            y = await oq.get()
            tile_id = await oq.get()
            screen[y][x] = tile_id
                                    
            render(screen)

if __name__ == "__main__":
    asyncio.run(__main__())