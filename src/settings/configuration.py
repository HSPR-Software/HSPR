import os
import numpy as np
import pandas as pd
import configparser

## App settings
name = "Headlamp Safety Performance Rating"

host = "0.0.0.0"

port = int(os.environ.get("PORT", 5000))

debug = True

contacts = "https://www.linkedin.com" ##???

code = "https://github.com"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css' ###???

username = 'rajanovich' # Plotly account username

api_key = 'JT7wIAf7s9vCQe8ze2Qm' # Generated api key from plotly website profile > settings > regenerate key

valid_username_password_pairs = {
    'admin': 'admin'
}

## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"


## Assessment settings
Zones= {'Zone1':[3,5],
        'Zone2':[-5,3],
        'Zone3':[-15,-5]   
        }

Glare_Weights = np.array([[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                         [0.2, 0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2],
                         [0.2, 0.2, 0.5,   1,   1,   1, 0.5, 0.2],
                         [0.2, 0.2, 0.5,   1,   1,   1, 0.5, 0.2],
                         [0.2, 0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2],
                         ])

# List with performance results
Performance_Levels = ['Standard', 'Good', 'Advanced', 'Excellent', 'Premium', 'Premium+']

# Headlamp assessment reference points for overall scatter plot
# add total assessment into data
db_system_endscores=pd.DataFrame([[4400, 53, 'ADB', '1.3 million pixels + 84 pixels'], [4300, 46, 'ADB', '84 pixels'],
                                [3810, 47, 'ADB', '1.3 million pixels'], [3800, 44, 'ADB', '24 pixels + ZFL'],
                                [4000, 34, 'Automatic', 'BiXENON_1'], [4040, 28, 'Automatic', 'LED_4'],
                                [4000, 24, 'Manually', 'BiXENON_1'], [4040, 17, 'Manually', 'LED_4'],
                                [2900, 38, 'Automatic', 'LED_8'], [2800, 38, 'ADB', 'Swivelling Y + ZFL'],
                                [3200, 37, 'Automatic', 'LED_LASER'], [3800, 44, 'ADB', 'Swivelling Z + ZFL'],
                                [2700, 39, 'ADB', '12 pixels'], [2400, 34, 'ADB', 'Swivelling X'],
                                [2450, 33, 'ADB', '7 pixels'], [2400, 32, 'Automatic', 'LED_6'],
                                [2200, 29, 'Automatic', 'LED_5'], [2500, 26, 'Automatic', 'LED_3'],
                                [2350, 25, 'Automatic', 'XENON_1'], [2500, 24, 'Automatic', 'LED_2'],
                                [2370, 24, 'Manually', 'LED_6'], [2600, 24, 'Automatic', 'H7_3'],
                                [2500, 19, 'Automatic', 'LED_7'], [2280, 19, 'Automatic', 'H7_2'],
                                [2500, 19, 'Manually', 'LED_3'], [2280, 19, 'Manually', 'LED2'],
                                [2400, 15, 'Manually', 'XENON_1'], [2650, 14, 'Manually', 'H7_3'],
                                [2248, 9, 'Manually', 'H7_1'], [2280, 11, 'Manually', 'H7_2'],
                                [2100, 22, 'Manually', 'LED_5'], [1800, 20, 'Automatic', 'LED_1'],
                                [1800, 13, 'Manually', 'LED_1'],
                                ],
                                columns=['Illumination Flux in lm', 'Total Score', 'Type', 'Name'])

# Average score for all assessment points over the three evaluation tests LB, HB, ADB[50m, 100m, 200m]
                                # LB scores
db_system_average=pd.DataFrame([[83.4, 'LB', 'Zone A'], [105, 'LB', 'Zone B'], [40.6, 'LB', 'Zone C'],
                                [8.6, 'LB', 'Zone D Offside'], [12, 'LB', 'Zone D Nearside'], [7.8, 'LB', 'Zone E Offside'],
                                [8.5, 'LB', 'Zone E Nearside'], [0.42, 'LB', 'Glare'], [1266.4, 'LB', 'Flux'],             
                                # HB scores
                                [184.2, 'HB', 'Point A'], [45.1, 'HB', 'Point B'], [47.4, 'HB', 'Point C'],
                                [61.7, 'HB', 'Point D'], [170.9, 'HB', 'Point E'], [8, 'HB', 'Zone E Offside'],
                                [8.4, 'HB', 'Zone E Nearside'], [2120.1, 'HB', 'Flux'],  
                                # ADB scores
                                [184, 'ADB Line 1', 'Zone A\''], [141.6, 'ADB Line 1', 'Zone B'], 
                                [66.4, 'ADB Line 1', 'Zone C\''], [0.1995, 'ADB Line 1', 'Glare'], 
                                [2452.4, 'ADB Line 1', 'Flux'], 

                                [170.3, 'ADB Line 2', 'Zone A\''], [147.5, 'ADB Line 2', 'Zone B'], 
                                [78.4, 'ADB Line 2', 'Zone C\''], [2555.7, 'ADB Line 2', 'Flux'], 

                                [148.5, 'ADB Line 3', 'Zone A\''], [151, 'ADB Line 3', 'Zone B'], 
                                [118.2, 'ADB Line 3', 'Zone C\''], [2615.2, 'ADB Line 3', 'Flux'], 

                                [53.4, 'ADB Line 4', 'Zone A\''], [160.2, 'ADB Line 4', 'Zone B'], 
                                [101.4, 'ADB Line 4', 'Zone C\''], [0.2751, 'ADB Line 4', 'Glare'], 
                                [2418.1, 'ADB Line 4', 'Flux'], 

                                [73, 'ADB Line 5', 'Zone A\''], [156.6, 'ADB Line 5', 'Zone B'], 
                                [133.1, 'ADB Line 5', 'Zone C\''], [2522.2, 'ADB Line 5', 'Flux'], 

                                [102.3, 'ADB Line 6', 'Zone A\''], [153.4, 'ADB Line 6', 'Zone B'], 
                                [157.4, 'ADB Line 6', 'Zone C\''], [2582.1, 'ADB Line 6', 'Flux']
                                ],
                                columns=['Average Score', 'Type', 'Name'])
columns_titles = ['Type', 'Name', 'Average Score']
db_system_average=db_system_average.reindex(columns=columns_titles)