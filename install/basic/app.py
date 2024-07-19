import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My first App')
        button = QPushButton('Close me')
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
