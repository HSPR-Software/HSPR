"""GUI for the results of ADB Zone Check. 
einfach wenn es geklappt hat in grün colorcoden und wenn der Wert zu hoch war in Rot 
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class Ui_zone_check(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_zone_check,self).__init__()
        self.setWindowTitle("ADB Block-Out Zone Check")

        self.table = QTableWidget(8,4)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        
        self.table.setHorizontalHeaderLabels(["Measured Intensity left","Max. Intensity left", "Measured Intensity right","Max. Intensity right"])
        self.table.setVerticalHeaderLabels(["50m preceding a)", "50 preceding b)", "50m oncoming", "100m preceding a)", "100m preceding b)", "100m oncoming", "200m preceding", "200m oncoming"])

        self.layout = QVBoxLayout(self)
        self.explanation = QtWidgets.QLabel()
        self.explanation.setText("The test lines a) + b) need to be fulfilled")
        self.explanation.setFont(QtGui.QFont('Arial', 12))
        self.explanation.adjustSize()

        self.layout.addWidget(self.explanation)
        self.table.resizeColumnsToContents()
        self.layout.addWidget(self.table)

    def fill_table_colorcoded(self,maxintensities_left,maxintensities_right,measured_intensity_left,measured_intensity_right):
        for row in range(len(maxintensities_left)):
            max_item = QTableWidgetItem(str(maxintensities_left[row])+" cd")
            measured_item = QTableWidgetItem(str(measured_intensity_left[row])+" cd")
            self.table.setItem(row,0,measured_item)
            self.table.setItem(row,1,max_item)
            if maxintensities_left[row] >= measured_intensity_left[row]: 
                max_item.setBackground(QtGui.QColor(0,255,0))
                measured_item.setBackground(QtGui.QColor(0,255,0))
            else: 
                max_item.setBackground(QtGui.QColor(255,0,0))
                measured_item.setBackground(QtGui.QColor(255,0,0))

            max_item = QTableWidgetItem(str(maxintensities_right[row])+" cd")
            measured_item = QTableWidgetItem(str(measured_intensity_right[row])+" cd")
            if maxintensities_right[row] >= measured_intensity_right[row]: 
                max_item.setBackground(QtGui.QColor(0,255,0))
                measured_item.setBackground(QtGui.QColor(0,255,0))
            else: 
                max_item.setBackground(QtGui.QColor(255,0,0))
                measured_item.setBackground(QtGui.QColor(255,0,0))
            self.table.setItem(row,2,measured_item)
            self.table.setItem(row,3,max_item)



