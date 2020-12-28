import numpy as np

from sdf_primitives import euclidean_length

# Most of the these functions are based on these:
# https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm

# convenience
x = 0
y = 1
z = 2
r = 2
g = 0
b = 1

# important: 'p' is called position, but is the coordinate of the current sample point. Don't try to pass a static
# value there.


def elongate(p: np.array, h: np.array) -> np.array:
    """
    Elongates space along the specified axis
    :param p: vec3 position
    :param h: vec3 elongation axis (and length)
    :return: elongated space
    """
    q = np.zeros(3)
    np.clip(p, -h, h, out=q)
    return q


# fuck shadowing
def round(sdf: np.float, radius: np.float) -> np.float:
    """
    Rounds a shape
    :param sdf: pre-calculated SDF
    :param radius: radius
    :return: SDF
    """
    return sdf - radius


def onion(sdf: np.float, thickness: np.float) -> np.float:
    """
    Slices the interior of a shape into concentric layers
    :param sdf: pre-calculated SDF
    :param thickness: thickness of the slices
    :return: SDF
    """
    return np.abs(sdf) - thickness


def extrude_2d_sdf(p: np.array, sdf: np.float, h: float) -> np.float:
    """
    Extrudes a 2D SDF along the z axis
    :param p: position
    :param sdf: pre-calculated 2D SDF
    :param h: extrusion height
    :return: SDF
    """
    w = np.array([sdf, np.abs(p[z]), h])
    return np.minimum(np.maximum(w[x], w[y]), 0) + euclidean_length(np.maximum(w, 0.0))


# TODO
# def revolute_2d_sdf


def union(sdf1: np.float, sdf2: np.float) -> np.float:
    """
    Performs a union operation on two SDFs
    :param sdf1: SDF
    :param sdf2: SDF
    :return: SDF
    """
    return np.minimum(sdf1, sdf2)


def difference(sdf1: np.float, sdf2: np.float) -> np.float:
    """
    Performs a difference sdf1 - sdf2
    :param sdf1: SDF
    :param sdf2: SDF
    :return: SDF
    """
    return np.maximum(-sdf1, sdf2)


def intersection(sdf1: np.float, sdf2: np.float) -> np.float:
    """
    Performs an intersection of two SDFs
    :param sdf1: SDF
    :param sdf2: SDF
    :return: SDF
    """
    return np.maximum(sdf1, sdf2)


def transform(p: np.array, t: np.ndarray) -> np.array:
    """
    Transform space
    :param p: vec3 position
    :param t: rotation or translation matrix
    :return: vec3 position
    """
    return np.invert(t)*p


def infinite_repetition(p: np.array, c: np.array) -> np.array:
    """
    Repeat object in 3d space
    :param p:
    :param c:
    :return:
    """
