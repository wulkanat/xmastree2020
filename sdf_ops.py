import numpy as np

from sdf_primitives import euclidean_length

# Most of the these functions are based on these:
# https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm

# convenience
x = 0
y = 1
z = 2
r = 1
g = 0
b = 2

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


def rotate(p: np.array, axis: np.array, theta: np.float) -> np.array:
    """
    Rotate around three angles
    :param p: vec3 position
    :param axis: unit vec3 axis to rotate around
    :param theta: angle to rotate around axis
    :return: vec3
    """
    return p*np.cos(theta)+(np.cross(axis, p)*np.sin(theta)+axis*(axis*p)*(1-np.cos(theta)))


def normalize(v):
    """
    Normalize a vector
    """
    return v / (v**2).sum()**0.5


def position(p, t: np.array) -> np.array:
    """
    Position
    :param p: vec3 position
    :param t: vec3 transform
    :return: vec3
    """
    return p + t


def infinite_repetition(p: np.array, c: np.array) -> np.array:
    """
    Repeat object in 3d space
    :param p:
    :param c:
    :return:
    """
    # TODO


def evaluate_sdf(sdf: np.float) -> bool:
    return sdf > 0.0


def colorize(inside: np.array, outside: np.array, sdf: np.float) -> np.array:
    """
    Colorizes an SDF
    :param inside: color on the inside of the shape
    :param outside: color on the outside of the shape
    :param sdf: the signed distance field
    :return: color
    """
    val = np.moveaxis(np.array([sdf < 0]), 0, 1)
    # if
    return inside*val+(1-val)*outside
