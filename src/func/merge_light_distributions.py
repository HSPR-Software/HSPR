import numpy as np

def merge_light_distributions(matrix, verticale_angle, horizontal_angle, data_names, installation_height=0.75, headlight_spread_distance=1.5, distance=25):
    """merge the light distribution of both (left and right) headlamps

    Args:
        matrix ([array]): [light distribution both (left and right)]
        verticale_angle ([array]): [vertical angles of the light distribution]
        horizontal_angle ([array]): [horizontal angles of the light distribution]
        installation_height (float, optional): [Installation height of the headlight systems above surface]. Defaults to 0.75.
        headlight_spread_distance (float, optional): [distance between both (left and right) headlight systems]. Defaults to 1.5.
        distance (float, optional): [distance between the origin and the projection wall]. Defaults to 25.

    Returns:
        [array]: [light distribution after merging both headlamps(left and right)]
        [array]: [new horizontal angles]
    """
    

    # horizontal angle shift
    resolution = horizontal_angle[1] - horizontal_angle[0]
    horizontal_shift = np.rad2deg(np.arctan(0.5*headlight_spread_distance/distance))
    new_angle_horizontal = np.around(np.arange(
                                    horizontal_angle[0] - horizontal_shift, 
                                    horizontal_angle[-1] + horizontal_shift + resolution,  
                                    resolution
                                    ), decimals=2
                                )

    LVK_left = np.zeros((len(verticale_angle), len(new_angle_horizontal)))
    LVK_right = np.zeros((len(verticale_angle), len(new_angle_horizontal)))
        

    if 'LH' in data_names[0]:
        LVK_left[:,:len(horizontal_angle)] = matrix[0]
        LVK_right[:,(len(new_angle_horizontal)-len(horizontal_angle)):] = matrix[-1]
    elif 'RH' in data_names[0]:
        LVK_left[:,:len(horizontal_angle)] = matrix[-1]
        LVK_right[:,(len(new_angle_horizontal)-len(horizontal_angle)):] = matrix[0]
    
    LVK = LVK_left + LVK_right
    return LVK, np.around(new_angle_horizontal, decimals=3)