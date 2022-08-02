#!/usr/bin/python3
from .config import *

__all__ = [
        "rocs",
        ]


def rocs(labels, scores, settings, fig_setting):
    '''
    Draw ROC curve
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
    from sklearn.metrics import roc_curve, auc, roc_auc_score

    fig = plt.figure()
    title = fig_setting.get("title") if fig_setting.get("title") else ""
    scale = fig_setting.get("scale") if fig_setting.get("scale") else (1, 1)
    ## Figure size
    (width_scale, height_scale) = scale
    width, height = fig.get_size_inches()
    fig.set_size_inches(width*width_scale, height*height_scale)
    ## Label Size
    label_size = fig_setting.get("label_size") if fig_setting.get("label_size") else 10
    ## Title Size
    title_size = fig_setting.get("title_size") if fig_setting.get("title_size") else 12
    ## Line width
    line_width = fig_setting.get("line_width") if fig_setting.get("line_width") else 1
    ## Get Axes
    ax = fig.add_axes([0, 0, 1, 1])

    for idx, (label, score, setting) in enumerate(zip(labels, scores, settings)):
        fpr, tpr, threshold = roc_curve(label, score)
        roc_auc = auc(fpr, tpr)
        ## Colors
        color = setting.get("color") if setting.get("color") else COLOR[idx % len(COLOR)]
        ## Linestyle
        linestyle = setting.get("linestyle") if setting.get("linestyle") else LINESTYLE[0]
        ## Label
        label = setting.get("label") if setting.get("label") else "ROC curve (area = %0.2f)" % roc_auc
        
        ax.plot(fpr, tpr, color=color, lw=line_width, label=label, linestyle=linestyle)
    
    # Reference line
    ax.plot([0, 1], [0, 1], color="grey", lw=line_width, linestyle="--")
    ax.tick_params(axis="both", labelsize=12)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("False Positive Rate", fontsize=label_size)
    ax.set_ylabel("True Positive Rate", fontsize=label_size)
    ax.set_title(title, fontsize=title_size)

    return fig, ax
