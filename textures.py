from lib import np
import quaternion

# convenience
from sdf_primitives import euclidean_length

x = 0
y = 1
z = 2
w = 3


def conical_gradient(p: np.array) -> np.float:
    """
    TODO
    Draws a conical gradient 0..1 around the z axis
    :param p: vec3 position
    :return: float 0..1
    """
    return 0.5 * (np.sign(p[0]) > 0) + np.interp()


julia_iterations = range(11)


def julia(p: np.array, c: quaternion) -> np.float:
    """
    Julia set SDF
    :param p: vec3 position=
    :param c: vec4
    :return: float SDF
    """
    p = quaternion.as_quat_array(np.concatenate((p, np.zeros((p.shape[0], 1))), axis=1))

    for i in julia_iterations:
        p = np.array([quaternion.quaternion.square(i) for i in p]) + c

    return euclidean_length(quaternion.as_float_array(p))
