import sys, time

from PySide6.QtWidgets import QDialog, QApplication, QSplashScreen, QProgressBar
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)

        self.setEnabled(False)


class MainWindow(QDialog):
    """ Beispielanwendung """
    def __init__(self, parent=None):
        super().__init__(parent)
        time.sleep(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SplashScreen erstellen und anzeigen
    pixmap = QPixmap("img/splash.png")
    splash = SplashScreen(pixmap)
    splash.show()

    # Erstellen des Hauptfensters
    mainWindow = MainWindow()

    # SplashScreen ausschalten
    splash.finish(mainWindow)

    # Anzeige des Hauptfensters
    mainWindow.show()

    sys.exit(app.exec())