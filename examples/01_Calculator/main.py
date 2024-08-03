"""
Simpel calculator built with Python and PySide
"""

import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)
from functools import partial

ERROR_MSG = 'ERROR'
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = QSize(40, 40)


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Create the Display"""
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        """Create all Buttons"""
        self.buttons = {}
        button_layout = QGridLayout()
        key_boards = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '00', '.', '+', '=']
        ]
        for row, keys in enumerate(key_boards):
            for col, key in enumerate(keys):
                self.buttons[key] = QPushButton(key)
                self.buttons[key].setFixedSize(BUTTON_SIZE)
                button_layout.addWidget(self.buttons[key], row, col)
        self.general_layout.addLayout(button_layout)

    def set_display_text(self, text):
        """Set the display text"""
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        """Get the display text"""
        return self.display.text()

    def clear_display(self):
        """Clear the display"""
        self.set_display_text('')


class Model:
    @staticmethod
    def evaluate(expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
        return result


class Controller:
    """Calculator controller class"""
    def __init__(self, model, view: View):
        self._model = model
        self._view = view
        self._connect_signal_and_slots()
        self._view.show()

    def _connect_signal_and_slots(self):
        for key, button in self._view.buttons.items():
            if key not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._build_expression, key)
                )
        self._view.buttons['='].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)
        self._view.buttons['C'].clicked.connect(self._view.clear_display)

    def _build_expression(self, sub_expression):
        if self._view.display_text() == ERROR_MSG:
            self._view.clear_display()
        expression = self._view.display_text() + sub_expression
        self._view.set_display_text(expression)

    def _calculate_result(self):
        result = self._model.evaluate(self._view.display_text())
        self._view.set_display_text(result)


def main():
    app = QApplication()
    Controller(Model(), View())
    sys.exit((app.exec()))


if __name__ == "__main__":
    main()
