import numpy as np

def light_combiner(lb, hb):
    """Combines the LB and HB light distribution depending on the vertical and horizontal angles

    Args:
        lb ([array]): [LB light distribution]
        hb ([array]): [HB light distribution]

    Returns:
        [array]: [Combined light distribution]
    """
    # check horizontal angles
    horizontal_lb_min, horizontal_lb_max = lb[1][0], lb[1][-1]
    horizontal_hb_min, horizontal_hb_max = hb[1][0], hb[1][-1]

    # check vertical angles
    vertical_lb_min, vertical_lb_max = lb[2][0], lb[2][-1]
    vertical_hb_min, vertical_hb_max = hb[2][0], hb[2][-1]

    horizontal_min_index = np.where(hb[1] == horizontal_lb_min)[0][0]
    horizontal_max_index = np.where(hb[1] == horizontal_lb_max)[0][0]

    vertical_min_index = np.where(hb[2] == vertical_lb_min)[0][0]
    vertical_max_index = np.where(hb[2] == vertical_lb_max)[0][0]


    left_hb = lb[0][0] + hb[0][0][vertical_min_index:vertical_max_index+1, horizontal_min_index:horizontal_max_index+1]
    right_hb = lb[0][1] + hb[0][1][vertical_min_index:vertical_max_index+1, horizontal_min_index:horizontal_max_index+1]

    new_left_hb = hb[0][0]
    new_right_hb = hb[0][1]

    new_left_hb[vertical_min_index:vertical_max_index+1, horizontal_min_index:horizontal_max_index+1] = left_hb
    new_right_hb[vertical_min_index:vertical_max_index+1, horizontal_min_index:horizontal_max_index+1] = right_hb
  
    return [new_left_hb, new_right_hb]