import os
import math
import numpy as np
import pandas as pd
from func.safety_performance_level import *
    
def compute_overall_assessment(assessment_points, adb_checked):
    """compute the overall assessment from TC4-45 of the given .ies data
        depending on the reached points

    Args:
        assessment_points ([dict]): [reached points pro category]

    Returns:
        [list]: [reached MEP and overall assessment]
    """
    # performance variables
    effective_performance = {}

    for key in assessment_points.keys():
            if 'LB' in key:
                effective_performance[key] = np.around(9.71 * assessment_points[key] + 53.24, decimals=3)
            elif 'HB' in key:
                effective_performance[key] = np.around(23.91 * assessment_points[key] + 90.35, decimals=3)
            else:
                adb_mean = np.around(np.mean([assessment_points['ADB_50'], assessment_points['ADB_100'], assessment_points['ADB_200']]), decimals=3)
                effective_performance[key.split('_')[0]] = np.around(9.65 * adb_mean + 98.43, decimals=3)
                break
    
    # compute manually and automatic mean effective_performance
    mep_manually = 0.9 * effective_performance['LB'] + 0.1 * effective_performance['HB'] 
    mep_automatic = 0.7 * effective_performance['LB'] + 0.3 * effective_performance['HB'] 

    mep_manually = np.around(0.611 * mep_manually - 37.66, decimals=3)
    mep_automatic = np.around(0.611 * mep_automatic - 37.66, decimals=3)

    # if self.checkbox_adb.isChecked():
    #     # Create dataframe with result data
    #     d = {'Assessment': ['EP LB', 'EP HB', 'EP ADB', 'MEP Manually', 'MEP Automatic', 'MEP ADB', 'Overall MEP'], 
    #             'Result': data}
    # else:
    #     d = {'Assessment': ['EP LB', 'EP HB', 'MEP Manually', 'MEP Automatic', 'Overall MEP'], 
    #             'Result': data}

    if adb_checked:
        # compute adb mean effective_performance 
        mep_adb = 0.3 * effective_performance['LB'] + 0.3 * effective_performance['HB'] + 0.4 * effective_performance['ADB']  
        mep_adb = np.around(0.611 * mep_adb - 37.66, decimals=3)
        overall_performance = safety_performance_level(np.mean([mep_manually, mep_automatic, mep_adb]))
        return [mep_manually, mep_automatic, mep_adb, overall_performance]

    else:
        overall_performance = safety_performance_level(np.mean([mep_manually, mep_automatic]))
        return [mep_manually, mep_automatic, overall_performance]