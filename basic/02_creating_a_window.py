
# Only needs for access to command line arguments
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Create the Application
app = QApplication(sys.argv)

# Create the Widget
window = QMainWindow()
window.show()

# Start the event loop
app.exec_()

