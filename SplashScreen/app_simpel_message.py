import sys
import time

from PySide6.QtWidgets import QDialog, QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6 import QtGui


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlag(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setEnabled(False)


class MainWindow(QDialog):
    """ Beispielanwendung """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._connection = None

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SplashScreen erstellen und anzeigen
    pixmap = QPixmap("img/splash.png")
    splash = SplashScreen(pixmap)
    # Setze die Schriftart für die Nachricht
    font = QtGui.QFont("Arial", 18, QtGui.QFont.Bold)
    splash.setFont(font)
    splash.show()
    splash.raise_()  # SplashScreen in den Vordergrund bringen
    splash.activateWindow()  # Fokus auf den SplashScreen legen

    # Erstellen des Hauptfensters
    mainWindow = MainWindow()

    # Datenbankverbindung erstellen
    mainWindow.connection = 'datenbank'
    message = 'Datenbankverbindung herstellen...'
    splash.showMessage(message,
                       Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
                       Qt.white)
    time.sleep(2)
    splash.clearMessage()

    # SplashScreen ausschalten
    splash.finish(mainWindow)

    # Anzeige des Hauptfensters
    mainWindow.show()

    sys.exit(app.exec())
