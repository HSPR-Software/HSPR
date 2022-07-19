import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.patches as patches

from gui import Ui_MainWindow 

from func.effective_performance import *
from assessments.lb_assessment import *
from assessments.hb_assessment import *
from assessments.adb_assessment import *

def evaluate_data(data, predifined_height, predifined_width, assessment_mode): 
    """Manege the evaluation process for the different assessments

    Args:
        data ([dict]): [contains LB, HB, and ADB data]
        predifined_height ([list]): [installation height for the different assessments]
        predifined_width ([list]): [installation width for the different assessments]
        assessment_mode ([list]): [contains the assessment mode selected by the user]

    Returns:
        [list]: [Assessment results]
    """

    results = {} 

    for key in data:
        print('---------{}-----------'.format(key))
        if 'LB' in key: 
            results[key] = lb_assessment(data[key], predifined_height[0], predifined_width[0])
            pass
        elif 'HB' in key:
            results[key] = hb_assessment(data[key], predifined_height[1], predifined_width[1])   
            pass  
        elif len(data["ADB"])>0:
            lines = [line.split('_')[0] for line in data['ADB'][3]]
            temp_list = adb_assessment(data[key], lines, predifined_height[2], predifined_width[2])
            
            # add results to dictionary
            results[''.join([key,'_50'])] = temp_list['50']
            results[''.join([key,'_100'])] = temp_list['100']
            results[''.join([key,'_200'])] = temp_list['200']
    
    # Close all graphs produced with matplotlib    
    plt.close('all')

    # split data
    assessment_points=dict()
    try:
        for key in results:
            assessment_points[key] = results[key][-1]
            del results[key][-1]
    except Exception as e:
        pass

    return [effective_performance(assessment_points, assessment_mode), predifined_height, predifined_width], results