import sys

from PySide6.QtCore import QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.db = QSqlDatabase('QSQLITE')
        self.db.setDatabaseName('chinook.sqlite')
        self.db.open()

        self.table = QTableView()
        self.model = QSqlTableModel(db=self.db)
        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
