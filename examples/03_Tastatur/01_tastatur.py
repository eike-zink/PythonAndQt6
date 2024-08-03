import sys
import os
from PySide6.QtWidgets import *

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

app = QApplication([])
w = QWidget()
vl = QVBoxLayout(w)

btn = QPushButton()
btn.setText('Start')
vl.addWidget(btn)
tb = QLineEdit()
vl.addWidget(tb)

w.show()
sys.exit(app.exec())