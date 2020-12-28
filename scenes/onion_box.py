from sdf_primitives import *
from sdf_ops import *


# keyframe values
r1 = np.float(100)
r2 = np.float(100)


def tick(t: float):
    global r1
    global r2
    r1 = 5*(2+np.sin(t))
    r2 = np.pi*(2+np.cos(t))


# palette in RGB
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])

axis = normalize(np.array([0.5, 1, 2]))


def render_point(p: np.array) -> np.array:
    # render a sphere with radius 100
    return colorize(red, blue, onion(
        sphere(rotate(position(p, np.array([10, 50, 20])), axis, r2), 40),
        r1))


def set_palette_mode(grb: bool):
    if not grb:
        return

    for element in [red, green, blue]:
        element[[g, r, b]] = element[[r, g, b]]
