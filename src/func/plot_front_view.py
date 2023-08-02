import numpy as np
import matplotlib.pyplot as plt
from .find_nearest import *
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
    cmap = plt.get_cmap('jet')
    
    # check defined boundries 
    y_min, y_max = np.where(vertical_angle==find_nearest(vertical_angle, -15))[0][0], np.where(vertical_angle==find_nearest(vertical_angle, 15))[0][0]
    x_min, x_max = np.where(horizontal_angle==find_nearest(horizontal_angle, -45))[0][0], np.where(horizontal_angle==find_nearest(horizontal_angle, 45))[0][0]

    vertical_angle = vertical_angle[y_min:y_max]
    horizontal_angle = horizontal_angle[x_min:x_max]
    matrix = matrix[y_min:y_max,x_min:x_max]

    im = axes.pcolormesh(matrix, cmap=cmap)

    # find max and zero of each axes
    zero_yaxes = np.where(vertical_angle==find_nearest(vertical_angle, 0))[0][0]
    zero_xaxes = np.where(horizontal_angle==find_nearest(horizontal_angle, 0))[0][0]
    max_yaxes = matrix.shape[0]
    max_xaxes = matrix.shape[1]
    
    # add zero lines
    axes.plot([zero_xaxes, zero_xaxes], [0, max_yaxes], color='dimgray', linewidth=2.5)
    axes.plot([0, max_xaxes], [zero_yaxes, zero_yaxes], color='dimgray', linewidth=2.5)

    # set labels and ticks for axis
    axes.set_ylabel('Vertical angle in degrees', loc='center')
    axes.set_yticks(np.around(np.linspace(0, im.sticky_edges.y[-1], 9)))
    axes.set_yticklabels(np.around(np.linspace(vertical_angle[0], vertical_angle[-1], 9)))

    axes.set_xlabel('Horizontal angle in degrees', loc='center')
    axes.set_xticks(np.around(np.linspace(0, im.sticky_edges.x[-1], 9)))
    axes.set_xticklabels(np.around(np.linspace(horizontal_angle[0], horizontal_angle[-1], 9)))


    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="3%", pad=0.1)
    cbar= plt.colorbar(im, cax=cax, ticks=[0, np.round(np.max(matrix)/2), np.round(np.max(matrix))])
    cbar.ax.set_yticklabels(['0', ''.join([str(np.round(np.max(matrix)/2000, decimals=1)), 'k']), ''.join([str(np.round(np.max(matrix)/1000, decimals=1)), 'k'])])
    cbar.ax.set_title('I in cd', fontsize=9)

    return fig