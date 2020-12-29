import numpy as np


def conical_gradient(p: np.array) -> np.float:
    """
    Draws a conical gradient 0..1 around the z axis
    :param p: vec3 position
    :return: float 0..1
    """
    return 0.5*(np.sign(p[0]) > 0) + np.interp()