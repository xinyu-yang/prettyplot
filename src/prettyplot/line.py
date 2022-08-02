#! python3
from .config import *

__all__ = [
        "lines",
        ]


def lines(xs, ys, settings, fig_setting):
    '''
    Draw multiple lines in one figure
    :param xs: A list of x axes
    :type xs: list or tuple of list or tuple

    :param ys: A list of y axes
    :type ys: list or tuple of list or tuple

    :param settings: A list of setting for each line
    :type settings: list or tuple of dictionary

    :fig_setting: The overall setting
    :type fig_setting: dict
    '''
    import matplotlib.pyplot as plt

    # Get figure
    fig = plt.figure()
    ## Figure size
    scale = fig_setting.get("scale") if fig_setting.get("scale") else (1, 1)
    (width_scale, height_scale) = scale
    width, height = fig.get_size_inches()
    fig.set_size_inches(width*width_scale, height*height_scale)

    ## Get Axes
    ax = fig.add_axes([0, 0, 1, 1])

    ## Get title and size
    title = fig_setting.get("title") if fig_setting.get("title") else ""
    title_size = fig_setting.get("title_size") if fig_setting.get("title_size") else 12
    ax.set_title(title, fontsize=title_size)

    ## Label and label size
    label_size = fig_setting.get("label_size") if fig_setting.get("label_size") else 10
    xlabel = fig_setting.get("xlabel") if fig_setting.get("xlabel") else ""
    ylabel = fig_setting.get("ylabel") if fig_setting.get("ylabel") else ""
    ax.set_xlabel(xlabel, fontsize=label_size)
    ax.set_ylabel(ylabel, fontsize=label_size)

    ## Line width
    line_width = fig_setting.get("line_width") if fig_setting.get("line_width") else 1

    ## Tick size
    tick_labelsize = fig_setting.get("tick_labelsize") if fig_setting.get("tick_labelsize") else 12
    ax.tick_params(axis="both", labelsize=tick_labelsize)

    ## Set xlim and ylim
    if fig_setting.get("xlim"):
        ax.set_xlim(fig_setting.get("xlim"))
    if fig_setting.get("ylim"):
        ax.set_ylim(fig_setting.get("ylim"))

    for idx, (x, y, setting) in enumerate(zip(xs, ys, settings)):
                ## Colors
        color = setting.get("color") if setting.get("color") else COLOR[idx % len(COLOR)]
        ## Linestyle
        linestyle = setting.get("linestyle") if setting.get("linestyle") else LINESTYLE[0]
        ## Marker
        marker = setting.get("marker") if setting.get("marker") else None
        ## Label
        label = setting.get("label") if setting.get("label") else ""
        ## draw the plot
        ax.plot(x, y, color=color, lw=line_width, label=label, marker=marker, linestyle=linestyle)

    return fig, ax
