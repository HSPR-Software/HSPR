import numpy as np

from func.find_nearest import *
from func.compute_points import *

def evaluate_point(matrix, horizontal_angles, vertical_angles, data_names, headlamp_adjustment, installation_height, one_point, two_point, DirX, DirY, DirZ=100, lux=3):
    """calculate the light intensity at different positions depending on the defenition of TC-45

    Args:
        matrix ([array]): [light distribution]
        horizontal_angles ([array]): [horizontal angle of the light distribution]
        vertical_angles ([array]): [vertical angle of the light distribution]
        one_point ([int]): [one point for weight calculation]
        two_point ([int]): [two point for weight calculation]
        x ([int]): [x is the headlamp width from the origin with origin being in the center (0,0,0)]
        y ([int]): [y is the headlamp height from the origin with origin being in the center (0,0,0)]
        z ([int]): [z is the headlamp vertical distance from the origin with origin being in the center (0,0,0)]
        distance (int, optional): [distance between vehicle and measurment point]. Defaults to 100.
        lx (int, optional): [lx which is used for calculation defenition can be found in TC-45]. Defaults to 3.

    Returns:
        [int]: [mean of the calculated points]
        [int]: [weighted mean of the calculated points]
    """
    hb_step = 800
    step_size = 0.5 
    E_vert_S = []   

    while hb_step > 0:
        for index in range(matrix.shape[0]):
            # Adjust (x,y,z) of headlamp
            x_headlamp = [-headlamp_adjustment if 'LH' in data_names[index] else headlamp_adjustment][0]
            y_headlamp = installation_height
            z_headlamp=0

            Range_dir_norm = np.sqrt(DirX**2+DirY**2+DirZ**2)
            RangeDirX = np.divide(DirX, Range_dir_norm)
            RangeDirY= np.divide(DirY, Range_dir_norm)
            RangeDirZ= np.divide(DirZ, Range_dir_norm)
    
            x = np.multiply(hb_step, RangeDirX) 
            y = np.multiply(hb_step, RangeDirY) 
            z = np.multiply(hb_step, RangeDirZ) 

            # find angle alpha on horizontal axis
            alpha = np.rad2deg(np.arctan(np.divide(x-x_headlamp, z-z_headlamp))) 
            horizontal_index = np.where(horizontal_angles == find_nearest(horizontal_angles, alpha))[0]

            # find angle beta on vertical axis
            beta = np.rad2deg(np.arctan(np.divide(y-y_headlamp, np.sqrt((x-x_headlamp)**2+(z-z_headlamp)**2)))) 
            vertical_index = np.where(vertical_angles == find_nearest(vertical_angles, beta))[0]

            distance = np.sqrt((x_headlamp-x)**2+(y_headlamp-y)**2+(z_headlamp-z)**2)
            I_S = matrix[index][vertical_index, horizontal_index]
            E_rad_S = np.divide(I_S, distance**2)

            cosfact = np.divide(z-z_headlamp, np.sqrt((x_headlamp-x)**2+(y_headlamp-y)**2+(z_headlamp-z)**2))
            E_vert_S.append(np.multiply(E_rad_S, cosfact))

        # E_vert_S links und rechts addieren
        E_vert_S = np.sum(E_vert_S)

        if E_vert_S > lux:
            value=hb_step
            break  
        else:
            E_vert_S = []
            hb_step=hb_step-step_size     

    weight = np.around(compute_points(value, one_point, two_point), decimals=3)
    return value, weight