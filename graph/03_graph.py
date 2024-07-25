"""
Background, Line Colour, Width and Style
"""

from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 33, 22, 38, 32, 27, 38, 32, 44]

        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setTitle('Temperature')
        styles = {'color': 'r', 'font-size': '12px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (h)', **styles)
        self.graphWidget.addLegend()
        self.plot(hour, temperature_1, 'Sensor1', 'r')
        self.plot(hour, temperature_2, 'Sensor2', 'b')

    def plot(self, x, y, name, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=name, pen=pen, symbol='+', symbolSize=5, symbolBrush=color)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
