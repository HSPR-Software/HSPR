import numpy as np

def find_nearest(array, value):
    """find the nearest integer to a value in the given array

    Args:
        array ([array])
        value ([int]): [value which should be found]

    Returns:
        [int]: [nearest integer to the searched value ]
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]