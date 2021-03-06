from sdf_primitives import *
from sdf_ops import *


# keyframe values
r1 = np.float(100)
r2 = np.float(100)


def tick(t: float):
    global r1
    global r2
    r1 = 100*(2+np.sin(t))
    r2 = 50*(2+np.cos(t))


# palette in RGB
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])


def render_point(p: np.array) -> np.array:
    # render a sphere with radius 100
    return colorize(red, blue, torus(p, np.array([r1, r2])))


def set_palette_mode(grb: bool):
    if not grb:
        return

    for element in [red, green, blue]:
        element[[g, r, b]] = element[[r, g, b]]
