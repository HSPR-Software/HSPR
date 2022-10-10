import numpy as np
from func.merge_light_distributions import *
#from skimage import io
from matplotlib import pyplot as plt
from scipy.interpolate import interp2d, RectBivariateSpline

"""Get index where vertical and horizontal angle are at the edges, looks them up in data and determines the maximum to check if they exceed the given limits
    data contains the 12 ADB LVKs
    ECE R123
    Line1 = oncoming 50m
    Line2 = oncoming 100m
    line3 = oncoming 200m
    line4 = preceding 50m
    line5 = preceding 100m
    line6 = preceding 200m

    Args:
        data ([dictionary]): [data of all assessments]
        horizontal_angles: [horizontal angles in degree to the matrices in data]
        vertical_angles: [vertical angles in degree to the matrices in data]
        headlight_spread_distance: distance between both headlights with default 1.5m


    Returns:
        measured_max_left: [maximum values on test line for the left headlight]
        measured_max_right: [maximum values on test line for the right headlight]

    """
def adb_blockout_zone_check(data,horizontal_angles,vertical_angles, headlight_spread_distance=1.5):
    measured_max_left =[]
    measured_max_right = []
    distances = [50,50,50,100,100,100,200,200]
    vertical_line_angle = [0.30,0.30,0.57,0.15,0.15,0.30,0.10,0.15]
    left_edges = [-2.2,1.0,-5.3,-1.4,0.5,-2.9,-0.95,-1.7]
    right_edges = [1.0,2.2,-1.5,0.5,1.4,-0.5,0.95,0.0]

    for i,(distance,vert) in enumerate(zip(distances,vertical_line_angle)):
        ohnetransition_verschiebung = True

        left_leftedge_angle_shifted,left_rightedge_angle_shifted,right_leftedge_angle_shifted,right_rightedge_angle_shifted = parallax_correction_shift(left_edges[i],right_edges[i],headlight_spread_distance, distance)

        if i==0:#means 50m preceding a) -> line4 right edge is not allowed to shift and has a 0.5° tolerance
            LVK_left,LVK_right = data[6],data[7]
            if ohnetransition_verschiebung:
                left_rightedge_angle_shifted = right_edges[i]
                right_rightedge_angle_shifted = right_edges[i]


        if i==1: #means 50m preceding b)-> line4 left edge is not allowed to shift and has a 0.5° tolerance
            LVK_left,LVK_right = data[6],data[7]
            if ohnetransition_verschiebung:
                left_leftedge_angle_shifted = left_edges[i]
                right_leftedge_angle_shifted = left_edges[i]
 

            
        if i==2: #means 50m oncoming -> line1  left edge is not allowed to shift
            LVK_left,LVK_right = data[0],data[1]

        if i==3: #means 100m preceding a) -> line5  right edge is not allowed to shift
            LVK_left,LVK_right = data[8],data[9]
            if ohnetransition_verschiebung:
                left_rightedge_angle_shifted = right_edges[i]
                right_rightedge_angle_shifted = right_edges[i]


        if i==4: #means 100m preceding b) -> line5  left edge is not allowed to shift
            LVK_left,LVK_right = data[8],data[9]
            if ohnetransition_verschiebung:
                left_leftedge_angle_shifted = left_edges[i]
                right_leftedge_angle_shifted = left_edges[i]


        if i==5: #means 100m oncoming -> line2
            LVK_left,LVK_right = data[2],data[3]

        if i==6: #means 200m preceding -> line6
            LVK_left,LVK_right = data[10],data[11]

        if i==7: #means 200m oncoming -> line3
            LVK_left,LVK_right = data[4],data[5]


        f_left = interp2d(horizontal_angles,vertical_angles,LVK_left, kind="linear") 
        f_right = interp2d(horizontal_angles,vertical_angles,LVK_right, kind="linear")
        new_horizontal_left = np.linspace(left_leftedge_angle_shifted,left_rightedge_angle_shifted,100)
        new_horizontal_right = np.linspace(right_leftedge_angle_shifted,right_rightedge_angle_shifted,100)


        measured_max_left.append(round(np.nanmax(f_left(new_horizontal_left,vert)),3))
        measured_max_right.append(round(np.nanmax(f_right(new_horizontal_right,vert)),3))

    return measured_max_left,measured_max_right


def parallax_correction_shift(left_edges,right_edges,headlight_spread_distance, distance):
    """keeps the old resolution but calculates the horizontal values for a bigger matrix which fits the new LVK created by combining and shifting the left and right LVK"""
    horizontal_shift = np.rad2deg(np.arcsin(0.5*headlight_spread_distance/distance))

    left_leftedge_angle = left_edges+horizontal_shift
    left_rightedge_angle = right_edges+horizontal_shift

    right_leftedge_angle = left_edges-horizontal_shift
    right_rightedge_angle = right_edges-horizontal_shift

    return left_leftedge_angle,left_rightedge_angle,right_leftedge_angle,right_rightedge_angle
















def shift_lvks(lvk_left,lvk_right,new_angle_horizontal,horizontal_angles,vertical_angles):
    """shifts the existing LVKs to the left and right based on new horizontal angles"""
    LVK_left = np.zeros((len(vertical_angles), len(new_angle_horizontal)))
    LVK_right = np.zeros((len(vertical_angles), len(new_angle_horizontal)))
    LVK_left[:,:len(horizontal_angles)] = lvk_left
    LVK_right[:,(len(new_angle_horizontal)-len(horizontal_angles)):] = lvk_right
    return lvk_right,lvk_right
