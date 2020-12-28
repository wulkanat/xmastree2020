from sdf_primitives import *
from sdf_ops import *


# keyframe values
sphere_radius = np.float(100)


def tick(t: float):
    global sphere_radius
    sphere_radius = 200*(1+np.sin(t))


# palette in RGB
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])


def render_point(p: np.array) -> np.array:
    # render a sphere with radius 100
    return colorize(red, blue, sphere(p, sphere_radius))


def set_palette_mode(grb: bool):
    if not grb:
        return

    for element in [red, green, blue]:
        element[[g, r, b]] = element[[r, g, b]]
