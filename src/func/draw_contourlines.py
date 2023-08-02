import os
import numpy as np
#import mplcursors
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import matplotlib.colors as mc

def draw_contourlines(Ev, Eh, Eq, E_levels, show_plot=False):
    """Create a matplotlib contour plot for the light distribution

    Args:
        Ev ([array]): [vertical grid layout]
        Eh ([array]): [horizontal grid layout]
        Eq ([array]): [z value on the grid layout]
        E_levels ([array]): [contour levels]
        show_plot (bool, optional): [shows plot if True]. Defaults to False.

    Returns:
        [list]: [contour lines]
        [fig]: [contour fig]
        [list]: [x and y boundries]
    """
    # variables for contour plots
    norm = mc.BoundaryNorm(E_levels, 256)
    fig, axes = plt.subplots()
    axes.invert_yaxis() 
    cs = axes.contourf(Ev, Eh, Eq, levels=E_levels)
    
    # plot the [1, 3, 5] lx isolux lines
    cs1 = axes.contour(cs, levels=[E_levels[0]], norm=norm, colors='w', linestyles='-', linewidths=1)
    # cs3 = axes.contour(cs, levels=[E_levels[1]], norm=norm, colors='w', linestyles='-', linewidths=1)
    # cs5 = axes.contour(cs, levels=[E_levels[2]], norm=norm, colors='w', linestyles='-', linewidths=1)

    # Set plot boundries
    x_max, y_max, y_min = np.zeros(3) 
    for array in cs1.allsegs[0]:
        if np.floor(np.min(array[:,1])) < y_min:
            y_min = np.floor(np.min(array[:,1]))
        if np.ceil(np.max(array[:,1])) > y_max:
            y_max = np.ceil(np.max(array[:,1]))
        if np.ceil(np.max(array[:,0])) > x_max:
            x_max = np.ceil(np.max(array[:,0]))

    # return [cs, cs1, cs3, cs5], fig, [x_max, y_max, y_min]
    return [], {}, [x_max, y_max, y_min]
    