import numpy as np
from func.compute_points import *

def weighted_sum(values, one_point, two_point):
    """Calculate the weighted sum

    Args:
        values ([list]): [Contains the result of the left and right headlamp]
        one_point ([float]): [one point for weight calculation]
        two_point ([float]): [two point for weight calculation]

    Returns:
        [list]: [actual and weighted results]
    """
    # find point on horizontal axis
    result = np.sum(values[0]+values[1])
    weight = np.around(compute_points(result, one_point, two_point), decimals=3)
    
    return np.around(result, decimals=3), np.around(weight, decimals=3)

