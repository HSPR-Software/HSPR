from .find_nearest import *

def find_interpolation_points(matrix, alpha, beta, horizontal_angles, vertical_angles):
    """Find the four neighboring points with their x and y coordinate values

    Args:
        matrix ([array]): [light distribution data]
        alpha ([float]): [horizontal angle to origin]
        beta ([float]): [verticale angle to origin]
        horizontal_angles ([array]): [horizontal angles to the corresponding light distribution in matrix]
        vertical_angles ([array]): [verticale angles to the corresponding light distribution in matrix]

    Returns:
        [list]: [contain the four neighboring points with coordinates]
    """

    horizontal_index = np.where(horizontal_angles == find_nearest(horizontal_angles, alpha))[0]
    vertical_index = np.where(vertical_angles == find_nearest(vertical_angles, beta))[0]

    if np.abs(horizontal_angles[horizontal_index-1]-alpha) < np.abs(horizontal_angles[horizontal_index+1]-alpha):        
        left_x = horizontal_index-1
        right_x = horizontal_index
    else:
        left_x = horizontal_index
        right_x = horizontal_index+1

    if np.abs(vertical_angles[vertical_index-1]-beta) < np.abs(vertical_angles[vertical_index+1]-beta):
        upper_y = vertical_index-1
        lower_y = vertical_index
    else:
        upper_y = vertical_index
        lower_y = vertical_index+1

    upper_left = (horizontal_angles[left_x][0], vertical_angles[upper_y][0], matrix[upper_y[0]][left_x[0]])
    lower_left = (horizontal_angles[left_x][0], vertical_angles[lower_y][0], matrix[lower_y[0]][left_x[0]])
    upper_right = (horizontal_angles[right_x][0], vertical_angles[upper_y][0], matrix[upper_y[0]][right_x[0]])      
    lower_right = (horizontal_angles[right_x][0], vertical_angles[lower_y][0], matrix[lower_y[0]][right_x[0]])

    return [upper_left, lower_left, upper_right, lower_right]