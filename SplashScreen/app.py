from PySide6.QtWidgets import QApplication, QSplashScreen, QMainWindow, QProgressBar, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
import sys


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)

        # Setze das Layout für den SplashScreen
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(0,
                                      pixmap.height() - 50,
                                      pixmap.width(),
                                      20)
        # Positioniere die ProgressBar am unteren Rand
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def update_progress(self, value):
        self.progress_bar.setValue(value)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")
        self.setGeometry(300, 300, 800, 600)

        # Setze ein einfaches Layout für das Hauptfenster
        layout = QVBoxLayout()
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def simulate_long_task(self, splash):
        for i in range(101):
            QTimer.singleShot(i * 30, lambda val=i: splash.update_progress(val))
            QTimer.singleShot(i * 30, lambda: app.processEvents())  # Verarbeite Events, um den Fortschritt anzuzeigen
        QTimer.singleShot(3100, splash.close)  # Schließe den SplashScreen nach Abschluss
        QTimer.singleShot(3200, self.show)  # Zeige das Hauptfenster nach Abschluss


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Lade das Bild und erstelle den SplashScreen
    pixmap = QPixmap("img/bine.")
    splash = SplashScreen(pixmap)
    splash.show()

    # Erstelle das Hauptfenster
    main_window = MainWindow()

    # Simuliere einen langen Ladevorgang und steuere den Fortschritt
    main_window.simulate_long_task(splash)

    sys.exit(app.exec())
