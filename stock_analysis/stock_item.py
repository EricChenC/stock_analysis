from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

class StockItem(QWidget):
    change_signal = pyqtSignal(QWidget)

    def __init__(self, name, value, size_str = ''):
        QWidget.__init__(self)
        self.name_label = QLabel(name)
        self.value_lineEdit = QLineEdit()
        self.size_label = QLabel(size_str)

        self.value_lineEdit.setText(str(value))

        item_horizon_layout = QtWidgets.QHBoxLayout()
        item_horizon_layout.addWidget(self.name_label, 1)
        item_horizon_layout.addWidget(self.value_lineEdit, 4)
        item_horizon_layout.addWidget(self.size_label, 2)

        self.setLayout(item_horizon_layout)

        self.value_lineEdit.textChanged.connect(self.content_update)

    def get_item_name(self):
        return self.name_label.text()

    def set_item_name(self, name):
        self.name_label.setText(name)

    def get_item_value(self):
        return self.value_lineEdit.text()

    def set_item_value(self, value):
        self.value_lineEdit.setText(str(value))

    def content_update(self):
        self.change_signal.emit(self)

