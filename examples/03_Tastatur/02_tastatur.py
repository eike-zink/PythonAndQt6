import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QLineEdit

CURRENT_DIRECTORY = Path(__file__).resolve().parent

def main():
    os.environ["QML_IMPORT_PATH"] = os.fspath(CURRENT_DIRECTORY / "qml")
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    os.environ["QT_VIRTUALKEYBOARD_STYLE"] = "default"

    app = QApplication(sys.argv)

    w = QLineEdit()
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()