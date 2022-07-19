import math
import numpy as np
from scipy.interpolate import interp1d, interp2d 

def project_on_surface(light_distribution, new_angle_horizontal, angle_vertical, assessment_mode=None, installation_height=0.75):
    """calculate the projection of the light distribution on the road surface

    Args:
        light_distribution ([ndarray]): [contains the light distribution]
        new_angle_horizontal ([ndarray]): [horizontal angles of the light distribution]
        angle_vertical ([ndarray]): [vertical angles of the light distribution]
        assessment_mode ([list], optional): [used to project the light distribution depending on the mode]. Defaults to None.
        installation_height (float, optional): [vehicle headlamp installation height]. Defaults to 0.75.

    Returns:
        [array]: [data used to plot the top view (contour plots)]
    """

    if assessment_mode == 'ADB':
        # mirror the angles
        matrix = np.flipud(light_distribution)
        angle_vertical = np.flipud(angle_vertical) * -1
        distance_vertical = np.absolute(np.divide(installation_height, np.tan(1e-4 + np.deg2rad(angle_vertical))))
    else:
        matrix = light_distribution
        distance_vertical = np.absolute(np.divide(installation_height, np.tan(1e-4 + np.deg2rad(angle_vertical))))
    
    # length limit
    value = np.max(distance_vertical)
    index = np.where(distance_vertical==value)
    limit = index[0][0] + 1

    distance_horizontal = np.zeros((limit, len(new_angle_horizontal)))
    distance_diagonal = np.zeros((limit, len(new_angle_horizontal)))
    distance_res = np.zeros((limit, len(new_angle_horizontal)))

    for i in range(limit):
        distance_horizontal[i,:] = np.multiply(np.tan(np.deg2rad(new_angle_horizontal)),distance_vertical[i])
        distance_diagonal[i,:] = np.sqrt(distance_vertical[i]**2 + distance_horizontal[i,:]**2)
        distance_res[i,:] = np.sqrt(installation_height**2 + distance_diagonal[i,:]**2)

    # Calculation of the Illuminance [lux]
    E = np.zeros((limit,len(new_angle_horizontal)))
    E_vertical = np.zeros((limit,len(new_angle_horizontal)))
    E_horizontal = np.zeros((limit,len(new_angle_horizontal)))
    for i in range(limit):
        E[i,:] = np.divide(matrix[i,:], distance_res[i,:]**2)
        E_vertical[i,:] = np.multiply(np.divide(distance_diagonal[i,:], distance_res[i,:]), np.divide(matrix[i,:], distance_res[i,:]**2))
        E_horizontal[i,:] = np.multiply(np.divide(installation_height, distance_res[i,:]), np.divide(matrix[i,:], distance_res[i,:]**2))


    E_levels = np.sort(np.array([1, 3, 5, 10, 30, 50, 100, 150, 200, 0.9*np.max(E), np.max(E)]))
    distance_vertical_2 = np.repeat(np.expand_dims(distance_vertical[:limit], axis=1), len(new_angle_horizontal), axis=1)

    # interpolation of light distribution on surface
    resolution = 0.01
    horizontal_resolution = np.arange(-50, 50+resolution, resolution).reshape(1, -1)
    resolution_matrix = np.repeat(horizontal_resolution, distance_vertical_2.shape[0], axis=0)
    E_l = np.zeros((distance_vertical_2.shape[0], horizontal_resolution.shape[-1]))
    vertical_matrix = np.repeat(distance_vertical[:limit].reshape(-1, 1), horizontal_resolution.shape[-1], axis=1) #repmat(Entfernung_vert(1:limit).',1,length(Horizontal));



    # Interpolate horizontally
    
    for i in range(distance_vertical_2.shape[0]):
        interpolate = interp1d(distance_horizontal[i,:], E[i,:], bounds_error=False)
        E_interpolate = interpolate(horizontal_resolution.reshape(-1))
        index = np.isnan(E_interpolate)
        E_interpolate[index] = 0
        E_l[i,:] = E_interpolate

    # Interpolate vertically original resolution = 0.1 
    resolution = 0.1
    # resolution = 0.01
    vertical_minimum = np.min(distance_vertical)
    vertical_maximum = distance_vertical[np.where(distance_vertical==value)[0][0]-1]
    verical_interpolation = interp2d(horizontal_resolution[0], distance_vertical_2[:,0], E_l, kind='linear')
    E_new = verical_interpolation(horizontal_resolution[0],np.arange(vertical_minimum, vertical_maximum+resolution, resolution))
    

    Eh = distance_horizontal
    Ev = distance_vertical_2
    Eq = E_new

    return Ev, Eh, Eq, E_levels, distance_vertical