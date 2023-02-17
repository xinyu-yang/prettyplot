#! python3
from .config import *

__all__ = [
        "bars",
        ]


# The input is a list of entities, each entity is a list of attributes.
# Bars are always grouped by attributes.
# e.g., we have 3 entities with 5 attributes, the figure will have 5 groups and 
# each group has 3 entities.
def bars(data_mtx, fig_setting): 
    '''
    Draw multiple bars in one figure
    :param data_mtx: A list of entities
    :type data_mtx: list or tuple of list or tuple

    :fig_setting: The overall setting
    :type fig_setting: dict
    '''
    import matplotlib.pyplot as plt
    import numpy as np

    # Create figure
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

    ## Tick size
    tick_labelsize = fig_setting.get("tick_labelsize") if fig_setting.get("tick_labelsize") else 12
    ax.tick_params(axis="both", labelsize=tick_labelsize)

    ## Set xlim and ylim
    if fig_setting.get("xlim"):
        ax.set_xlim(fig_setting.get("xlim"))
    if fig_setting.get("ylim"):
        ax.set_ylim(fig_setting.get("ylim"))

    ## Colors
    bar_colors = fig_setting.get("bar_colors") if fig_setting.get("bar_colors") else COLOR
    ## Edgecolor
    edgecolor = fig_setting.get("edgecolor") if fig_setting.get("edgecolor") else "white"
    ## Hatch
    hatch = fig_setting.get("hatch") if fig_setting.get("hatch") else None

    ## Labels
    labels = fig_setting.get("labels") if fig_setting.get("labels") else []
    attributes = fig_setting.get("attributes") if fig_setting.get("attributes") else []
    # Whether to revise or not.
    bar_inverse_data_matrix = fig_setting.get("bar_inverse_data_matrix") if fig_setting.get("bar_inverse_data_matrix") else False
    if bar_inverse_data_matrix:
        data_mtx = list(zip(*data_mtx))
        labels, attributes = attributes, labels

    ## Edgecolor
    bar_width = fig_setting.get("bar_width") if fig_setting.get("bar_width") else 1
    ## Hatch
    group_padding = fig_setting.get("group_padding") if fig_setting.get("group_padding") else 1
    ## Bar label
    enable_bar_label = fig_setting.get("bar_label") if fig_setting.get("bar_label") else False
    bar_label_size = fig_setting.get("bar_label_size") if fig_setting.get("bar_label_size") else "small"


    x = np.arange(len(attributes))  # the label locations
    overall_group_width = bar_width * len(labels) + group_padding
    ax.set_xticks(x * overall_group_width + (bar_width * len(labels))/2., attributes)

    for idx in range(len(labels)):
        offset = bar_width * idx + bar_width / 2
        rects = ax.bar(x * overall_group_width + offset, data_mtx[idx], bar_width, label=labels[idx], edgecolor=edgecolor, color=bar_colors[idx])
        if enable_bar_label:
            ax.bar_label(rects, padding=3, fontsize=bar_label_size)

    return fig, ax
