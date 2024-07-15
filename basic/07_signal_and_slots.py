
# Only needs for access to command line arguments
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        self.button_is_checked = True

        self.button = QPushButton("Click Me")
        self.button.setCheckable(True)
        self.button.released.connect(self.button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print('Checked?', self.button_is_checked)


# Create the Application
app = QApplication(sys.argv)

# Create the Widget
window = MainWindow()
window.show()

# Start the event loop
app.exec_()

