from sdf_primitives import *
from sdf_ops import *


# keyframe values
rotation = np.float(100)


def tick(t: float):
    global rotation
    rotation = (1 + np.sin(t)) % (2 * np.pi)


# palette in RGB
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])


def render_point(p: np.array) -> np.array:
    # render a sphere with radius 100
    return colorize(red, blue, sphere(p, rotation))


def set_palette_mode(grb: bool):
    if not grb:
        return

    for element in [red, green, blue]:
        element[[g, r, b]] = element[[r, g, b]]
