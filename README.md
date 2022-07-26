# Headlamp Systems Performance Rating

## Disclaimer
This is an early Version of the HSPR Software. The Code base is work in progress and a refactoring of the code is coming soon.
All computations are based on Headlight Safety Performance Rating (HSPR) - Recommended Practice - CE-5815.


## Installation

- Currently we used and tested the Software for Python 3.8.3
- We recommend using an Virtual Python Enviroment like [miniconda](https://docs.conda.io/en/latest/miniconda.html). To create a new conda enviroment run the following command in the command line
    ```bash
    conda create -n EnviromentName python==3.8.3
    conda activate EnviromentName # avtivate the enviroment
    ```
- Please use the provided zip file or clone the code using the folowing command in your command line:
    ```bash
        git clone https://github.com/HSPR-Software/HSPR.git
    ```
    - To use the git clone command under windows pleas install the latest [git software](https://git-scm.com/downloads)
- To install the required python packages please run the following command from the main direcotry of the project (conda enviroment needs to be activated)
    ```bash
    pip install -r requiremnts.txt # file is located in the base folder
    ```
- To run the program you can use the following command:
    ```bash
    python src/main.py
    ```

- To create an .exe file please run the following comand inside the src directory:
    ```bash
    pyinstaller --clean --onefile main.py
    ```
    The .exe file will be located inside the src/dist folder after completion of the process