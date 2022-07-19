import numpy as np

def compute_points(value, one_point, two_point):
    """ calculate the achieved points

    Args:
        value ([int]): [computed value]
        one_point ([int]): [mean + std]
        two_point ([int]): [mean - std]

    Returns:
        [int]: [the achieved points]
    """
    points = np.divide((value - one_point), (two_point-one_point))+1
    return points