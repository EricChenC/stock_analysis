from PyQt5 import QtCore, QtGui, QtWidgets

class StockItem(object):
    def __init__(self, name, value, size_str):
        self.item_widget = QtWidgets.QWidget()

        self.name_label = QtWidgets.QLabel(name)
        self.value_combobox = QtWidgets.QComboBox()
        self.size_label = QtWidgets.QLabel(size_str)

        self.value_combobox.setEditable(True)
        self.value_combobox.addItem(str(value))

        item_horizon_layout = QtWidgets.QHBoxLayout()
        item_horizon_layout.addWidget(self.name_label, 1)
        item_horizon_layout.addWidget(self.value_combobox, 4)
        item_horizon_layout.addWidget(self.size_label, 2)

        self.item_widget.setLayout(item_horizon_layout)

    def get_item(self):
        return self.item_widget

    def get_item_name(self):
        return self.name_label.text()

    def set_item_name(self, name):
        self.name_label.setText(name)

    def get_item_value(self):
        return int(self.value_combobox.currentText())

    def set_item_value(self, value):
        self.value_combobox.addItem(str(value))
        self.value_combobox.setCurrentText(str(value))

