"""
Examole for using custom GUI widgets in PySide 6
"""

import sys
from PySide6.QtWidgets import QApplication
from power_bar import PowerBar

app = QApplication(sys.argv)
volume = PowerBar()
volume.show()
sys.exit(app.exec())
