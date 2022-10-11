import math

def read_parameters(height_list, width_list, computation_mode):
    """Reads and converts the headlamp installation parameters 

    Args:
        height_list ([list]): [Contains the headlamp installation height for the different assessments]
        width_list ([list]): [Contains the headlamp installation width for the different assessments]
        computation_mode ([list]): [Contains the computation mode selected by the user]

    Returns:
        [list]: [Contains the headlamp installation height and width of the headlamps]
    """
    min_width = 0    
    max_width = math.inf  
    standard_width = 1.5

    min_height = 0
    max_height = math.inf
    standard_height = 0.75

    for index, value in enumerate(height_list):
        if value.replace('.', '', 1).isdigit():
            height_list[index] =  float([value if float(value)>min_height and float(value)<max_height else standard_height][0])
        elif value.replace(',', '', 1).isdigit():
            height_list[index] =  float([value.replace(',', '.', 1) if float(value.replace(',', '.', 1))>min_height and float(value.replace(',', '.', 1))<max_height else standard_height][0])
        else:
            height_list[index] = standard_height

    for index, value in enumerate(width_list):
        if value.replace('.', '', 1).isdigit():
            width_list[index] =  float([value if float(value)>min_width and float(value)<max_width else standard_width][0])
        elif value.replace(',', '', 1).isdigit():
            width_list[index] =  float([value.replace(',', '.', 1) if float(value.replace(',', '.', 1))>min_width and float(value.replace(',', '.', 1))<max_width else standard_width][0])
        else:
            width_list[index] = standard_width 



    return height_list, width_list