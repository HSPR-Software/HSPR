# Headlamp Systems Performance Rating

## Disclaimer
This is an early version of the HSPR software. The code base is work in progress and a refactoring of the code is coming soon.
All computations are based on [Headlight Safety Performance Rating (HSPR) - Recommended Practice - CE-5815](https://www.gtb-lighting.org/wp-content/uploads/2023/09/2023-09_GTB-Recommended-Practice-for-HSPR.pdf).
For further instructions of how to use the software, see [Software Manual](https://www.gtb-lighting.org/wp-content/uploads/2023/02/HSPR-Software-Manual_V2.1.pdf).

## Starting the program
The easiest way to use the HSPR software is via this [download link](https://hessenbox.tu-darmstadt.de/getlink/fiXiFWZ3WCW7WotyFpnSTYPG/HSPR_V2.1.1.exe) or the Downloadlink file
located in this repository. This leads to an already provided executable program for Windows operating systems.
Alternatively and for other operating systems than Windows please follow the further installation instructions. 

## Installation

- Currently we used and tested the software for Python 3.11.4
- We recommend using an Virtual Python Environment like [miniconda](https://docs.conda.io/en/latest/miniconda.html). To create a new conda environment run the following command in the command line terminal
    ```bash
    conda create -n EnvironmentName python==3.11.4
    conda activate EnvironmentName # activate the environment
    ```
- Please use the provided zip file or clone the repository using the following command in your command line:
    ```bash
        git clone https://github.com/HSPR-Software/HSPR.git
    ```
    - To use the git clone command under windows pleas install the latest [git software](https://git-scm.com/downloads)
- To install the required python packages please run the following command from the main directory of the project (conda environment needs to be activated)
    ```bash
    pip install -r requirements.txt # file is located in the base folder
    ```
- To run the program you can use the following command:
    ```bash
    python src/main.py
    ```

- To create an executable file for your operating system please run the following command inside the directory:
    ```bash
    pyinstaller HSPR.spec
    ```
    The .spec is a predefined build configuration. The file will be located inside the src/dist folder after completion of the process.