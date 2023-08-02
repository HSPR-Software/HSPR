import copy
import zipfile
import matplotlib.pyplot as plt

# from main import MainWindow  ##!!!
from .read_files import *
from .evaluate_data import *

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
    try:
        with zipfile.ZipFile(directory[0]) as z:
            files = {"LB":[], "HB":[], "ADB":[]}
            filenames = list(filter(lambda x:x.endswith('.ies'), z.namelist()))

            for file in filenames:
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
        plt.close('all')
        if 'IndexError' in str(e.__class__):
            error_message = "Folder is not complete. Either LB or HB folder or a file within the folders is missing."
        else:
            error_message = e.args[0]
        # MainWindow.show_error_popup(MainWindow, e, error_message)
        print(e, error_message)
    