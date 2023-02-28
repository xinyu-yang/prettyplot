#! python3

__all__ = [
        "smoothing",
        "set_default_visible"
        ]

def smoothing(data, step):
    """
    smoothing the data list
    :param data: list or tuple of data
    :param step: step size, int
    """
    import numpy as np
    res = []
    data = np.array(data)
    for i in range(data.shape[0] // step):
        res.append(data[step*i:step*(i+1)].mean())
    res.append(data[-(data.shape[0]%step):].mean())
    return res

def set_default_visible(fig, ax):
    # Set the border the figure
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Set the background color of the image
    fig.patch.set_visible(False)
    ax.patch.set_visible(False)

    return True
