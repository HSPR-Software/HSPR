
version = "2.1.1"

info = '''
Software Version '''+ str(version)+''' <br>
Laboratory of Adaptive Lighting Systems and Visual Processing <br>
Technical University of Darmstadt <br><br>
Helpdesk:<br>
<a href='mailto:HSPR-software@lichttechnik.tu-darmstadt.de'> HSPR-software@lichttechnik.tu-darmstadt.de </a> <br><br>
'''

txt = '''
This Application is used to assess the light distribution of various headlight systems. \n
Please take the following steps to avoid any Errors: \n
1) Upload the .ies files either in a single .zip folder containing the subfolders ADB, HB, and LB and the .ies files named according to the software manual.
    Alternatively upload the files separately with the corresponding buttons. The second methode does not require specific file names. It is required that the line "TILT=NONE" of every IES file is followed by 13 numbers representing the lights parameters. \n
2) Change the inputparameters to your car geometry. \n
3) If you don't use an ADB system check manual or automatic. ADB systems are automatically selected. \n
4) Start the computation by clicking on the Compute button. \n
5) Wait until the progressbar is full and the results are displayed. \n
Optional: Export the results in .xlsx or .csv format. \n
'''

#2) Check the ADB box if the data contains ADB light distributions.\n
#3) Adjust installation height and headlamp width, otherwise  
#   default values (height=0.75, width=1.5) will be used. \n
#4) Click on Compute to start the computation. After a brief amount of time 
#   the results should appear on the upper windows in table form and 
#   plots should appear in thier corresponding tabs.\n
#5) The results can be exported either in .xlsx or .csv format.