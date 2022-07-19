import numpy as np

def adb_normalized_points(point_preA, point_preB, point_preC, point_preFlux, point_preGlare, point_onA, point_onB, point_onC, point_onFlux, point_onGlare):
    """calculate sum of weighted points given by TC-45 for ADB

    Returns:
        [int]: [normalized points]
    """
    # given by TC-45
    best = 20.81
    worst = 9.35
    weights = np.array([1.5, 1, 1, 0.5, 0.5, 1.5, 1, 1, 0.5, 0.5])

    points = np.array([point_preA, point_preB, point_preC, point_preFlux, point_preGlare, point_onA, point_onB, point_onC, point_onFlux, point_onGlare])
    weighted_sum = np.sum(np.multiply(points, weights))
    result = np.around(np.multiply(np.divide(4, best-worst), weighted_sum-worst)+1, decimals=2)
    return result