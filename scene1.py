from sdf_primitives import *
from sdf_ops import *


# keyframe values
sphere_radius = np.float(100)


def tick(t: float):
    global sphere_radius
    sphere_radius = 100*np.sin(t/100)


# palette
red = np.array([0, 1, 0])
blue = np.array([0, 0, 1])
green = np.array([1, 0, 0])


def render_point(p: np.array) -> np.array:
    # render a sphere with radius 100
    return colorize(red, blue, sphere(p, 100))
