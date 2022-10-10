from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QWidget

class Ui_two_uploads(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.adjustSize()

        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.buttonbox = QtWidgets.QGridLayout()
        self.ok_cancel_layout = QtWidgets.QHBoxLayout()

        self.explanation = QtWidgets.QLabel()
        self.explanation.setText("Just press one of the buttons to open a explorer window for the ies file upload or directly drag a file into the corresponding button")
        self.explanation.setFont(QtGui.QFont('Arial', 12))
        self.explanation.adjustSize()

        self.verticallayout.addWidget(self.explanation)
        self.verticallayout.addLayout(self.buttonbox)

        self.left = DragDropButton(self)
        self.left.setText("LH file upload\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")
        self.left.setFixedSize(250,250)
        self.buttonbox.addWidget(self.left,1,0)

        self.right = DragDropButton(self)
        self.right.setText("RH file upload\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")
        self.right.setFixedSize(250,250)
        self.buttonbox.addWidget(self.right,1,1)

        self.ok_btn = QPushButton()
        self.ok_btn.setText("Confirm")
        self.ok_btn.clicked.connect(lambda: self.filldatapath())
        self.ok_btn.clicked.connect(lambda: self.hide())
        
        self.cancel_btn = QPushButton()
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(lambda: self.oncancel_click())

        self.ok_cancel_layout.addWidget(self.ok_btn)
        self.ok_cancel_layout.addWidget(self.cancel_btn)
        self.verticallayout.addLayout(self.ok_cancel_layout)

        self.datapaths = []

    def filldatapath(self):
        if self.left.datapath != None and self.right.datapath != None:
            self.datapaths = [self.left.datapath, self.right.datapath]

    def oncancel_click(self):
        self.hide()
        #to restore the previous filenames displayed on the buttons
        if len(self.datapaths) == 2:
            self.left.setText(self.datapaths[0].split("/")[-1])
            self.right.setText(self.datapaths[1].split("/")[-1])
        #else: self.restoreinitialButton()

    def restoreinitialButton(self):
        self.left.datapath = None 
        self.right.datapath = None
        self.datapaths = []
        self.left.setText("LH file upload\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")
        self.right.setText("RH file upload\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")


    

class Ui_adb_uploads(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_adb_uploads, self).__init__()
        self.setWindowTitle("ADB single IES upload")
        self.adjustSize()

        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.buttonbox = QtWidgets.QGridLayout()
        self.ok_cancel_layout = QtWidgets.QHBoxLayout()

        self.explanation = QtWidgets.QLabel()
        self.explanation.setText("Just press one of the buttons to open a explorer window for the ies file upload or directly drag a file into the corresponding button")
        self.explanation.setFont(QtGui.QFont('Arial', 12))
        self.explanation.adjustSize()

        self.verticallayout.addWidget(self.explanation)
        self.verticallayout.addLayout(self.buttonbox)
        self.buttons = []
        linecount = 1
        for i in range(1,4):
            for j in range(1,5):
                side = ""
                if(linecount%2):
                    side = "LH"
                else: side = "RH"
                button = DragDropButton(self)
                button.setText("Line"+str(round(linecount/2+0.1))+"_"+side+"\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")
                button.adjustSize()
                self.buttons.append(button)
                self.buttonbox.addWidget(button,i,j)
                linecount +=1

        self.ok_btn = QPushButton()
        self.ok_btn.setText("Confirm")
        self.ok_btn.clicked.connect(lambda: self.filldatapath())
        self.ok_btn.clicked.connect(lambda: self.hide())

        self.cancel_btn = QPushButton()
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(lambda: self.oncancel_click())

        self.ok_cancel_layout.addWidget(self.ok_btn)
        self.ok_cancel_layout.addWidget(self.cancel_btn)
        self.verticallayout.addLayout(self.ok_cancel_layout)

        self.datapaths = []

    def filldatapath(self):
        for i in range(0,len(self.buttons)):
            if self.buttons[i].datapath != None:
                self.datapaths.append(self.buttons[i].datapath)

    def oncancel_click(self):
        self.hide()
        #to restore the previous filenames displayed on the buttons
        if len(self.datapaths) == 12:
            i =0
            for path in self.datapaths:
                if path is not None:
                    self.buttons[i].setText(self.datapaths[0].split("/")[-1])
                    i+=1
        #else: self.restoreinitialButton()


    def restoreinitialButton(self):
        for linecount in range(1,13):
            self.datapaths = []
            side = ""
            if(linecount%2):
                side = "LH"
            else: side = "RH"
            button = self.buttons[linecount-1]
            self.buttons[linecount-1].datapath = None
            button.setText("Line"+str(round(linecount/2+0.1))+"_"+side+"\n\nDrag and Drop an ies File in here \n\n or \n\n click this to open a file explorer")



class DragDropButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        #self.resize(100, 100)
        self.datapath = None

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.datapath = QtWidgets.QFileDialog.getOpenFileName(None, 'Open zip achive', 
                            None,"File (*.ies)")[0]
            if self.datapath != (''): 
                self.setText(self.datapath.split("/")[-1])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            self.datapath = None
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    self.datapath = str(url.toLocalFile())
            self.setText(self.datapath.split("/")[-1])
        else:
            event.ignore()


