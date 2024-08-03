"""
Creating custom GUI widgets in PySide 6
https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/
"""

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class _Bar(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Courier")
        font.setPointSize(18)
        painter.setFont(font)

        painter.drawText(25, 25, "{}->{}->{}".format(vmin, value, vmax))
        painter.end()

    def _trigger_refresh(self):
        self.update()

class PowerBar(QtWidgets.QWidget):
    """
    Custom QT Widget to show a power bar and dial.
    """

    def __init__(self, step=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        self._bar = _Bar()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        layout.addWidget(self._dial)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)

        self.setLayout(layout)
