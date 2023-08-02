import numpy as np
from ..settings.configuration import Performance_Levels

def safety_performance_level(performance):
    """find the corrsponding perfomance level from the computed score
    Args:
        performance ([int]): [computed performance level depending of the LB, HB and ADB assesment]

    Returns:
        [str]: [peformance level depending on reached value]
    """
    if performance < 10:
        performance = Performance_Levels[0]
    elif performance > 50:
        performance = Performance_Levels[-1]
    else:
        index = np.int(np.around(performance/10, decimals=1))
        performance = Performance_Levels[index]
    
    return performance