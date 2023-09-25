import os
import math
import numpy as np
from func.find_nearest import *
from func.bilinear_interpolation import *
from func.find_interpolation_points import *
from settings.configuration import Zones, Glare_Weights

def compute_adb_glare(matrix, installation_width, installation_height, horizontal_angles, vertical_angles, 
                                    horizontal_edges, vertical_edges=[0.93, 1.62], distance=50, line=None):
    
    """compute the passing beam glare the for ADB assessment

    Args:
        matrix ([array]): [contains the ADB light distribution]
        horizontal_angle ([array]): [horizontal angle of the light distribution]
        vertical_angle ([array]): [vertical angle of the light distribution]
        one_point ([int]): [one point for weight calculation]
        two_point ([int]): [two point for weight calculation]
        horizontal_edges (list, optional): [horizontal edges for glare zone]. Defaults to [-7.9, 1.3].
        vertical_edges (list, optional): [vertical edges for glare zone]. Defaults to [0.18, 0.87].
        distance (int, optional): [distance for the glare zone in meters]. Defaults to 50.

    Returns:
        [int]: [computed result]
        [int]: [weighted result]
    """
    # check if oncoming or preceding glare
    line_number = int(line[-1])
    x_headlamp = installation_width
    y_headlamp = installation_height
    z_headlamp = 0
    # Calculate actual edges depending on installation_height and width
    vertical_boundry = [np.around((vertical_edges[0]-installation_height), decimals=2), 
                        np.around((vertical_edges[1]-installation_height), decimals=2)]

    # vertical variables
    vertical_resolution = 0.0138
    # vertical_resolution = np.around((vertical_boundry[1]-vertical_boundry[0])/5, decimals=3)
    vertical_resolution_half = vertical_resolution*0.5
    lower_meter = np.around(vertical_boundry[0]+installation_height+vertical_resolution_half, decimals=3)
    upper_meter = np.around(vertical_boundry[1]+installation_height-vertical_resolution_half, decimals=3)

    # find horizontal index of left and right angles depending on line number
    if line_number < 4:    
        # horizontal variables
        horizontal_resolution = 0.01
        horizontal_resolution_half = horizontal_resolution*0.5
        left_meter = horizontal_edges[0] + horizontal_resolution_half
        right_meter = horizontal_edges[1] - horizontal_resolution_half

        matrix_width = int(np.around((right_meter-left_meter)/horizontal_resolution)+1)
        matrix_height = int(np.around((upper_meter-lower_meter)/vertical_resolution)+1)
        new_matrix = np.zeros((matrix_height, matrix_width))
       
        y = upper_meter
        z = distance
        for row in range(new_matrix.shape[0]):
            x = left_meter
            for column in range(new_matrix.shape[1]):
                # find angle alpha and beta
                alpha = np.rad2deg(np.arctan(np.divide(x-x_headlamp, z-z_headlamp)))
                beta = np.rad2deg(np.arctan(np.divide(y-y_headlamp, np.sqrt((x-x_headlamp)**2+(z-z_headlamp)**2)))) 

                # find points for bilinear_interpolation 
                points = find_interpolation_points(matrix, alpha, beta, horizontal_angles, vertical_angles)
                I_S = bilinear_interpolation(alpha, beta, points)
                
                # Calculate distance between headlamp and point on matrix for steradians
                distance = np.sqrt((x_headlamp-x)**2+(y_headlamp-y)**2+(z_headlamp-z)**2)

                # calculate steredians
                width = horizontal_resolution#_half
                height = vertical_resolution#_half        
                area = width*height
                steradians = np.divide(area, distance**2)

                weight_row = int((row//(matrix_height/Glare_Weights.shape[0]))%(matrix_height/Glare_Weights.shape[0]))
                new_matrix[row][column] = I_S * steradians * Glare_Weights[:,4][weight_row]

                # add to x with each step
                x = x + horizontal_resolution

            y = y - vertical_resolution
            
        result = np.sum(new_matrix)

    else:

        result = []
        # horizontal variables
        horizontal_resolution = 0.01
        horizontal_resolution_half = horizontal_resolution*0.5
        for index in range(len(horizontal_edges)-1):       
            left_meter = horizontal_edges[index] + horizontal_resolution_half
            right_meter = horizontal_edges[index+1] - horizontal_resolution_half

            matrix_width = int(np.around((right_meter-left_meter)/horizontal_resolution)+1)
            matrix_height = int(np.around((upper_meter-lower_meter)/vertical_resolution)+1)
            new_matrix = np.zeros((matrix_height, matrix_width))
        
            y = upper_meter
            z = distance
            for row in range(new_matrix.shape[0]):
                x = left_meter
                for column in range(new_matrix.shape[1]):
                    # find angle alpha and beta
                    alpha = np.rad2deg(np.arctan(np.divide(x-x_headlamp, z-z_headlamp)))
                    beta = np.rad2deg(np.arctan(np.divide(y-y_headlamp, np.sqrt((x-x_headlamp)**2+(z-z_headlamp)**2)))) 

                    # find points for bilinear_interpolation 
                    points = find_interpolation_points(matrix, alpha, beta, horizontal_angles, vertical_angles)
                    I_S = bilinear_interpolation(alpha, beta, points)
                    
                    # Calculate distance between headlamp and point on matrix for steradians
                    distance = np.sqrt((x_headlamp-x)**2+(y_headlamp-y)**2+(z_headlamp-z)**2)

                    # calculate steredians
                    width = horizontal_resolution
                    height = vertical_resolution       
                    area = width*height
                    steradians = np.divide(area, distance**2)

                    weight_row = int((row//(matrix_height/Glare_Weights.shape[0]))%(matrix_height/Glare_Weights.shape[0]))
                    new_matrix[row][column] = I_S * steradians * (Glare_Weights[:,4][weight_row] * (1850/2500)**index)

                    # add to x with each step
                    x = x + horizontal_resolution

                y = y - vertical_resolution

            result.append(np.sum(new_matrix))

        result = np.sum(result)
    
    return np.around(result, decimals=3)