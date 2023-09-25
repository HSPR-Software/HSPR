import warnings



warnings.filterwarnings('ignore')


import pandas as pd
import traceback, sys

from PyQt5.QtGui import *
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets  import QApplication, QVBoxLayout, QMainWindow, QFileDialog, QMessageBox, QHeaderView

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

from settings.about import info, txt
import settings.about
from func.read_zipdir import *
from func.clear_layout import *
from func.read_parameters import *
from func.add_results_to_dataframe import *
from func.plot_top_view import *
from func.plot_front_view import *
from func.get_open_files_and_dirs import *
from classes.WorkerSignals import *
from classes.LoadingCircle import *
from classes.Worker import *
from classes.Canvas import *
from classes.PandasModel import *
from ui.main_gui import Ui_MainWindow
from ui.IES_upload_gui import *
from ui.adb_zonecheck_gui import*
from func.adb_blockout_zone_check import adb_blockout_zone_check
from ui.computation_progressBar import ProgressWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # threadpool for multithreading
        self.threadpool = QThreadPool() 
        print("\n Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
   
        # create loading circle
        self.loading_circle = LoadingCircle()
        self.loading_screen.setMovie(self.loading_circle.movie)

        # single upload windows
        self.lb_upload_window = Ui_two_uploads()
        self.lb_upload_window.setWindowTitle("LB single IES upload")
        self.lb_upload_window.ok_btn.clicked.connect(lambda: self.getdatafromUI("LB",self.lb_upload_window))
        self.lb_upload_window.hide()

        self.hb_upload_window = Ui_two_uploads()
        self.hb_upload_window.setWindowTitle("HB single IES upload")
        self.hb_upload_window.ok_btn.clicked.connect(lambda: self.getdatafromUI("HB",self.hb_upload_window))
        self.hb_upload_window.hide()

        self.adb_upload_window = Ui_adb_uploads()
        self.adb_upload_window.ok_btn.clicked.connect(lambda: self.getdatafromUI("ADB",self.adb_upload_window))
        self.adb_upload_window.hide()

        self.adb_check_ui = Ui_zone_check()

        # connect buttons
        self.upload_button.clicked.connect(lambda: self.upload_data("ZIP"))
        self.upload_lb_btn.clicked.connect(lambda: self.upload_data("LB"))
        self.upload_hb_btn.clicked.connect(lambda: self.upload_data("HB"))
        self.upload_adb_btn.clicked.connect(lambda: self.upload_data("ADB"))
        self.clear_loadeddata_btn.clicked.connect(lambda: self.clear_uploadeddata())
        self.adb_quickcheck_btn.clicked.connect(lambda: self.adb_zone_check())
        self.compute_button.clicked.connect(self.compute_assessment)
        self.export_button.clicked.connect(self.export_results)

        #connect menubar
        self.howto_action.triggered.connect(lambda: self.usage_information())
        self.about_action.triggered.connect(lambda: self.about_information())

        #connect checkboxen
        self.checkbox_adb.stateChanged.connect(self.update_computebutton_status)
        self.checkbox_automatic.stateChanged.connect(self.update_computebutton_status)
        self.checkbox_automatic.stateChanged.connect(lambda: self.checkbox_manually.setChecked(False) if self.checkbox_automatic.isChecked() else False)
        self.checkbox_manually.stateChanged.connect(self.update_computebutton_status)
        self.checkbox_manually.stateChanged.connect(lambda: self.checkbox_automatic.setChecked(False) if self.checkbox_manually.isChecked() else False)
        self.checkbox_csv.stateChanged.connect(self.update_exportbutton_status)
        self.checkbox_xlsx.stateChanged.connect(self.update_exportbutton_status)

        self.width_lb.setValue(1.5)
        self.height_lb.setValue(.75)
        self.width_hb.setValue(1.5)
        self.height_hb.setValue(.75)
        self.width_adb.setValue(1.5)
        self.height_adb.setValue(.75)

        self.layout_dict = {
            'LB': [self.low_beam],
            'HB': [self.high_beam],
            'ADB_50': [self.adb50_oncoming, self.adb50_preceding],
            'ADB_100': [self.adb100_oncoming, self.adb100_preceding],
            'ADB_200': [self.adb200_oncoming, self.adb200_preceding],
        }

        self.seperator_list = ['Installation', 'Height', 'Width']
        self.mode_list = ['Low Beam', 'High Beam', 'ADB']
        global data
        data = {}


    def terminate(self):
        self.threadpool.clear()

    def checkbox_changed(self, state):
        pass

    def show_assessment(self, data):
        data = data[0]
        installation_data = [self.mode_list, data[1], data[2]]
        for index, key in enumerate(data[0].keys()):
            data[0][key].append(self.seperator_list[index])
            for list_index in range(len(installation_data)):
                data[0][key].append([item for item in installation_data[index]][list_index])

        del data[1:]  
        data = data[0]        
        global assessment_df       
        assessment_df = pd.DataFrame(data=data)        
        #Resize table
        self.show_dataframe(self.assessment_view, assessment_df)

    def show_table(self, data):
        data = data[1]
        #Create dataframe with result data
        global result_df
        result_df = add_results_to_dataframe(data)
        #Resize table
        self.show_dataframe(self.table_view, result_df)
        #Stop loading circle
        self.loading_circle.stop_animation()
        self.loading_screen.hide()

    def plot_layout(self, data, key):
        
        self.canvas = Canvas(self, width=12, height=4, dpi=100)
        ax_1 = self.canvas.figure.add_subplot(1, 1, 1)
        ax_1 = plot_front_view(self.canvas.figure, ax_1, data[0])
        #Add subplots to layout
        # ax_2 = self.canvas.figure.add_subplot(1, 2, 2) 
        # ax_2 = plot_top_view(self.canvas.figure, ax_2, data[1]) 
        #Add title to the figures
        self.canvas.figure.suptitle(''.join(['Front view of the light distribution for', ' (Both Headlamps)']), y=0.9)
        self.canvas.figure.tight_layout()        

        return self.canvas


    def tab_add_plot(self, data, key):
        if self.layout_dict[key][0].layout():
            clear_layout(self.layout_dict[key][0].layout())
            layout = self.layout_dict[key][0].layout()
        else:
            layout = QVBoxLayout()
        
        figure = self.plot_layout(data[:2], key)
        self.toolbar = NavigationToolbar(figure, self.layout_dict[key][0])
        layout.addWidget(self.toolbar)    
        layout.addWidget(figure)
        self.layout_dict[key][0].setLayout(layout) 

        if len(data) > 4:
            if self.layout_dict[key][1].layout():
                clear_layout(self.layout_dict[key][1].layout())
                layout = self.layout_dict[key][1].layout()
            else:
                layout = QVBoxLayout()
            
            figure = self.plot_layout(data[2:4], key)
            self.toolbar = NavigationToolbar(figure, self.layout_dict[key][1])
            layout.addWidget(self.toolbar)    
            layout.addWidget(figure)
            self.layout_dict[key][1].setLayout(layout) 
        else: 
            pass

    def upload_data(self, type):
        global data
        if type == "LB":
            self.lb_upload_window.show()
        elif type == "HB":
            self.hb_upload_window.show()
        elif type == "ADB":
            self.adb_upload_window.show()
        else:
            try:
                #cwd = os.getcwd()
                global folder_name
                #folder_name = get_open_files_and_dirs(None, "Open file", cwd)
                folder_name = QFileDialog.getOpenFileName(None, 'Open zip achive', 
                                None,"zip-archive (*.zip)")
                self.label_upload.setText(str(folder_name[0]))
                print('\n Following folder has been uploaded: {}'.format(folder_name[0]))
                data = read_zipdir(folder_name)
                self.lb_upload_window.restoreinitialButton()
                self.hb_upload_window.restoreinitialButton()
                self.adb_upload_window.restoreinitialButton()

            except Exception as e:
                pass
        self.update_computationmode_checkbox_status()

    def clear_uploadeddata(self):
        global data
        if len(data) > 0: self.statusbar.showMessage("Data has been cleared",2000)
        data = {}
        self.label_upload.clear()
        self.lb_upload_window.restoreinitialButton()
        self.hb_upload_window.restoreinitialButton()
        self.adb_upload_window.restoreinitialButton()
        self.update_computationmode_checkbox_status()
        self.update_exportbutton_status()


    def getdatafromUI(self,type,ui):
        try:
            ui_data = ui.datapaths
            if ((type == "LB") or (type == "HB")) and (len(ui_data) !=2): raise Exception("Please upload a right as well as a left ies file.")
            if (type == "ADB") and (len(ui_data) != 12): raise Exception("It is necessary to uploade all 12 ADB ies files ")
            else:
                global data
                data[type] = read_files(None,ui.datapaths)
                if type == "ADB": data[type][3] = ["Linie1_LH", "Linie1_RH", "Linie2_LH", "Linie2_RH","Linie3_LH", "Linie3_RH","Linie4_LH", "Linie4_RH","Linie5_LH", "Linie5_RH","Linie6_LH", "Linie6_RH"] #correction for necessary names in adb:assessment
                self.statusbar.showMessage(str(type)+" files have been uploaded",3500)
            self.update_computationmode_checkbox_status()

        except Exception as e:
            self.show_error_popup(e, str(e))
            return
        

    def clean_and_plot(self, data):
        print('\n Computation is over. Sending results to graphical user interface.')
        #Clear ADB layout if no ADB data
        if len(data[1].keys()) < 5:
            for key in list(self.layout_dict.keys())[2:]:
                clear_layout(self.layout_dict[key][0].layout())
                clear_layout(self.layout_dict[key][1].layout())
        #Insert plots into layout
        for key in data[1]:
            self.tab_add_plot(data[1][key], key)
        
        self.show_end_popup()
        
    def adb_zone_check(self):
        """Evaluates if Block-Out Zone is correct. """
        if "ADB" in data.keys() and len(data["ADB"][0]) == 12:
            adb_data = data["ADB"] #for example [0] is shape (12, 301, 901) so the 12 lines with data. [1]=horizontal and [2] is vertical
            #maxintensities_left_old = [1850,4250,625,5300,7000,1750,16000,5450]
            maxintensities_left = [2475,4250,975,5300,8750,1750,16000,5450]
            #maxintensities_right_old = [1850,2500,625,5300,7000,1750,16000,5450]
            maxintensities_right = [2475,4250,975,5300,8750,1750,16000,5450]
            measured_intensity_left,measured_intensity_right = adb_blockout_zone_check(adb_data[0],adb_data[1],adb_data[2], read_parameters([],[self.width_adb.text()],[])[1][0])
            self.adb_check_ui.fill_table_colorcoded(maxintensities_left,maxintensities_right,measured_intensity_left,measured_intensity_right)
            self.adb_check_ui.show()
        else: self.show_error_popup("Value Error", "Please upload all 12 ADB files before starting the evaluation.")


    def compute_assessment(self): 
        # run loading circle gif   
        self.loading_screen.show()     
        self.loading_circle.start_animation()
        progressWindow = ProgressWindow()
        progressWindow.progressBar.setMaximum(8)
        progressWindow.show()

        # read given height and width parameters
        width_list = [self.width_lb.text(), self.width_hb.text(), self.width_adb.text()]
        height_list = [self.height_lb.text(), self.height_hb.text(), self.height_adb.text()]
        computation_mode = [x.text() for x in [self.checkbox_manually, self.checkbox_automatic, self.checkbox_adb] if x.isChecked()]
        
        try:
            if len(data)<2: raise ValueError("Upload data before computing")
            if len(computation_mode) < 1: raise AssertionError("Please select at least one assessment mode.") 
            if "ADB" in data and computation_mode[0] != "ADB": raise AssertionError("Use ADB methode when having an ADB system!")
            if "ADB" not in data and computation_mode[0] == "ADB": raise AssertionError("Please upload ADB data if you want to use ADB mode.")

            else:                             
                predifined_height, predifined_width = read_parameters(height_list, width_list, computation_mode) 
                #data = read_zipdir(folder_name, predifined_height, predifined_width, computation_mode)
                # Uncomment for debugging
                # A, B = evaluate_data(data, predifined_height, predifined_width, computation_mode)
                if not data:
                    raise TypeError() 
                # Create Worker and add args
                self.worker_eval = Worker(evaluate_data,data, predifined_height, predifined_width, computation_mode)
                #self.worker_eval.args = (data, predifined_height, predifined_width, computation_mode,progressWindow)

                # Connect signals
                self.worker_eval.signals.updateProgressText.connect(lambda text: self.updateTextSlot(text, progressWindow))
                self.worker_eval.signals.updateProgressBar.connect(lambda value: self.updateProgressSlot(value, progressWindow))

                self.worker_eval.signals.result.connect(self.show_assessment)
                self.worker_eval.signals.result.connect(self.clean_and_plot)
                self.worker_eval.signals.result.connect(self.show_table)              
                
                # Execute
                self.threadpool.start(self.worker_eval) 


        except Exception as e:
            # stop loading circle
            progressWindow.close()
            self.loading_circle.stop_animation()
            self.loading_screen.hide()

            # show error message
            if 'NameError' in str(e.__class__):
                error_message = 'Please upload a folder before computing.'
                self.show_error_popup(e, error_message)
            elif 'TypeError' in str(e.__class__):
                pass
            else:
                error_message = e.args[0]
                self.show_error_popup(e, error_message)


    #@pyqtSlot(str)
    def updateTextSlot(self, text,progressWindow):
        progressWindow.updatetext(text)

    #@pyqtSlot(str)
    def updateProgressSlot(self, amount,progressWindow):
        progressWindow.increasebar_by(amount) 


    def export_results(self):
        #Merge result dataframes
        #Open folder dialog
        #root = tk.Tk()
        #root.withdraw()
        try:
            export_df = pd.concat([result_df, assessment_df])
            export_df = export_df.apply(lambda x: pd.Series(x.dropna().values))
            #export_file_path = filedialog.asksaveasfilename()
            predefined_name = settings.about.version
            if self.checkbox_csv.isChecked() and self.checkbox_xlsx.isChecked():
                export_file_path = QFileDialog.getSaveFileName(None, 'Save File as csv and xlsx', 
                                    ("HSPR_"+predefined_name),"Datatype (*.csv *.xlsx)")
                if export_file_path != ('', ''):
                    export_file_path = str(export_file_path[0].split(".")[0])
                    export_df.to_csv((export_file_path+".csv"), index=False)
                    export_df.to_excel((export_file_path+".xlsx"), index=False)
            elif self.checkbox_csv.isChecked() : 
                export_file_path = QFileDialog.getSaveFileName(None, 'Save File as csv', "HSPR_"+predefined_name,"(*.csv)") 
                if export_file_path != ('', ''):
                    export_df.to_csv(export_file_path[0], index=False)
            elif self.checkbox_xlsx.isChecked():
                export_file_path = QFileDialog.getSaveFileName(None, 'Save File as xlsx', "HSPR_"+predefined_name,"(*.xlsx)")
                if export_file_path != ('', ''):
                    export_df.to_excel(export_file_path[0], index=False)            
        
        #except NameError: return
        except Exception as e:
            print(e)
            # stop loading circle
            self.loading_circle.stop_animation()
            self.loading_screen.hide()
            # show error message
            if 'NameError' in str(e.__class__): error_message = "You need a finished calculation before exporting results."
            else: error_message = 'Invalid name for exporting data.\n Please enter a valid name when exporting.'
            self.show_error_popup(e, error_message)
            return
            

    def show_end_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Completed")
        msg.setText('Computation is complete. Results and plots have been updated.')      
        x = msg.exec_()

    def show_error_popup(self, error_type, error_message):
        msg = QMessageBox()
        msg.setWindowTitle("Error message")
        msg.setText(''.join([str(error_type.__class__), ' ', error_message]))      
        x = msg.exec_()

    def usage_information(self):
        msg = QMessageBox()
        msg.setWindowTitle("Usage Information")
        msg.setText(txt)            
        x = msg.exec_()

    def about_information(self):
        msg = QMessageBox()
        msg.setWindowTitle("Software Information")
        msg.setText(info)     
        msg.setTextFormat(1)  # Qt.TextFormat = 1 for HTML to display the mail address as a link       
        x = msg.exec_()

    def align_table(self, frame):
        #Table will fit the frrame widget horizontally
        frame.horizontalHeader().setStretchLastSection(True)
        frame.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
    
    def show_dataframe(self, frame, data):
        #Show Dataframe on the Frame widget 
        model = PandasModel(data)
        frame.setModel(model)
        self.align_table(frame)

    def closeEvent(self, event):
            event.accept()
            self.lb_upload_window.close()
            self.hb_upload_window.close() 
            self.adb_upload_window.close() 
            self.adb_check_ui.close() 


    def update_computationmode_checkbox_status(self):
        global data
        keys = data.keys()
        self.checkbox_adb.setChecked(False)
        self.checkbox_manually.setChecked(False)
        self.checkbox_automatic.setChecked(False)
        self.checkbox_adb.setEnabled(False)
        self.checkbox_manually.setEnabled(False)
        self.checkbox_automatic.setEnabled(False)

        if bool("ADB" in keys) & bool("LB" in keys) & bool("HB" in keys): 
            self.checkbox_adb.setEnabled(True)
            self.checkbox_adb.setChecked(True)


        elif bool("LB" in keys) & bool("HB" in keys): 
            self.checkbox_manually.setEnabled(True)
            self.checkbox_automatic.setEnabled(True)



    def update_computebutton_status(self):
        #todo Bedingungen unten noch beser anpassen
        self.computation_mode = [x.text() for x in [self.checkbox_manually, self.checkbox_automatic, self.checkbox_adb] if x.isChecked()]
        if bool(self.computation_mode): self.compute_button.setEnabled(True)
        else: self.compute_button.setEnabled(False)

    def switch_manuell_automatic_checkboxstate(self,button):
        if button.isChecked:
            self.checkbox_automatic.setChecked(False)
            self.checkbox_manually.setChecked(False)
            button.setChecked(True)



    def update_exportbutton_status(self):
        if self.checkbox_xlsx.isChecked() or self.checkbox_csv.isChecked():
            self.export_button.setEnabled(True)
        else: self.export_button.setEnabled(False)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    #MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "taskbar_icon.png")))
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())