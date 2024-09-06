import sys
import os 
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QColorDialog
from PySide6.QtGui import QIcon, QAction


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    clipboard = QApplication.clipboard()

    # Funktion, um eine Benachrichtigung anzuzeigen
    def show_notification(title, message):
        tray.showMessage(title, message)

    # Funktionen zur Farbauswahl
    def copy_hex_value():
        color_dialog = QColorDialog()
        if color_dialog.exec():
            color = color_dialog.selectedColor()
            clipboard.setText(color.name())
            show_notification("Farbe ausgewählt", f"Hex-Wert: {color.name()}")

    def copy_rgb_value():
        color_dialog = QColorDialog()
        if color_dialog.exec():
            color = color_dialog.selectedColor()
            clipboard.setText('rgb(%d, %d, %d)' % (
                color.red(), color.green(), color.blue()
            ))
            show_notification("Farbe ausgewählt", f"RGB-Wert: {color.red()}, {color.green()}, {color.blue()}")

    def copy_hsv_value():
        color_dialog = QColorDialog()
        if color_dialog.exec():
            color = color_dialog.selectedColor()
            clipboard.setText('hsv(%d, %d, %d)' % (
                color.hue(), color.saturation(), color.value()
            ))
            show_notification("Farbe ausgewählt", f"HSV-Wert: {color.hue()}, {color.saturation()}, {color.value()}")


    # Lade das Icon mit vollständigem Pfad
    icon_path = os.path.abspath('img/app.png')
    print(icon_path)
    icon = QIcon(icon_path)

    # Überprüfen, ob das Icon korrekt geladen wurde
    if icon.isNull():
        print("Das Icon konnte nicht geladen werden.")
        sys.exit(1)

    # Erstelle ein SystemTrayIcon
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Erstelle ein Kontextmenü für das Tray-Icon
    menu = QMenu()

    # Aktionen zur Farbauswahl
    copy_hex_action = QAction('Hex')
    copy_hex_action.triggered.connect(copy_hex_value)
    menu.addAction(copy_hex_action)

    copy_rgb_action = QAction('RGB')
    copy_rgb_action.triggered.connect(copy_rgb_value)
    menu.addAction(copy_rgb_action)

    copy_hsv_action = QAction('HSV')
    copy_hsv_action.triggered.connect(copy_hsv_value)
    menu.addAction(copy_hsv_action)

    # Aktion zum Beenden der Anwendung
    exit_action = QAction("Beenden")
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)

    tray.setContextMenu(menu)

    # Zeige das Tray-Icon an
    #tray.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()