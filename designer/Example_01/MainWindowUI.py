# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 233)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.leDateinamen = QLineEdit(self.frame)
        self.leDateinamen.setObjectName(u"leDateinamen")
        self.leDateinamen.setEnabled(False)
        self.leDateinamen.setReadOnly(False)

        self.gridLayout.addWidget(self.leDateinamen, 2, 1, 1, 1)

        self.lDateinamen = QLabel(self.frame)
        self.lDateinamen.setObjectName(u"lDateinamen")

        self.gridLayout.addWidget(self.lDateinamen, 2, 0, 1, 1)

        self.leBetrieb = QLineEdit(self.frame)
        self.leBetrieb.setObjectName(u"leBetrieb")

        self.gridLayout.addWidget(self.leBetrieb, 0, 1, 1, 1)

        self.lBetrieb = QLabel(self.frame)
        self.lBetrieb.setObjectName(u"lBetrieb")

        self.gridLayout.addWidget(self.lBetrieb, 0, 0, 1, 1)

        self.cbInEinrichtung = QCheckBox(self.frame)
        self.cbInEinrichtung.setObjectName(u"cbInEinrichtung")

        self.gridLayout.addWidget(self.cbInEinrichtung, 0, 2, 1, 1)

        self.pbOpenFileDialog = QPushButton(self.frame)
        self.pbOpenFileDialog.setObjectName(u"pbOpenFileDialog")

        self.gridLayout.addWidget(self.pbOpenFileDialog, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)

        self.verticalLayout.addWidget(self.progress)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 373, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.leBetrieb, self.cbInEinrichtung)
        QWidget.setTabOrder(self.cbInEinrichtung, self.pbOpenFileDialog)
        QWidget.setTabOrder(self.pbOpenFileDialog, self.leDateinamen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.leDateinamen.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dateinamen", None))
        self.lDateinamen.setText(QCoreApplication.translate("MainWindow", u"Datei", None))
#if QT_CONFIG(statustip)
        self.leBetrieb.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.leBetrieb.setText("")
        self.leBetrieb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Betriebsnummer", None))
        self.lBetrieb.setText(QCoreApplication.translate("MainWindow", u"Betrieb", None))
#if QT_CONFIG(statustip)
        self.cbInEinrichtung.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.cbInEinrichtung.setText(QCoreApplication.translate("MainWindow", u"in Einrichtung", None))
        self.pbOpenFileDialog.setText(QCoreApplication.translate("MainWindow", u"&Datei \u00f6ffnen", None))
    # retranslateUi

