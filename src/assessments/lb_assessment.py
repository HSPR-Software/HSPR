import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.patches as patches
# plt.switch_backend('agg')

from ..func.weighted_sum import *
from ..func.evaluate_zone import *
from ..func.compute_lb_glare import *
from ..func.evaluate_width import *
from ..func.draw_contourlines import *
from ..func.project_on_surface import *
from ..func.combine_projection import *
from ..func.total_luminous_flux import *
from ..func.merge_light_distributions import *
from .lb_normalized_points import *

# 1-point and 2-point used for the low beam assessment
one_point = [71.6, 71.5, 32.7, 4.8, 7.6, 5.9, 6.6, 747.6, 0.73]
two_point = [95.1, 138.4, 48.4, 12.5, 16.3, 9.6, 10.5, 1785.1, 0.27]

def lb_assessment(data, predifined_height, predifined_width):
    """Calculates the performance of the Low Beam headlight system in a vehicle

    Args:
        data ([list]): [contains the data including horizontal and vertical angles]
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
    # given variables
    spread_distance = predifined_width
    installation_height = predifined_height
    headlamp_adjustment = spread_distance/2
    matrix, horizontal_angles, vertical_angles, data_names = data[0], data[1], data[2], data[3]  

    # split data 
    # left_headlamp, right_headlamp = matrix[0], matrix[1]
                                                                                                      
    # calculate the light distribution on the road surface
    # Ev_left, Eh_left, Eq_left, E_levels, distance_vertical_left = project_on_surface(left_headlamp, horizontal_angles, vertical_angles, installation_height=installation_height)

    # Ev_right, Eh_right, Eq_right, _, distance_vertical_right = project_on_surface(right_headlamp, horizontal_angles, vertical_angles, installation_height=installation_height)

    # combine left and right headlamp and save figure data for plotting
    # Eq, Eh, Ev = combine_projection(Eq_left, Eq_right, distance_vertical_left, predifined_width)
    # cs, contour_figure, axes_intervals = draw_contourlines(Ev, Eh, Eq, E_levels)
    # figure_data = [Eq, Eh, Ev]
 

    # compute the P weights for Zone A-C in the light distribution for passing beam range assessment
    actual_A, point_A = evaluate_zone(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[0], two_point[0], DirX=[0, 1.5, 3], DirY=0)

    actual_B, point_B = evaluate_zone(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[1], two_point[1], DirX=[0, 1.5, 3], DirY=0, theta=5)

    actual_C, point_C = evaluate_zone(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[2], two_point[2], DirX=[-3, -4.5, -6], DirY=0.25)


    actual_Doffside, point_Doffside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[3], two_point[3], DirX=-20, DirY=0, DirZ=[30,40, 50])

    actual_Dnearside, point_Dnearside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[4], two_point[4], DirX=20, DirY=0, DirZ=[30,40, 50])

    # calculate Zone E for DirY=250mm above road surface
    actual_Eoffside, point_Eoffside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[5], two_point[5], DirX=-20, DirY=0.25, DirZ=[10,20])

    actual_Enearside, point_Enearside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[6], two_point[6], DirX=20, DirY=0.25, DirZ=[10,20])

    # Merge headlamp LVK and calculate total luminous flux
    LVK, new_horizontal_angles = merge_light_distributions(matrix, vertical_angles, horizontal_angles, data_names, headlight_spread_distance=spread_distance, distance=1000)
    actual_Flux, point_Flux = compute_total_luminous_flux(LVK, new_horizontal_angles, vertical_angles, [-45, 45], [-15, 5], one_point=one_point[7], two_point=two_point[7]) 

    glare_points=[]	   
    for index in range(matrix.shape[0]):
        installation_width = [-spread_distance/2  if 'LH' in data_names[index] else spread_distance/2][0]
        glare_points.append(compute_lb_glare(matrix[index], installation_width, installation_height, horizontal_angles, vertical_angles, horizontal_edges=[-7.9, 1.3]))
    
    actual_Glare, point_Glare = weighted_sum(glare_points, one_point=one_point[8], two_point=two_point[8])

    # print results    
    print(' Zone A: ', actual_A, ', weight: ', point_A, '\n',
          'Zone B: ', actual_B, ', weight: ', point_B, '\n',
          'Zone C: ', actual_C, ', weight: ', point_C, '\n',
          'Offside D: ', actual_Doffside, ', weight: ', point_Doffside, '\n',
          'Nearside D: ', actual_Dnearside, ', weight: ', point_Dnearside, '\n',
          'Offside E: ', actual_Eoffside, ', weight: ', point_Eoffside, '\n',
          'Nearside E: ', actual_Enearside, ', weight: ', point_Enearside, '\n',
          'Flux: ', actual_Flux, ', weight: ', point_Flux, '\n',
          'Glare: ', actual_Glare, ', weight: ', point_Glare)

    # Output variables                                                      
    front_view_figdata = [LVK, new_horizontal_angles, vertical_angles] 
    # not used?
    # top_view_figdata = [figure_data[0], figure_data[1], figure_data[2], E_levels, axes_intervals]
    top_view_figdata = []
    actual_results = [[actual_A, actual_B, actual_C, actual_Doffside, actual_Dnearside, actual_Eoffside, actual_Enearside, actual_Glare, actual_Flux],
                    [point_A, point_B, point_C, point_Doffside, point_Dnearside, point_Eoffside, point_Enearside, point_Glare, point_Flux]]
    result_points = lb_normalized_points(point_A, point_B, point_C, point_Doffside, point_Dnearside, point_Eoffside, point_Enearside, point_Flux, point_Glare)   

    # Close all graphs produced with matplotlib    
    plt.close('all')
    
    # Output [1] LVK fig, [2] contour fig, [3] actual calculations, [4] flux, [5] normalized points 
    return [front_view_figdata, top_view_figdata, actual_results, actual_Flux, result_points]