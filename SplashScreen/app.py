import sys, time

from PySide6.QtWidgets import QDialog, QApplication, QSplashScreen, QProgressBar
from PySide6.QtGui import QPixmap, Qt


class MainWindow(QDialog):
    """ Beispielanwendung """
    def __init__(self, parent=None):
        super().__init__(parent)

        # Simulation des Programmstarts
        time.sleep(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SplashScreen erstellen und anzeigen
    splash_pixmap = QPixmap("img/bine.png").scaled(400, 400)
    splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
    splash.setWindowFlag(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)

    # SplashScreen, Progressbar ergaenzen
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(50, splash_pixmap.height() - 50, splash_pixmap.width() - 50, 20)
    splash.showMessage("<h1><font color='green'>Willkommen</font></h1>", Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)


    splash.show()

    mainWindow = MainWindow()
    mainWindow.show()

    # SplashScreen ausschalten
    splash.finish(mainWindow)

    sys.exit(app.exec())