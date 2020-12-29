from sdf_primitives import *
from sdf_ops import *
from textures import *


# keyframe values
c = quaternion.quaternion()


def tick(t: float):
    global c
    # TODO
    c = quaternion.as_quat_array(np.zeros((3000, 4)))


# palette in RGB
red = np.array([1, 0, 0])
green = np.array([0, 1, 0])
blue = np.array([0, 0, 1])


def render_point(p: np.ndarray) -> np.ndarray:
    """
    Render one or all points
    :param p: array of points
    :return: array of colors
    """
    j = julia(p*500, c) / 200
    return color_of(blue, j)


def set_palette_mode(grb: bool):
    if not grb:
        return

    for element in [red, green, blue]:
        element[[g, r, b]] = element[[r, g, b]]
