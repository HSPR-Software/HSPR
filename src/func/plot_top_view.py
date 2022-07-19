import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.axes_grid1 import make_axes_locatable

def plot_top_view(fig, axes, data, show_plot=False):
    # variables for contour plots
    Eq, Eh, Ev, E_levels = data[0], data[1], data[2], data[3]
    norm = mc.BoundaryNorm(E_levels, 256)
    # Plot
    # fig, axes = plt.subplots(nrows=1)
    cmap = plt.get_cmap('jet')
    # add axis labels
    # axes.text(0.5, 0.04, 'Vertical length in meters', ha='center', va='center', fontsize=10)
    # axes.text(0.06, 0.5, 'Horizontal length in meters', ha='center', va='center', rotation='vertical', fontsize=10)
    if Eq.max() < 5:
        E_levels = [1, 2, 3, 4, 5]
    else:
        E_levels = np.append([1, 3], np.around(np.linspace(5, Eq.max(), 8)))
        E_levels = np.unique(E_levels)
    cs = axes.contourf(Ev, Eh, Eq, levels=E_levels, cmap=cmap)
    # plot the [1, 3, 5] lx isolux lines
    cs1 = axes.contour(cs, levels=[E_levels[0]], norm=norm, colors='w', linestyles='-', linewidths=0.5)
    cs3 = axes.contour(cs, levels=[E_levels[1]], norm=norm, colors='w', linestyles='-', linewidths=0.5)
    cs5 = axes.contour(cs, levels=[E_levels[2]], norm=norm, colors='w', linestyles='-', linewidths=0.5)

    # Set plot boundries
    x_max, y_max, y_min = np.zeros(3) 
    for array in cs1.allsegs[0]:
        if np.floor(np.min(array[:,1])) < y_min:
            y_min = np.floor(np.min(array[:,1]))
        if np.ceil(np.max(array[:,1])) > y_max:
            y_max = np.ceil(np.max(array[:,1]))
        if np.ceil(np.max(array[:,0])) > x_max:
            x_max = np.ceil(np.max(array[:,0]))
    
    # Set axes label and boundries
    axes.set_xlabel('Vertical length in meters', loc='center')
    axes.set_ylabel('Horizontal length in meters', loc='center')
    axes.set_ylim([y_min, y_max])
    axes.set_xlim([0, x_max])

    # axes.plot([0, road_length], [0,0], color='k', linewidth=1)
    axes.plot([0, (data[4][0]+ data[4][0]* 0.1)], [1.5,1.5], color='k', linewidth=1.5)
    # axes.plot([0, road_length], [3,3], color='k', linewidth=1)
    axes.plot([0, (data[4][0]+ data[4][0]* 0.1)], [-1.5,-1.5], color='k', linestyle='--', linewidth=1.5)
    axes.plot([0, (data[4][0]+ data[4][0]* 0.1)], [-4.5,-4.5], color='k', linewidth=1.5)
    # axes.plot([0, 500], [0,43.74], color='k', linewidth=1.5)
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    cbar = fig.colorbar(cs, cax=cax, ax=axes)
    cbar.ax.set_title('E in Lux', fontsize=9)
    axes.invert_yaxis()

    return fig