"""
Creating custom GUI widgets in PySide 6
https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/
"""

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class _Bar(QtWidgets.QWidget):

    clickedValue = QtCore.Signal(int)

    def __init__(self, steps, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

        if isinstance(steps, list):
            # list of colors
            self.n_steps = len(steps)
            self.steps = steps
        elif isinstance(steps, int):
            # number of bars, defaults to red
            self.n_steps = steps
            self.steps = ["red"] * self.n_steps
        else:
            raise TypeError('steps must be a list or an integer')

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor("black")
        self._padding = 0.4

    def _calculate_clicked_value(self, event):
        parent = self.parent()
        v_min, v_max = parent.minimum(), parent.maximum()
        d_height = self.size().height() + (self._padding * 2)
        step_size = d_height / self.n_steps
        click_y = event.y() - self._padding + step_size / 2

        pc = (d_height - click_y) / d_height
        value = int(v_min + pc * (v_max - v_min))
        print(value)
        self.clickedValue.emit(value)

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state
        dial = self.parent()._dial
        d_min, d_max, value = dial.minimum(), dial.maximum(), dial.value()

        # Define our canvas
        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        # Draw the bars
        step_size = int(d_height / self.n_steps)
        bar_height = int(step_size * self._bar_solid_percent)
        bar_spacer = int(step_size * (1 - self._bar_solid_percent) / 2)

        # Calculate the y-stop position, from the value range
        pc = (value - d_min) / (d_max - d_min)
        steps_to_draw = int(pc * self.n_steps)

        for n in range(steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            rect = QtCore.QRect(
                int(self._padding),
                int(self._padding + d_height - ((1 + n) * step_size) + bar_spacer),
                int(d_width),
                bar_height
            )
            painter.fillRect(rect, brush)
        painter.end()

    def trigger_refresh(self):
        self.update()

    def mouseMoveEvent(self, event):
        self._calculate_clicked_value(event)

    def mousePressEvent(self, event):
        self._calculate_clicked_value(event)


class PowerBar(QtWidgets.QWidget):
    """
    Custom QT Widget to show a power bar and dial.
    """

    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)

        self._bar = _Bar(steps)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._bar)

        self._dial = QtWidgets.QDial()
        self._dial.setNotchesVisible(True)
        self._dial.setWrapping(False)
        self._dial.valueChanged.connect(self._bar.trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)
        # Take feedback from click events on the meter
        self._bar.clickedValue.connect(self._dial.setValue)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self[attr]
        return getattr(self._dial, attr)

    def setColor(self, color):
        self._bar.steps = [color] * self._bar.n_steps
        self._bar.update()

    def setColors(self, colors):
        self._bar.n_steps = len(colors)
        self._bar.steps = colors
        self._bar.update()

    def setBarPadding(self, padding: int):
        self._bar._padding = padding
        self._bar.update()

    def setBarSolidPercent(self, percent: float):
        self._bar._bar_solid_percent = percent
        self._bar.update()

    def setBackgroundColor(self, color):
        self._bar._background_color = QtGui.QColor(color)
        self._bar.update()

