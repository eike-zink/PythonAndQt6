import sys, time

from PySide6.QtWidgets import QDialog, QApplication, QSplashScreen, QProgressBar
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt, QTimer


class AnimatedSplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)  # 50 ms für eine schnelle Animation
        
    def animate(self):
        self.counter += 1
        self.repaint()  # Neu zeichnen

    def drawContents(self, painter):
        super().drawContents(painter)
        # Zeichne eine einfache Animation (z.B. einen sich bewegenden Kreis)
        radius = 20
        x_pos = (self.counter * 5) % self.width()  # Bewegt den Kreis nach rechts
        y_pos = self.height() // 2
        
        painter.setBrush(QColor(255, 215, 0))  # Goldgelber Kreis
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(x_pos, y_pos, radius, radius)


class MainWindow(QDialog):
    """ Beispielanwendung """
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # SplashScreen erstellen und anzeigen
    pixmap = QPixmap(500, 300) # Alternative QPixmap("img/splash.png")
    splash = AnimatedSplashScreen(pixmap)
    splash.show()

    # Erstellen des Hauptfensters
    mainWindow = MainWindow()

    # Beende den SplashScreen und zeige das Hauptfenster nach einer kurzen Verzögerung
    QTimer.singleShot(3000, splash.finish)  # SplashScreen nach 3 Sekunden schließen
    QTimer.singleShot(3100, mainWindow.show)  # Hauptfenster nach 3.1 Sekunden anzeigen

    sys.exit(app.exec())