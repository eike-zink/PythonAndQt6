"""
Beispiele für QRunnable und QThreadPool
siehe dazu  https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
"""

from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool, QObject, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout

import sys
import time
import traceback


class WorkerSignals(QObject):
    """
    Defines the signals available from a runnig worker thread
    Supported signals are:
    finished 
        no data
    error
        tuple (exctype, value, traceback.format_exc())
    result
        object fata returned from the function
    progress
        int indication % progress
    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


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
        self.signals = WorkerSignals()
        # Add the callback to kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()             #QtSlote
    def run(self):
        """
        Yout code goes in this function
        """
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


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

    def execute_this(self, progress_callback):
        print('Function start')
        for n in range(5):
            time.sleep(1)
            progress_callback.emit(n*100/4)
        print('Function complete')

    def worker_progress(self, n):
        print(f'{n}% done')

    def worker_result(self, s):
        print(s)

    def worker_completed(self):
        print('Thread complete')

    def oh_no(self):
        worker = Worker(self.execute_this)
        worker.signals.result.connect(self.worker_result)
        worker.signals.finished.connect(self.worker_completed)
        worker.signals.progress.connect(self.worker_progress)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter {self.counter}')


app = QApplication(sys.argv)
window = MainWindow()
app.exec()