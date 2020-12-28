from scene1 import render_point, tick
from concurrent import futures

import numpy as np


def worker(index: int):
    neo_pixels[index] = render_point(points[index])


points = np.ndarray()
neo_pixels = []


def xmaslight():
    # This is the code from my 

    # NOTE THE LEDS ARE GRB COLOUR (NOT RGB)

    # Here are the libraries I am currently using:
    import time
    import board
    import neopixel
    import re
    import math

    # You are welcome to add any of these:
    # import random
    # import numpy
    # import scipy
    # import sys

    # If you want to have user changable values, they need to be entered from the command line
    # so import sys sys and use sys.argv[0] etc
    # some_value = int(sys.argv[0])

    # IMPORT THE COORDINATES (please don't break this bit)

    coord_filename = "Python/coords.txt"

    fin = open(coord_filename, 'r')
    coords_raw = fin.readlines()

    coords_bits = [i.split(",") for i in coords_raw]

    coords = []

    for slab in coords_bits:
        new_coord = []
        for i in slab:
            new_coord.append(int(re.sub(r'[^-\d]', '', i)))
        coords.append(new_coord)

    # set up the pixels (AKA 'LEDs')
    PIXEL_COUNT = len(coords)  # this should be 500

    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)

    # YOU CAN EDIT FROM HERE DOWN

    global points
    global neo_pixels
    points = np.ndarray(coords)
    neo_pixels = pixels

    # maximum parallel processes
    workers = 40
    while True:
        tick(time.time_ns())

        # process each pixel in parallel
        with futures.ProcessPoolExecutor(max_workers=workers) as pool:
            results = [pool.submit(render_point, i) for i in pixels]
            futures.as_completed(results)
            pixels.show()


# yes, I just put this at the bottom so it auto runs
xmaslight()
