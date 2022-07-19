import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.patches as patches
# plt.switch_backend('agg')

from func.weighted_sum import *
from func.evaluate_zone import *
from func.draw_contourlines import *
from func.compute_adb_glare import *
from func.project_on_surface import *
from func.combine_projection import *
from func.total_luminous_flux import *
from func.get_index_positions import *
from func.merge_light_distributions import *
from assessments.adb_normalized_points import *


lines = {'50':['Linie1', 'Linie4'],
        '100':['Linie2', 'Linie5'],
        '200':['Linie3', 'Linie6']}

# 1-point and 2-point used for the ADB assessment
one_point = {'50':[113.0, 119.9, 27.3, 1889.3, 39.8, 124.1, 74.6, 1843.7],
            '100':[92.8, 127.1, 65.0, 1949.7, 52.9, 134.8, 94.7, 1943.9],
            '200':[81.3, 130.6, 89.4, 1993.6, 66.2, 132.9, 110.9, 2025.2]}
two_point = {'50':[228.2, 182.0, 86.3, 2829.9, 57.0, 181.4, 117.5, 2748.6],
            '100':[209.9, 182.9, 86.9, 2962.7, 82.7, 184.0, 150.0, 2898.7],
            '200':[176.0, 183.2, 131.1, 3038.5, 113.2, 183.3, 177.4, 2979.9]}

