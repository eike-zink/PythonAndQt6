import sys, time

from PySide6.QtWidgets import QDialog, QApplication, QSplashScreen, QProgressBar
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, pixmap.height() - 50, pixmap.width() - 100, 30)
        self.progress_bar.setRange(0, 10)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setEnabled(False)
    
    def update_progress(self, value):
        self.progress_bar.setValue(value)


class MainWindow(QDialog):
    """ Beispielanwendung """
    def __init__(self, parent=None):
        super().__init__(parent)


    def initialize(self, splash):
        # Simulation des Programmstarts (10 Aufgaben)
        for i in range(11):
            QTimer.singleShot(i * 30, lambda value = i: splash.update_progress(value))
            # Eventloop (notwendig zur Anzeige des Fortschritts)
            QTimer.singleShot(i * 30, lambda: app.processEvents())
        QTimer.singleShot(3100, lambda: splash.finish(self)) # Verwende finish, um den SplashScreen zu schließen
        QTimer.singleShot(3200, self.show) # Anzeige des MainWindows (SplashScreen wird automatisch geschlossen)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SplashScreen erstellen und anzeigen
    pixmap = QPixmap("img/splash.png")
    splash = SplashScreen(pixmap)
    splash.show()

    # Erstellen des Hauptfensters
    mainWindow = MainWindow()

    # Start des Initialisierungsprozess, 
    # im Anschluss wird das Hauptfenster
    # automatisch angezeigt
    mainWindow.initialize(splash)

    # SplashScreen ausschalten
    splash.finish(mainWindow)

    sys.exit(app.exec())