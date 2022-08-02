#! python3
import numpy as np

def smoothing(data, step):
    """
    smoothing the data list
    :param data: list or tuple of data
    :param step: step size, int
    """
    res = []
    data = np.array(data)
    for i in range(data.shape[0] // step):
        res.append(data[step*i:step*(i+1)].mean())
    res.append(data[-(data.shape[0]%step):].mean())
    return res