def adb_assessment(data, line_names, predifined_height, predifined_width):
    """Evaluate the performance of the ADB headlight system in a vehicle

    Args:
        data ([list]): [contains the data including horizontal and vertical angles]
        line_names ([list]): [contain line names of the data]
        predifined_height (float): [installation height above the surface of the headlight system given by user]
        predifined_width (float): [installation width of the headlight system given by user]

    Returns:
        [list]: [sublist [1] contains data used for front view plots
                         [2] contains data used for contour plots
                         [3] contains actual calculations
                         [4] contains total luminous flux
                         [5] contains the normalized points
                        ]
    """
    
    # Variables
    spread_distance = predifined_width
    headlamp_adjustment = spread_distance/2
    installation_height = predifined_height
    matrix, horizontal_angles, vertical_angles, data_names = data[0], data[1], data[2], data[3]
    
    result_dict = {}
    for assessment_mode in ['50', '100', '200']:
        
        print('-------{}-----------'.format(lines[assessment_mode][0]))

        # calculate Zone A, B and C for the oncoming ADB at 1.5m above road surface
        actual_A_oncoming, point_A_oncoming = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][0])], horizontal_angles, vertical_angles, 
                                data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][0], two_point[assessment_mode][0], [1.5, 3], 1.5)

        actual_B_oncoming, point_B_oncoming = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][0])], horizontal_angles, vertical_angles, 
                    data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][1], two_point[assessment_mode][1], [0, 1.5, 3], 1.5, theta=5)

        actual_C_oncoming, point_C_oncoming = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][0])], horizontal_angles, vertical_angles, 
                              data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][2], two_point[assessment_mode][2], [-4.5, -6], 1.5)

        # merge both headlamps and calculate total luminous flux
        LVK_oncoming, new_horizontal_angles = merge_light_distributions(matrix[get_index_position(line_names, lines[assessment_mode][0])], vertical_angles, horizontal_angles, 
                                                                        data_names, headlight_spread_distance=spread_distance, distance=int(assessment_mode))                                                                        
                                                
        actual_Flux_oncoming, point_Flux_oncoming = compute_total_luminous_flux(LVK_oncoming, new_horizontal_angles, vertical_angles, [-45, 45], [-5, 10], 
                                                                                            one_point[assessment_mode][3], two_point[assessment_mode][3])                                                                              
        
        
        # plot the contour the oncoming ADB 1.5m above road surface
        left_headlamp, right_headlamp = matrix[get_index_position(line_names, lines[assessment_mode][0])]

        Ev_left, Eh_left, Eq_left, E_levels, distance_vertical_left = project_on_surface(left_headlamp, horizontal_angles, vertical_angles, assessment_mode='ADB', 
                                                                                                                          installation_height=installation_height)

        Ev_right, Eh_right, Eq_right, _, distance_vertical_right = project_on_surface(right_headlamp, horizontal_angles, vertical_angles, assessment_mode='ADB', 
                                                                                                                        installation_height=installation_height)

        Eq_oncoming, Eh_oncoming, Ev_oncoming = combine_projection(Eq_left, Eq_right, distance_vertical_left, predifined_width)
        cs, contour_figure_line2, axes_intervals_oncoming = draw_contourlines(Ev_oncoming, Eh_oncoming, Eq_oncoming, E_levels)   
        figure_data_oncoming = [Eq_oncoming, Eh_oncoming, Ev_oncoming]

        if assessment_mode == '50':

            # calculate ADB oncoming passing beam glare for the 50m line
            glare_points=[]    
            for index in range(matrix[get_index_position(line_names, lines[assessment_mode][0])].shape[0]):
                installation_width = [-spread_distance/2  if 'LH' in data_names[index] else spread_distance/2][0]
                glare_points.append(compute_adb_glare(matrix[get_index_position(line_names, lines[assessment_mode][0])][index], installation_width, installation_height, 
                                                                    horizontal_angles, vertical_angles, horizontal_edges=[-4.2, -1.75], line=lines[assessment_mode][0]))
            
            actual_Glare_oncoming, point_Glare_oncoming = weighted_sum(glare_points, one_point=0.28, two_point=0.11)                                            

        print(' Zone A: ', actual_A_oncoming, ', weight: ', point_A_oncoming, '\n',
        'Zone B: ', actual_B_oncoming, ', weight: ', point_B_oncoming, '\n',
        'Zone C: ', actual_C_oncoming, ', weight: ', point_C_oncoming, '\n',
        'Flux: ', actual_Flux_oncoming, ', weight: ', point_Flux_oncoming) 
        

        print('-------{}-----------'.format(lines[assessment_mode][-1]))

        # calculate Zone A, B and C for the preceding ADB at 1.5m above road surface
        actual_A_preceding, point_A_preceding = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][-1])], horizontal_angles, vertical_angles, 
                                  data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][4], two_point[assessment_mode][4], [1.5, 3], 1.5)

        actual_B_preceding, point_B_preceding = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][-1])], horizontal_angles, vertical_angles, 
                        data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][5], two_point[assessment_mode][5], [0, 1.5, 3], 1.5, theta=5)

        actual_C_preceding, point_C_preceding = evaluate_zone(matrix[get_index_position(line_names, lines[assessment_mode][-1])], horizontal_angles, vertical_angles, 
                                 data_names, headlamp_adjustment, installation_height, one_point[assessment_mode][6], two_point[assessment_mode][6], [-4.5, -6], 1.5)
        
        # merge both headlamps and calculate total luminous flux
        LVK_preceding, _ = merge_light_distributions(matrix[get_index_position(line_names, lines[assessment_mode][-1])], vertical_angles, horizontal_angles, 
                                                                        data_names, headlight_spread_distance=spread_distance, distance=int(assessment_mode))  

        actual_Flux_preceding, point_Flux_preceding = compute_total_luminous_flux(LVK_preceding, new_horizontal_angles, vertical_angles, [-45, 45], [-5, 10], 
                                                                                            one_point[assessment_mode][7], two_point[assessment_mode][7]) 
        # calculate flux mean
        actual_Flux = np.around(np.mean([actual_Flux_oncoming, actual_Flux_preceding]), decimals=0)

        # plot the contour the preceding ADB 1.5m above road surface
        left_headlamp, right_headlamp = matrix[get_index_position(line_names, lines[assessment_mode][-1])]

        Ev_left, Eh_left, Eq_left, E_levels, distance_vertical_left = project_on_surface(left_headlamp, horizontal_angles, vertical_angles, assessment_mode='ADB',                                                                                         
                                                                                                                          installation_height=installation_height)

        Ev_right, Eh_right, Eq_right, _, distance_vertical_right = project_on_surface(right_headlamp, horizontal_angles, vertical_angles, assessment_mode='ADB', 
                                                                                                                        installation_height=installation_height)

        Eq_preceding, Eh_preceding, Ev_preceding = combine_projection(Eq_left, Eq_right, distance_vertical_left, predifined_width)
        cs, contour_figure_line5, axes_intervals_preceding = draw_contourlines(Ev_preceding, Eh_preceding, Eq_preceding, E_levels)
        figure_data_preceding = [Eq_preceding, Eh_preceding, Ev_preceding]       
        

        if assessment_mode == '50':
            
            # calculate ADB preceding passing beam glare for the 50m line
            glare_points=[]    
            for index in range(matrix[get_index_position(line_names, lines[assessment_mode][0])].shape[0]):
                installation_width = [-spread_distance/2  if 'LH' in data_names[index] else spread_distance/2][0]
                glare_points.append(compute_adb_glare(matrix[get_index_position(line_names, lines[assessment_mode][-1])][index], installation_width, installation_height, 
                                                              horizontal_angles, vertical_angles, horizontal_edges=[-1.48, 0.87, 1.48], line=lines[assessment_mode][-1]))
            
            actual_Glare_preceding, point_Glare_preceding = weighted_sum(glare_points, one_point=0.35, two_point=0.16)

        # Output variables                                                      
        front_view_figdata_oncoming = [LVK_oncoming, new_horizontal_angles, vertical_angles]
        top_view_figdata_oncoming = [figure_data_oncoming[0], figure_data_oncoming[1], figure_data_oncoming[2], E_levels, axes_intervals_oncoming]
        front_view_figdata_preceding = [LVK_preceding, new_horizontal_angles, vertical_angles]
        top_view_figdata_preceding = [figure_data_preceding[0], figure_data_preceding[1], figure_data_preceding[2], E_levels, axes_intervals_preceding]
        actual_results = [[actual_A_oncoming, actual_B_oncoming, actual_C_oncoming, actual_Glare_oncoming, actual_Flux_oncoming, actual_A_preceding, actual_B_preceding, actual_C_preceding, actual_Glare_preceding, actual_Flux_preceding],
                            [point_A_oncoming, point_B_oncoming, point_C_oncoming, point_Glare_oncoming, point_Flux_oncoming, point_A_preceding, point_B_preceding, point_C_preceding, point_Glare_preceding, point_Flux_preceding]]
        result_points = adb_normalized_points(point_A_preceding, point_B_preceding, point_C_preceding, point_Flux_preceding, point_Glare_preceding, point_A_oncoming, point_B_oncoming, point_C_oncoming, point_Flux_oncoming, point_Glare_oncoming)   
        
        # Output [1] LVK fig, [2] contour fig, [3] actual calculations, [4] flux, [5] normalized points 
        result_dict[assessment_mode] = [front_view_figdata_oncoming, top_view_figdata_oncoming, front_view_figdata_preceding, 
                                        top_view_figdata_preceding, actual_results, actual_Flux, result_points]

        print(' Zone A: ', actual_A_preceding, ', weight: ', point_A_preceding, '\n',
        'Zone B: ', actual_B_preceding, ', weight: ', point_B_preceding, '\n',
        'Zone C: ', actual_C_preceding, ', weight: ', point_C_preceding, '\n',
        'Flux: ', actual_Flux_preceding, ', weight: ', point_Flux_preceding) 

    return result_dict