import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QTableView, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        data = [
            [4, 9, 2],
            [1, 'hello', 0],
            [3, 5, 0],
            [3, 3, 'hello'],
            ['hello', 8, 9],
        ]

        self.model = TableModel(data)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterKeyColumn(-1) # Search in all columns
        self.proxy_model.sort(0, Qt.AscendingOrder)

        self.table = QTableView()
        self.table.setModel(self.proxy_model)

        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.proxy_model.setFilterFixedString)

        layout = QVBoxLayout()
        layout.addWidget(self.searchbar)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


