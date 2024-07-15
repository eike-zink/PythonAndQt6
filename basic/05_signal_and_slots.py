
# Only needs for access to command line arguments
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        button = QPushButton("Click Me")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_clicked)
        button.clicked.connect(self.button_was_toggled)

        self.setCentralWidget(button)
    
    def button_was_clicked(self):
        print('Click')

    def button_was_toggled(self, checked: bool):
        print('Checked?', checked)


# Create the Application
app = QApplication(sys.argv)

# Create the Widget
window = MainWindow()
window.show()

# Start the event loop
app.exec_()

