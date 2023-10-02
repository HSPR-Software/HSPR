from os import read
import numpy as np
from main import MainWindow 
from scipy.interpolate import interp2d

import re
import numpy as np

def read_ies_file(filetext):
    # Initialize variables
    metadata = {}
    vertical_angles = []
    horizontal_angles = []
    candela_values = []
    
    # Split the file into lines
    lines = filetext.split("\n")
    
    # Process each line
    tilt_none_index = -1
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("["):
            # This is a keyword line
            keyword, value = line[1:].split("]", 1)
            metadata[keyword.strip()] = value.strip()
        elif line == "TILT=NONE":
            # This marks the end of the header and the beginning of the data
            tilt_none_index = i
            break
        elif line == "TILT=INCLUDE": 
            raise Exception("The HSPR Software currently does not support TILT=INCLUDE please make sure light distribution is designed for TILT=NONE.")
    

    # Check and process the line containing 10 values
    next_line = re.split(r'[,\s\r\n]+', lines[tilt_none_index + 1].strip())
    if len(next_line) != 10:
        raise Exception("The line following TILT=NONE must contain exactly 10 numerical values with the photometric specifications.")

    # Convert and assign the 10 photometric specifications
    conversion_funcs = [int, float, float, int, int, int, int, float, float, float]

    num_lamps, lumens_per_lamp, candela_multiplier, num_vert_angles, num_horiz_angles, photometric_type, units_type, width, length, height = [func(val) for func, val in zip(conversion_funcs, next_line)]

    # Check and process the line containing 3 values
    next_line = re.split(r'[,\s\r\n]+', lines[tilt_none_index + 2].strip())
    if len(next_line) != 3:
        raise Exception("The line following the 10-value line must contain exactly 3 numerical values.")

    # Convert and assign the next three values: ballast factor, file generation type, input watts
    ballast_factor, file_generation_type, input_watts = map(float, next_line)

    remaining_data = "".join(lines[tilt_none_index + 3:])
    new_iterator = iter(re.split(r'[,\s\r\n]+', remaining_data.strip()))

    vertical_angles = np.array([float(next(new_iterator)) for _ in range(num_vert_angles)])
    horizontal_angles = np.array([float(next(new_iterator)) for _ in range(num_horiz_angles)])
    candela_values = np.array([float(next(new_iterator)) for _ in range(num_vert_angles * num_horiz_angles)])

    if num_vert_angles*num_horiz_angles != len(candela_values):
        raise ValueError(f"There is an error in the ies file. Please check if the file contains the prescribed quantity of photometric values and keywords.") 

    candela_values = candela_values.reshape((num_horiz_angles, num_vert_angles)).T 

    #min_diff = np.min(np.abs(np.diff(horizontal_angles)))
    #horizontal_angles_new = np.arange(horizontal_angles[0], horizontal_angles[-1] + min_diff, min_diff)
    horizontal_angles_new = np.arange(-45, 45.05, 0.05)

    #min_diff = np.min(np.abs(np.diff(vertical_angles)))
    #vertical_angles_new = np.arange(vertical_angles[0], vertical_angles[-1] + min_diff, min_diff)
    vertical_angles_new = np.arange(-15, 15.05, 0.05)

    interpolator = interp2d(horizontal_angles,vertical_angles,candela_values, kind="linear", fill_value=0) 
    candela_values  = interpolator(horizontal_angles_new, vertical_angles_new)

    return metadata, vertical_angles_new, horizontal_angles_new, candela_values



def read_files(zip, file_path):
    names = []
    matrix = []
    
    for index in range(len(file_path)):
        filename = file_path[index]
        names.append(filename.split("/")[-1].split(".")[0])
        
        if zip is None:
            with open(filename,'r', encoding="utf-8") as file:
                data = file.read()
        else:
            with zip.open(filename,'r') as file:
                data = file.read().decode("utf-8")
        
        metadata, vertical_angles, horizontal_angles, candela_values = read_ies_file(data)
        matrix.append(candela_values)
        #horizontal_angles.append(horizontal_angles) #angles of the files have to be the same currently caught by interpolating everything to the same angles
        #vertical_angles.append(vertical_angles)

    return np.array(matrix), horizontal_angles, vertical_angles, names


