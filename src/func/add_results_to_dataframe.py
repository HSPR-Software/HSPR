import numpy as np
import pandas as pd
from ..settings.configuration import db_system_endscores, db_system_average

def add_results_to_dataframe(data):
    """Add and structure computed results to a new dataframe

    Args:
        data ([dictionary]): [data of all assessments]

    Returns:
        [Dataframe]: [Dataframe with actual and point score of all assessments]
    """
    # Create new dataframe with end results  
    lower_actual = []
    lower_points = []
    upper_actual = []
    upper_points = []
    point_list = []   
    actual_list = []

    if 'ADB_50' in data.keys():
        extracted_df = db_system_average.copy(deep=True)
        for key in data:
            if '0' in key:
                # delete ADB glare values of 100 and 200 lines
                if '100' in key or '200' in key:
                    del data[key][4][0][3], data[key][4][1][3]
                    del data[key][4][0][-2], data[key][4][1][-2]
                midpoint= np.int(len(data[key][4][0])/2)

                lower_actual.append(data[key][4][0][:midpoint])
                lower_points.append(data[key][4][1][:midpoint])
                upper_actual.append(data[key][4][0][midpoint:])
                upper_points.append(data[key][4][1][midpoint:])
            else:
                actual_list.append(data[key][2][0])
                point_list.append(data[key][2][1])
        
        lower_actual = sum(lower_actual, [])
        lower_points = sum(lower_points, [])
        upper_actual = sum(upper_actual, [])
        upper_points = sum(upper_points, [])
        
        flat_actual_list = [item for sublist in [actual_list[0], actual_list[1], lower_actual, upper_actual] for item in sublist]
        flat_points_list = [item for sublist in [point_list[0], point_list[1], lower_points, upper_points] for item in sublist]
    else:
        extracted_df = db_system_average.drop(db_system_average[db_system_average.Type.str.lower().str.contains('adb')].index).copy(deep=True)
        for key in data:
            actual_list.append(data[key][2][0])
            point_list.append(data[key][2][1])
        flat_actual_list = sum(actual_list, [])
        flat_points_list = sum(point_list, [])

    # Add data to Dataframe
    extracted_df['Actual Score'] = flat_actual_list
    extracted_df['Point Score'] = flat_points_list
    del extracted_df['Average Score']

    return extracted_df