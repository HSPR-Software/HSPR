from PyQt5.QtCore  import Qt
from PyQt5.QtWidgets  import *
from PyQt5.QtGui  import QMovie

class LoadingCircle(QWidget):
    """Class to display loading gif during computation
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie("C:\\Users\\Nutzer\\Desktop\\project_hrsp\\settings\\assets\\ajax-loader.gif")
        self.label_animation.setMovie(self.movie)
    
    def start_animation(self):
        self.movie.start()

    def stop_animation(self):
        self.movie.stop()
        self.close()