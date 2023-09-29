import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout, QPushButton,QApplication, QLabel
from PyQt5.QtCore import Qt



class ProgressWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(Qt.Tool) #hides window from taskbar

        layout = QVBoxLayout()

        self.label = QLabel("Please wait until the computation is completed.")
        self.label.setStyleSheet('font-size: 24px; height: 24px;')
        layout.addWidget(self.label)

        self.label2 = QLabel()
        self.label2.setStyleSheet('font-size: 12px; height: 12px;')
        layout.addWidget(self.label2)

        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)


    def increasebar_by(self, value):
        self.progressBar.setValue(self.progressBar.value()+value)
        if self.progressBar.value() >= self.progressBar.maximum(): self.close()

    def updatetext(self, text):
        self.label2.setText(self.label2.text() + '\n' + text)
        
    def closeself(self):
        self.close()
        

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    MainWindow = ProgressWindow()
#    MainWindow.show()
 #   sys.exit(app.exec_())