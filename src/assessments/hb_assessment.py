import os
# import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.patches as patches
# plt.switch_backend('agg')

from ..func.weighted_sum import *
from ..func.evaluate_width import *
from ..func.evaluate_point import *
from ..func.draw_contourlines import *
from ..func.project_on_surface import *
from ..func.combine_projection import *
from ..func.total_luminous_flux import *
from ..func.merge_light_distributions import *
from .hb_normalized_points import *


# 1-point and 2-point used for the high beam assessment
one_point = [133.3, 29.1, 31.5, 41.9, 134.2, 5.5, 5.9, 1114.1]
two_point = [235.0, 61.0, 63.3, 81.4, 207.7, 10.5, 10.9, 3126.1]

def hb_assessment(data, predifined_height, predifined_width):
    """Evaluate the performance of the High Beam headlight system in a vehicle

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

    # calculate A-E points for high beam
    actual_A, point_A = evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point=one_point[0], two_point=two_point[0], DirX=0, DirY=installation_height)
    actual_B, point_B = evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point=one_point[1], two_point=two_point[1], DirX=-20, DirY=installation_height)
    actual_C, point_C = evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point=one_point[2], two_point=two_point[2], DirX=0, DirY=9+installation_height)
    actual_D, point_D = evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point=one_point[3], two_point=two_point[3], DirX=20, DirY=installation_height)
    actual_E, point_E = evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point=one_point[4], two_point=two_point[4], DirX=0, DirY=-2+installation_height)

    # calculate the light distribution for 250mm above road surface
    # left_headlamp, right_headlamp = matrix[0], matrix[1]
    # Ev_left, Eh_left, Eq_left, E_levels, distance_vertical_left = project_on_surface(left_headlamp, horizontal_angles, vertical_angles, installation_height=installation_height-0.25)

    # Ev_right, Eh_right, Eq_right, _, distance_vertical_right = project_on_surface(right_headlamp, horizontal_angles, vertical_angles, installation_height=installation_height-0.25)

    # plot contour of the combined projection
    # Eq, Eh, Ev = combine_projection(Eq_left, Eq_right, distance_vertical_left, predifined_width)
    # cs, contour_figure, axes_intervals = draw_contourlines(Ev, Eh, Eq, E_levels) 
    # figure_data = [Eq, Eh, Ev]


    # calculate E nearside and offside for high beam
    actual_Eoffside, point_Eoffside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[5], two_point[5], DirX=-20, DirY=0.25, DirZ=[10,20])

    actual_Enearside, point_Enearside = evaluate_width(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point[6], two_point[6], DirX=20, DirY=0.25, DirZ=[10,20])

    # Merge headlamp LVK and calculate total luminous flux
    LVK, merged_horizontal_angles = merge_light_distributions(matrix, vertical_angles, horizontal_angles, data_names, headlight_spread_distance=spread_distance, distance=1000)
    
    actual_Flux, point_Flux = compute_total_luminous_flux(LVK, merged_horizontal_angles, vertical_angles, [-45, 45], [-5, 10], one_point=one_point[7], two_point=two_point[7])

    # print results    
    print(' Point A: ', actual_A, ', weight: ', point_A, '\n',
          'Point B: ', actual_B, ', weight: ', point_B, '\n',
          'Point C: ', actual_C, ', weight: ', point_C, '\n',
          'Point D: ', actual_D, ', weight: ', point_D, '\n',
          'Point E: ', actual_E, ', weight: ', point_E, '\n',
          'Offside E: ', actual_Eoffside, ', weight: ', point_Eoffside, '\n',
          'Nearside E: ', actual_Enearside, ', weight: ', point_Enearside, '\n',
          'Flux: ', actual_Flux, ', weight: ', point_Flux, '\n')

    # Output variables                                                      
    front_view_figdata = [LVK, merged_horizontal_angles, vertical_angles]
    # not used?
    # top_view_figdata = [figure_data[0], figure_data[1], figure_data[2], E_levels, axes_intervals] 
    top_view_figdata = []
    actual_results = [[actual_A, actual_B, actual_C, actual_D, actual_E, actual_Eoffside, actual_Enearside, actual_Flux],
                      [point_A, point_B, point_C, point_D, point_E, point_Eoffside, point_Enearside, point_Flux]]
    result_points = hb_normalized_points(point_A, point_B, point_C, point_D, point_E, point_Eoffside, point_Enearside, point_Flux)     
    
    # Close all graphs produced with matplotlib    
    plt.close('all') 

    # Output [1] LVK fig, [2] contour fig, [3] actual calculations, [4] flux, [5] normalized points 
    return [front_view_figdata, top_view_figdata, actual_results, actual_Flux, result_points]