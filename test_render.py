#
# THIS IS NOT REQUIRED TO RENDER, IT'S JUST A PREVIEW
#

from scene1 import render_point, tick
from concurrent import futures

import numpy as np
import open3d as o3d


def worker(index: int):
    np.asarray(neo_pixels.colors)[index] = render_point(neo_pixels.points[index])


def xmaslight():
    # This is the code from my

    # NOTE THE LEDS ARE GRB COLOUR (NOT RGB)

    # Here are the libraries I am currently using:
    import time
    import board
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

    coord_filename = "coords.txt"

    fin = open(coord_filename, 'r')
    coords_raw = fin.readlines()

    coords_bits = [i.split(",") for i in coords_raw]

    coords = []

    for slab in coords_bits:
        new_coord = []
        for i in slab:
            new_coord.append(int(re.sub(r'[^-\d]', '', i)))
        coords.append(new_coord)

    # YOU CAN EDIT FROM HERE DOWN

    global neo_pixels
    global vis
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    neo_pixels = o3d.geometry.PointCloud()
    neo_pixels.points = o3d.utility.Vector3dVector(np.asarray(coords))
    neo_pixels.colors = o3d.utility.Vector3dVector(np.asarray(coords))
    vis.add_geometry(neo_pixels)
    vis.poll_events()

    # maximum parallel processes
    iterator = range(0, 500)
    workers = 40
    last_time = time.time_ns()
    while True:
        tick(time.time_ns())

        # TODO: parallel
        # process each pixel in parallel
        # with futures.ProcessPoolExecutor(max_workers=workers) as pool:
        #    for i in iterator:
        #        pool.submit(render_point, i)
        for i in iterator:
            worker(i)
        vis.update_geometry(neo_pixels)
        vis.update_renderer()
        vis.poll_events()

        print(f"{60 / ((time.time_ns() - last_time) / 1000000)} FPS")
        # lil loss here but who cares
        last_time = time.time_ns()
# yes, I just put this at the bottom so it auto runs


xmaslight()
