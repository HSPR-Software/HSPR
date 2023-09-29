import copy
import zipfile

from func.read_files import *
from func.evaluate_data import *

def read_zipdir(directory):
    """Unzip the uploaded folder and read the files within

    Args:
        directory ([str]): [contains the location of the uploaded .Zip folder]
        predifined_height (list): [Contains the headlamp installation height for the different assessments]
        predifined_width (list): [Contains the headlamp installation width for the different assessments]
        assessment_mode (list): [Contains the computation mode selected by the user]

    Raises:
        Exception: [Raise an error if the incorrect computation mode has been selected]

    Returns:
        [dic]: [description]
    """
    uploaded_data = {}
    current_file =""
    try:
        with zipfile.ZipFile(directory[0]) as z:
            files = {"LB":[], "HB":[], "ADB":[]}
            filenames = list(filter(lambda x:x.endswith('.ies'), z.namelist()))

            for file in filenames:
                current_file = file
                if file.split("/")[0] == "LB": files["LB"].append(file)
                if file.split("/")[0] == "HB": files["HB"].append(file)
                if file.split("/")[0] == "ADB": files["ADB"].append(file)
            if len(files["ADB"])==0: del files["ADB"]
            for folder in files:
                if len(files[folder]) > 0:
                    uploaded_data[folder] = read_files(z, files[folder])

            #if len(uploaded_data["ADB"]) == 0: del uploaded_data["ADB"]
            return uploaded_data
            
    except Exception as e: 
        raise  type(e)(f"\nOccured in file {current_file}: \n{e}")
