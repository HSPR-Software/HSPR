from os import read
import numpy as np
from main import MainWindow 
from scipy.interpolate import interp2d


def read_files(zip, file_path):
    """Encodes the uploaded .ies data within the given .zip folder

    Args:
        zip ([zipfile]): [the uploaded zipfile]
        file_path ([list]): [containing the strings with the location of the .ies files]

    Returns:
        [array]: [holds the light intensity]
        [array]: [horizontal angles]
        [array]: [vertical angles]
        [list]: [name of the data]
    """    
    # variables
    names = []
    #assessment = file_path[0].split("/")[-2]
    h_angles = []
    v_angles = []
    matrix = []
    try :
        for index in range(len(file_path)):
            filename = file_path[index]
            names.append(filename.split("/")[-1].split(".")[0])
            
            if zip == None:
                with open(filename,'r', encoding="utf-8") as file:
                    data = file.read()
                    filetext = data.replace("\r", " ").replace("\n"," ").replace("  ", " ").strip()

            else:
                with zip.open(filename,'r') as file:
                    data = file.read().decode("utf-8")
                    filetext = data.replace("\r", " ").replace("\n","").replace("  ", " ").strip()
            h_angles, v_angles, light_intensities = ies_file_read(filetext)
            matrix.append(light_intensities)
            
        return np.array(matrix), np.array(h_angles), np.array(v_angles), names
    except Exception as e:        
        if 'IndexError' in str(e.__class__):
            error_message = "One of the files contains too many or misses values."
        elif "ValueError" in str(e.__class__):
            error_message = "One data entry might not be a value or is otherwise corrupted. Please check the uploaded files."
        else:
            error_message = e.args[0]
        MainWindow.show_error_popup(MainWindow, e, error_message)
        return


"""Reads vertical and horizontal angles as well as the values out of an .ies file."""
def ies_file_read(filetext):
    #with open(path, "r") as file:
    #filetext = file.replace("\r", " ").replace("\n"," ").replace("  ", " ").strip()
    info = []  

    idx_tilt = filetext.find('TILT=NONE')
    if idx_tilt == -1: 
        #print("TILT not mentioned or not NONE.")  
        raise Exception("TILT not mentioned in the IES file or not NONE.\nMake sure your IES files contain TILT=NONE in the line before the headlight specifications.")

    content = filetext[idx_tilt+10:].split(" ") #puts everything after the header content in a list tilt=none is 9 long so +1=10
    info = content[:13] #hardcounted the 13 numbers which represent the lights data
    v_angles_num = int(info[3])
    h_angles_num = int(info[4])
    v_angles = [float(number) for number in content[13:13+v_angles_num]]
    h_angles = [float(number) for number in content[13+v_angles_num:13+v_angles_num+h_angles_num]]

    light_intensities = [float(number) for number in content[13+v_angles_num+h_angles_num:]]
    light_intensities = np.reshape(light_intensities, (h_angles_num, v_angles_num)).T 


    #corrects horizontal and vertical angles that have different step sizes
    diff = abs(h_angles[1] - h_angles[0])
    for idx, h in enumerate(h_angles[1:]):
        diff2 = abs(h - h_angles[idx])
        if diff2 < diff:
            diff = diff2
    h_angles_new = np.arange(h_angles[0], h_angles[-1]+diff, diff)

    diff = abs(v_angles[1] - v_angles[0])
    for idx, v in enumerate(v_angles[1:]):
        diff2 = abs(v - v_angles[idx])
        if diff2 < diff:
            diff = diff2
    v_angles_new = np.arange(v_angles[0], v_angles[-1]+diff, diff)

    #now interpolates the matri to fit the new angles
    interpolator = interp2d(h_angles,v_angles,light_intensities, kind="linear") 

    return h_angles_new, v_angles_new,   interpolator(h_angles_new, v_angles_new)



    #in ies files the it runs through the vertical angles first which means it is arranged as 
    # vertical sublists in horizontal angles so horizontal is the row vector and vertical the 
    # column verctor so thats why it gets transposed to fit the intuitive allignment 

   # return h_angles, v_angles, light_intensities

