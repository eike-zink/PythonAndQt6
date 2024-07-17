import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_time_clicked = 0
        self.setWindowTitle('My App')
        self.setFixedSize(QSize(400, 300))

        self.windowTitleChanged.connect(self.window_title_changed)

        self.button = QPushButton('Click Me')
        self.button.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        print('Clicked')
        new_window_title = choice(window_titles)
        print(f'Setting title: {new_window_title}')
        self.setWindowTitle(new_window_title)

    def window_title_changed(self, window_title):
        print(f'Window title changed: {window_title}')
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
