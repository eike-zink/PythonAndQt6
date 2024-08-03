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
        dial = self.parent().dial
        vmin, vmax, value = dial.minimum(), dial.maximum(), dial.value()

        # Define our canvas
        padding = 5
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)

        # Draw the bars
        step_size = int(d_height / 5)
        bar_height = int(step_size * 0.6)
        bar_spacer = int(step_size * 0.4 / 2)

        pc = (value - vmin) / (vmax - vmin)
        steps_to_draw = int(pc * 5)
        brush.setColor(QtGui.QColor("red"))
        for n in range(steps_to_draw):
            rect = QtCore.QRect(
                padding,
                int(padding + d_height - ((n + 1) * step_size) + bar_spacer),
                d_width,
                bar_height
            )
            painter.fillRect(rect, brush)
        painter.end()

    def trigger_refresh(self):
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

        self.dial = QtWidgets.QDial()
        layout.addWidget(self.dial)
        self.dial.valueChanged.connect(self._bar.trigger_refresh)

        self.setLayout(layout)
