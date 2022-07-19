from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class Canvas(FigureCanvasQTAgg):
    """Class to create a canvas model to display matplotlib on Pyqt GUI
    """
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # fig = plt.figure()
        self.axes = fig.add_subplot(111)
        self.axes.remove()
        super(Canvas, self).__init__(fig)
    
    def clear(self):
        self.figure.clear(True)
    