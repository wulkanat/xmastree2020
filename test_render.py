#
# THIS IS NOT REQUIRED TO RENDER, IT'S JUST A PREVIEW
#

from scenes.growing_sphere import render_point, tick, set_palette_mode

import numpy as np
import open3d as o3d

import time
import re


def xmaslight():
    # If you want to have user changable values, they need to be entered from the command line
    # so import sys sys and use sys.argv[0] etc
    # some_value = int(sys.argv[0])

    # IMPORT THE COORDINATES (please don't break this bit)

    # TODO: set this to true to use real light locations instead of generated cloud
    if False:
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
    else:
        size = 20000
        coords = (500*np.random.rand(size, 3)) - 250
        print(f"min: {coords.min()}, max: {coords.max()}")

    # YOU CAN EDIT FROM HERE DOWN

    vis = o3d.visualization.Visualizer()
    # TODO: remove left to display on primary monitor
    vis.create_window(width=1280, height=720, left=3000)
    neo_pixels = o3d.geometry.PointCloud()
    neo_pixels.points = o3d.utility.Vector3dVector(np.asarray(coords))
    neo_pixels.colors = o3d.utility.Vector3dVector(np.asarray(coords))
    vis.add_geometry(neo_pixels)
    vis.poll_events()

    set_palette_mode(grb=False)

    iterator = range(0, len(coords))
    ns_to_s = 1000000000
    last_time = time.time_ns() / ns_to_s  # seconds
    last_update = round(last_time)
    while True:
        tick(last_time)

        # This could be done in parallel, in this case I let numpy do it all in one go
        # so it should be pretty fast for Python standards
        neo_pixels.colors = o3d.utility.Vector3dVector(render_point(np.asarray(neo_pixels.points)))

        vis.update_geometry(neo_pixels)
        vis.update_renderer()
        vis.poll_events()

        t = time.time_ns() / ns_to_s  # seconds
        if last_update != round(t):
            print(f"{round(60 / (t - last_time))} FPS")
            last_update = round(t)
        last_time = t


if __name__ == '__main__':
    xmaslight()
