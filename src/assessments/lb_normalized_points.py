import numpy as np

def lb_normalized_points(point_A, point_B, point_C, point_offside_D, point_nearside_D, point_offside_E, point_nearside_E, point_flux, point_glare):
    """Calculate sum of weighted points given by TC-45 for Low Beam

    Returns:
        [int]: [normalized points]
    """
    # given by TC4-45
    best = 17.61
    worst = 11.15
    weights = np.array([1.5, 1, 1, 0.75, 0.75, 0.5, 0.5, 1, 1])

    points = np.array([point_A, point_B, point_C, point_offside_D, point_nearside_D, point_offside_E, point_nearside_E, point_flux, point_glare])
    weighted_sum = np.sum(np.multiply(points, weights))
    result = np.around(np.multiply(np.divide(4, best-worst), weighted_sum-worst)+1, decimals=2)
    return result