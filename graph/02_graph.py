"""
Background, Line Colour, Width and Style
"""

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
import pyqtgraph as pg
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setTitle('Temperature')
        styles = {'color': 'r', 'font-size': '12px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (h)', **styles)
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.DashLine)
        self.graphWidget.plot(hour, temperature, pen=pen, symbol='+')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
