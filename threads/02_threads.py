"""
Beispiele für QRunnable und QThreadPool
siehe dazu  https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
"""

from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout

import sys
import time


class Worker(QRunnable):
    """
    Worker thread
    :param fn:  Callback function to run on this worker thread. 
                Supplied args und kwargs will be passed through
                to the runner.
    :param args:  Arguments to make availabe to the run code
    :param kwargs: Keywords arguments to make available to the run code
    """
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()             #QtSlote
    def run(self):
        """
        Yout code goes in this function
        """
        self.fn(*self.args, **self.kwargs)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        layout = QVBoxLayout()

        self.label = QLabel('Start')
        button = QPushButton('DANGER')
        button.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def execute_this(self):
        print('Function start')
        time.sleep(5)
        print('Function complete')

    def oh_no(self):
        worker = Worker(self.execute_this)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter {self.counter}')


app = QApplication(sys.argv)
window = MainWindow()
app.exec()