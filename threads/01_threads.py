import sys
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel('Start')
        button = QPushButton('DANGER')
        button.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(button)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        for _ in range(5):
            QApplication.processEvents()
            time.sleep(1)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
