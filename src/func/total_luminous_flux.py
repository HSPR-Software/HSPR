import os
import math
import numpy as np

from .find_nearest import *
from .compute_points import *
from ..settings.configuration import Zones
from scipy.interpolate import interp2d

def compute_total_luminous_flux(matrix, horizontal_angle, vertical_angle, horizontal_boundry, vertical_boundry, one_point, two_point, distance=25):
    """compute the total luminous flux in a define area for the given light distribution

    Args:
        matrix ([array]): [light distribution]
        horizontal_angle ([array]): [horizontal angle of the light distribution]
        vertical_angle ([array]): [vertical angle of the light distribution]
        horizontal_boundry ([list]): [defined horizontal boundry given by TC-45]
        vertical_boundry ([list]): [defined vertical boundry given by TC-45]
        one_point ([int]): [one point for weight calculation]
        two_point ([int]): [two point for weight calculation]
        distance (int, optional): [defined distance in meters]. Defaults to 25.

    Returns:
        [int]: [total luminous flux]
        [int]: [weighted flux]
    """
    # get index where vertical boundry angle
    lower_boundry_index = np.where(vertical_angle == find_nearest(vertical_angle, vertical_boundry[0]))[0][0]
    upper_boundry_index = np.where(vertical_angle == find_nearest(vertical_angle, vertical_boundry[-1]))[0][0]
    left_boundry_index = np.where(horizontal_angle == find_nearest(horizontal_angle, horizontal_boundry[0]))[0][0]
    right_boundry_index = np.where(horizontal_angle == find_nearest(horizontal_angle, horizontal_boundry[-1]))[0][0]

    # Vertical/ Horizontal angles and Matrix Interpolation
    resolution = 0.01
    new_vertical_angles = np.round(np.arange(vertical_boundry[0], vertical_boundry[-1]+resolution, resolution), decimals=2)  
    new_horizontal_angles = np.round(np.arange(horizontal_boundry[0], horizontal_boundry[-1]+resolution, resolution), decimals=2)    
    
    # light distribution within the required zone
    interpolation = interp2d(horizontal_angle[left_boundry_index:right_boundry_index], 
                            vertical_angle[lower_boundry_index:upper_boundry_index], 
                            matrix[lower_boundry_index:upper_boundry_index, left_boundry_index:right_boundry_index], 
                            kind='linear')
    
    new_matrix = interpolation(new_horizontal_angles , new_vertical_angles)

    # Compute steradians for the corresponding zone
    width = np.tan(np.deg2rad(np.abs(new_horizontal_angles[0]-new_horizontal_angles[1])))*distance
    height = np.tan(np.deg2rad(np.abs(new_vertical_angles[0]-new_vertical_angles[1])))*distance
    area = width*height
    steradians = np.divide(area, distance**2)

    # Calcuate total luminous flux for the corresponding zone
    light_matrix = new_matrix
    luminous_flux = np.around(np.sum(light_matrix) * steradians, decimals=3)

    return np.around(luminous_flux, decimals=2), np.around(compute_points(luminous_flux, one_point, two_point), decimals=3)