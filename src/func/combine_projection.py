import numpy as np

def combine_projection(left, right, distance_vertical, headlamp_width):
    """AI is creating summary for combine_projection

    Args:
        left ([ndarray]): [light distribution (LVK) of left headlamp]
        right ([ndarray]): [light distribution (LVK) of right headlamp]
        distance_vertical ([ndarray]): [the vertical distance of each point within the LVK data]
        headlamp_width ([float]): [width of headlamps]

    Returns:
        [array]: [the combine projection of the light distiburion on the surface, as well as, data used to plot the top view (contour plots)]
    """
    # length limit
    value = np.max(distance_vertical)
    index = np.where(distance_vertical==value)
    limit = index[0][0] + 1

    # resolution_v = 0.1
    resolution_v = 0.1
    resolution_h = 0.01
    # add half of headlight width 
    horizontal_limit = 50 + (headlamp_width/2)
    horizontal_resolution = np.arange(-horizontal_limit, horizontal_limit+resolution_h, resolution_h).reshape(1, -1)

    vertical_minimum = np.min(distance_vertical)
    vertical_maximum = distance_vertical[np.where(distance_vertical==value)[0][0]-1]
    vertical_resolution = np.arange(vertical_minimum, vertical_maximum+resolution_v, resolution_v).reshape(-1, 1)
    horizontal_matrix = np.repeat(horizontal_resolution, right.shape[0], axis=0)
    # vertical_matrix = np.repeat(distance_vertical[:limit].reshape(-1,1), horizontal_matrix.shape[1], axis=1)
    vertical_matrix = np.repeat(vertical_resolution, horizontal_matrix.shape[1], axis=1)

    E_left = np.zeros((left.shape[0], horizontal_resolution.shape[1]))
    E_right = np.zeros((right.shape[0], horizontal_resolution.shape[1]))

    
    E_left[:,:right.shape[1]] = left
    E_right[:,(-1-right.shape[1])+1:] = right

    return E_left+E_right, horizontal_matrix, vertical_matrix