import numpy as np

def hb_normalized_points(point_A, point_B, point_C, point_D, point_E, point_offside_E, point_nearside_E, point_flux):
    """calculate sum of weighted points given by TC-45 for HB

    Returns:
        [int]: [normalized points]
    """
    # given by TC-45
    best = 19.230
    worst = 11.31
    weights = np.array([2, 0.8, 0.4, 0.8, 1, 1, 1, 1])

    points = np.array([point_A, point_B, point_C, point_D, point_E, point_offside_E, point_nearside_E, point_flux])
    weighted_sum = np.sum(np.multiply(points, weights))
    result = np.around(np.multiply(np.divide(4, best-worst), weighted_sum-worst)+1, decimals=2)
    return result