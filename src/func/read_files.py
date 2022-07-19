import numpy as np
from main import MainWindow 

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
    data_content = []
    angle_information = []
    names = []
    #assessment = file_path[0].split("/")[-2]
    try :
        for index in range(len(file_path)):
            filename = file_path[index]
            names.append(filename.split("/")[-1].split(".")[0])
            
            if zip != None:
                data = zip.open(filename, "r")
            elif zip == None:
                data = open(filename)

            data_lines = data.readlines()
            data_content = []
            for line in data_lines:
                #Decode from bytes to string
                if zip != None: line = str(line,'utf-8')
                
                data_content.append(" ".join(line.split()))  

            # index1 = [i for i, string in enumerate(data_content) if str(string, 'utf-8') == 'TILT=NONE\r\n']
            # index2 = [i for i, string in enumerate(data_content) if str(string, 'utf-8') == '1 1 0\r\n']   
            # index1 = [i for i, string in enumerate(data_content) if str(string, 'utf-8').rstrip() == 'TILT=NONE']
            # index2 = [i for i, string in enumerate(data_content) if str(string, 'utf-8').rstrip() == '1 1 0'] 

            
            index1 = [i for i, string in enumerate(data_content) if string.rstrip() == 'TILT=NONE']
            index2 = [i for i, string in enumerate(data_content) if string.rstrip() == '1 1 0']   


            #index2 = [index1[0]+2]

            # get lumen information from data
            lumen_information = [data_content[index1[0]+1].split(" ")[1] if data_content[index1[0]+1].split(" ")[1].replace(".","").isdigit() else -1]
            # for i, string in enumerate(data_content):
            #     # if str(string, 'utf-8') == 'TILT=NONE\r\n':
            #     if string.rstrip() == 'TILT=NONE':
            #         i+=1
            #         break
            
            # lumen_information.append(str(data_content[i], 'utf-8').split(" ")[1])
            # lumen_information = [str(data_content[i], 'utf-8').split(" ")[1] if str(data_content[i], 'utf-8').split(" ")[1].replace(".","").isdigit() else -1]


            # get angle_information from data
            for i in range(index1[0]+1, index2[0]+1):
                # temp = str(data_content[i], 'utf-8').split("\r\n")[0]
                temp = data_content[i].rstrip()
                for char in temp.split(" "):
                    angle_information.append(float(char) if char.isdigit() else -1)
            length_angle_vert = angle_information[3] #amount of vertical angular datapoints
            length_angle_hori = angle_information[4]  #amount of horizontal angular datapoints

            angle_vert = []
            angle_hori = []

            score_vert = 0
            score_hori = 0

            # calculate score_vertical
            for i in range(index2[0]+1, len(data_content)+1): 
                if score_vert < length_angle_vert: 
                    # new_vert_angles = str(data_content[i], 'utf-8').rstrip()
                    # new_vert_angles = str(data_content[i], 'utf-8').split("\r\n")[0].split(" ")
                    # new_vert_angles.remove("")
                    new_vert_angles = data_content[i].split(" ") 

                    new_vert_angles= list(filter(("").__ne__, new_vert_angles))
                    angle_vert.append(new_vert_angles)
                    score_vert = score_vert + len(new_vert_angles)
                    start_j = i+1  
            appended_angle_vert = []
            for row in angle_vert:
                for number in row:
                    #isfloat(number) 
                    appended_angle_vert.append(number)
            angle_vert = appended_angle_vert
            #angle_vert = [number for row in angle_vert for number in row]

            # calculate score_horizontal
            for j in range(start_j, len(data_content)+1):
                if score_hori<length_angle_hori:
                    # new_hori_angles = str(data_content[j], 'utf-8').rstrip()
                    # new_hori_angles = str(data_content[j], 'utf-8').split("\r\n")[0].split(" ")
                    # new_hori_angles.remove("")
                    new_hori_angles = data_content[j].split(" ")
                    new_hori_angles= list(filter(("").__ne__, new_hori_angles))
                    angle_hori.append(new_hori_angles)
                    score_hori = score_hori + len(new_hori_angles)
                    start_k = j+1
            angle_hori = [number for row in angle_hori for number in row]

            if index == 0:
                matrix = np.zeros((len(file_path), int(length_angle_vert), int(length_angle_hori)))    

            # need to be changed maybe (see Matlab)   
            for i in range(int(length_angle_hori)):
                score_vert = 0
                values = []
                for k in range(start_k, len(data_content)+1):
                    if score_vert < length_angle_vert:
                        # vert_values = str(data_content[k], 'utf-8').rstrip()
                        # vert_values = str(data_content[k], 'utf-8').split("\r\n")[0].split(" ")
                        # vert_values.remove("")
                        vert_values = data_content[k].split(" ")
                        vert_values= list(filter(("").__ne__, vert_values))
                        values.append(vert_values)
                        score_vert = score_vert + len(vert_values)
                        start_k = k+1
                    else:
                        temp = [number for row in values for number in row]
                        temp= list(filter(("").__ne__, temp))
                        matrix[index,:,i] = temp
                        break
    except Exception as e:        
        if 'IndexError' in str(e.__class__):
            error_message = "One of the files contains too many or misses values."
        elif "ValueError" in str(e.__class__):
            error_message = "One data entry might not be a value or is otherwise corrupted. Please check the uploaded files."
        else:
            error_message = e.args[0]
        MainWindow.show_error_popup(MainWindow, e, error_message)
        return

    # Covert angles into numpy array
    angle_hori = np.array(angle_hori, dtype=np.float) 
    angle_vert = np.array(angle_vert, dtype=np.float)     

    return [matrix, angle_hori, angle_vert, names]

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        print("Fehlerhafter Eintrag: ",num)

        return False

