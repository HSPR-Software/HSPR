import os
import math
import numpy as np
import pandas as pd
from .safety_performance_level import *
    
def effective_performance(assessment_points, assessment_mode):
    """compute the overall assessment from TC4-45 of the given .ies data, depending on the reached points        

    Args:
        assessment_points ([dict]): [reached points pro category]
        assessment_mode ([list]): [contains the assessment mode selected by the user]

    Returns:
        [list]: [reached MEP and overall assessment]
    """
    
    # performance variables
    effective_performance = {}
    for key in assessment_points.keys():
            if 'LB' in key:
                effective_performance[key] = np.around(5.8 * assessment_points[key] + 64.17, decimals=2)
            elif 'HB' in key:
                effective_performance[key] = np.around(11.71 * assessment_points[key] + 141.27, decimals=2)
            else:
                adb_mean = np.around(np.mean([assessment_points['ADB_50'], assessment_points['ADB_100'], assessment_points['ADB_200']]), decimals=2)
                # result = np.around(np.multiply(np.divide(4, best-worst), adb_mean-worst)+1, decimals=2)
                effective_performance[key.split('_')[0]] = np.around(10.87 * adb_mean + 94.13, decimals=2)
                break

    result = [value for value in effective_performance.values()].copy()

    # compute mean effective_performance
    if 'Manually' in assessment_mode:   
        mep = 0.95 * effective_performance['LB'] + 0.05 * effective_performance['HB']

    elif 'Automatic' in assessment_mode: 
        mep = 0.8 * effective_performance['LB'] + 0.2 * effective_performance['HB'] 

    elif 'ADB' in assessment_mode: 
        mep = 0.3 * effective_performance['LB'] + 0.2 * effective_performance['HB'] + 0.5 * effective_performance['ADB']  

    mep_score = np.around(0.626 * mep - 36.42, decimals=1)
    overall_performance = safety_performance_level(mep_score)

    try:
        data = {
        'Assessment': ['Low Beam', 'High Beam', 'ADB', ''.join([assessment_mode[0], ' Headlamp System'])],
        'Score': [assessment_points['LB'], assessment_points['HB'], adb_mean, mep_score],
        'Score Class': [safety_performance_level(assessment_points['LB']*10), safety_performance_level(assessment_points['HB']*10), safety_performance_level(adb_mean*10), overall_performance]
        } 
    except UnboundLocalError:
        data = {
        'Assessment': ['Low Beam', 'High Beam', ''.join([assessment_mode[0], ' Headlamp System'])],
        'Score': [assessment_points['LB'], assessment_points['HB'], mep_score],
        'Score Class': [safety_performance_level(assessment_points['LB']*10), safety_performance_level(assessment_points['HB']*10), overall_performance]
        } 

    return data