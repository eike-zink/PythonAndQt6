"""
https://stackoverflow.com/questions/74357189/pyqt5-painting-on-top-of-a-button-while-keeping-the-button-active
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

class DrawRangeButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super(DrawRangeButton, self).__init__(text)
        self.color = Qt.blue
        self.text = text

    def changeColor(self):
        self.color = Qt.red
        self.update()

    def paintEvent(self, event):
        r = event.rect()
        p = QtGui.QPainter(self)
        p.fillRect(0, 0, int(r.width()/2), int(r.height()), self.color)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = QtWidgets.QWidget() 
        self.layout = QtWidgets.QGridLayout(self.mainWidget)
                
        self.button = DrawRangeButton("TEST")
        self.button.clicked.connect(self.button.changeColor)
        self.layout.addWidget(self.button)

        self.setCentralWidget(self.mainWidget)

app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()
