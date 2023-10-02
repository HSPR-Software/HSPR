from matplotlib.ticker import FuncFormatter
import numpy as np
import matplotlib.pyplot as plt
from func.find_nearest import *
from mpl_toolkits.axes_grid1 import make_axes_locatable

def plot_front_view(fig, axes, data):
    """Create a matplotlib heatma figure for the light distribution 

    Args:
        fig ([Figure]): [Matplotlib figure]
        axes ([AxesSubPlot]): [Axes of the given matplotlib figure]
        data ([array]): [Light distribution data (LVK)]

    Returns:
        [Figure]: [Matplotlib plot containing the heatmap for the LVK]
    """
    
    matrix, horizontal_angle, vertical_angle = data[0], data[1], data[2]
    # aspect auto to stretch to the available space
    # extend limited to +-45° horizontally and +-10° vertically for visibility of the relevant regions
    #im = axes.imshow(matrix, cmap='jet', interpolation='nearest', origin='lower',extent=[horizontal_angle[0], horizontal_angle[-1], vertical_angle[0], vertical_angle[-1]], aspect='auto')
    area = [-45, 45, -10, 10]
    im = axes.imshow(matrix, cmap='jet', interpolation='nearest', origin='lower',extent=area, aspect='auto')

    axes.axvline(x=0, color='dimgray', linewidth=2.5,alpha=0.75)
    axes.axhline(y=0, color='dimgray', linewidth=2.5,alpha=0.75)

    # set labels and ticks for axis
    axes.set_ylabel('Vertical angle in degree', loc='center')
    axes.set_xlabel('Horizontal angle in degree', loc='center')

    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="3%", pad=0.1)
    cbar= plt.colorbar(im, cax=cax, )
    #cbar.ax.set_yticklabels(['0', ''.join([str(np.round(np.max(matrix)/2000, decimals=1)), 'k']), ''.join([str(np.round(np.max(matrix)/1000, decimals=1)), 'k'])])
    cbar.formatter = FuncFormatter(format_func)
    cbar.update_ticks()
    cbar.ax.set_title('I in kcd', fontname="Times New Roman")

    return axes

def format_func(x, pos):
    return f"{x / 1000:.0f}"

