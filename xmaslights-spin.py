# TODO: to change scene just import a different one
from scenes.growing_sphere import render_point, tick, set_palette_mode

import numpy as np


def xmaslight():
    # This is the code from my 

    # NOTE THE LEDS ARE GRB COLOUR (NOT RGB)

    # Here are the libraries I am currently using:
    import time
    import board
    import neopixel
    import re

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

    set_palette_mode(grb=True)

    # I couldn't test this directly unfortunately...
    # TODO: actually test it
    global points      # this should be an np.array
    global neo_pixels  # this should support assigning an np.array
    points = np.ndarray(coords)
    neo_pixels = pixels

    iterator = range(0, 500)
    ns_to_s = 1000000000
    last_time = time.time_ns() / ns_to_s  # seconds
    last_update = round(last_time)
    while True:
        tick(time.time_ns())

        # This is an array of colors
        colors = render_point(points)
        # TODO: assign all colors at once, no idea how... This part is probably a big bottleneck
        for i in range(len(colors)):
            pixels[i] = colors[i]
        pixels.show()

        t = time.time_ns() / ns_to_s  # seconds
        if last_update != round(t):
            # print FPS to console (I got around 5000 for the sphere scene)
            print(f"{round(60 / (t - last_time))} FPS")
            last_update = round(t)
        last_time = t


# yes, I just put this at the bottom so it auto runs
xmaslight()
