import numpy as np

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


def euclidean_distance(pos1: np.array, pos2: np.array) -> np.float:
    """
    Calculates the euclidean distance between two n-dimensional vectors
    :param pos1: fist position
    :param pos2: second position
    :return: distance
    """
    return np.sqrt(np.sum(np.square(pos1 - pos2)))


def euclidean_length(vec: np.array) -> np.float:
    """
    Calculates the euclidean length of an n-dimensional vector
    :param vec: vector
    :return: length
    """
    return np.sqrt(np.sum(np.square(vec)))


def sphere(p: np.array, radius: np.float) -> np.float:
    """
    Sphere SDF
    :param p: vec3 position
    :param radius: radius
    :return: signed distance
    """
    return euclidean_length(p) - radius


def box(p: np.array, size: np.array) -> np.float:
    """
    Box SDF
    :param p: vec3 position
    :param size: vec3 size of the box in each direction
    :return: signed distance
    """
    q = np.abs(p) - size
    return euclidean_length(np.maximum(p, 0.0)) + np.minimum(np.maximum(q[x], np.maximum(q[y], q[z])), 0)


def torus(p: np.array, t: np.array) -> np.float:
    """
    Torus SDF
    :param p: vec3 position
    :param t: vec2 size
    :return: signed distance
    """
    q = np.array([euclidean_length(np.array([p[x], p[z]])) - t[x], p[y]])
    return euclidean_length(q) - t[y]


def capped_torus(p: np.array, sc: np.array, ra: np.float, rb: np.float) -> np.float:
    """
    Capped Torus
    Like a torus, but with a section cut out and the ends smooth and round
    :param p: vec3 position
    :param sc: vec2 size
    :param ra: radius 1
    :param rb: radius 2
    :return: signed distance
    """
    p[x] = np.abs(p[x])
    k = np.dot(np.array([p[x], p[y]]), sc) if sc[y]*p[x] > sc[x]*p[y] else euclidean_length(np.array([p[x], p[y]]))
    return np.sqrt(np.dot(p, p) + ra**2 - 2.0*ra*k) - rb


def infinite_cylinder(p: np.array, c: np.array) -> np.float:
    """
    Never tried this one, no idea how to use it.
    :param p:
    :param c:
    :return:
    """
    return euclidean_length(np.array([p[x], p[z]]) - np.array([c[x], c[y]])) - c[z]


def plane(p: np.array, n: np.array, h: np.float) -> np.float:
    """
    A 3D plane
    :param p: vec3 position
    :param n: normalized vec3 span
    :param h: thickness (I think)
    :return:
    """
    return np.dot(p, n) + h



