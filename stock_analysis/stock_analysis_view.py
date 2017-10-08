from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QSplitter

from ui_stock_analysis import Ui_MainWindow
from stock_item import StockItem


class StockAnalysisView(QObject):
    search_signal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)    
        self.MainWindow.show()

        self.ui.splitter.setStretchFactor(1, 1)
        self.ui.splitter.setStretchFactor(2, 400)

    def init_ui(self):
        self.column_count = 4

        self.ui.SearchTableWidget.setColumnCount(self.column_count)
        self.ui.SearchTableWidget.resizeColumnsToContents()
        self.ui.SearchTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for column in range(self.column_count):
            self.ui.SearchTableWidget.setColumnWidth(column, 200)
        
        self.ui.SearchPushButton.clicked.connect(self.start_search)
        self.ui.menuParament_List.triggered.connect(self.add_search_items)

    def add_stock_list(self, stock_list):
        self.ui.StockListWidget.clear()
        self.ui.StockListWidget.addItems(stock_list)

    def add_search_items(self):
        self.ui.SearchTableWidget.clear()

        action_name_list = self.get_actions_name_list()
        row_count = len(action_name_list) / self.column_count
        mo_value = len(action_name_list) % self.column_count

        if(int(mo_value) != 0):
            row_count += 1

        self.ui.SearchTableWidget.setRowCount(row_count)
        for row in range(int(row_count)):
            self.ui.SearchTableWidget.setRowHeight(row, 50)
            
        self.name_value_dic = {}

        index = 0
        for row in range(int(row_count)):
            for column in range(self.column_count):
                value = 10.0

                stock_item = StockItem(action_name_list[index], value)
                if(action_name_list[index] == 'totalAssets'):
                    value = 10000.0
                    stock_item = StockItem(action_name_list[index], value, "billion")
                
                stock_item.change_signal.connect(self.search_item_update)

                self.name_value_dic[action_name_list[index]] = str(value)
                self.ui.SearchTableWidget.setCellWidget(row,column,stock_item)
                index += 1

                if(index == len(action_name_list)):
                    return

    def start_search(self):
        self.search_signal.emit()

    def get_actions_name_list(self):
        action_list = self.ui.menuParament_List.actions()

        name_list = []

        for index in range(len(action_list)) :
            if(action_list[index].isChecked()):
                name_list.append(action_list[index].text())

        return name_list

    def set_stock_table_widget_row_column(self, row, column):
        self.ui.StockTableWidget.clear()

        self.ui.StockTableWidget.setRowCount(row)
        self.ui.StockTableWidget.setColumnCount(column)

    def set_column_head_name(self, column, name):
        item = QtWidgets.QTableWidgetItem(name)

        self.ui.StockTableWidget.setHorizontalHeaderItem(column, item)

    def set_column_data_list(self, column, data_list):
        for index in range(len(data_list)):
            item = QtWidgets.QTableWidgetItem(data_list[index])
            self.ui.StockTableWidget.setItem(index, column, item)

    def get_name_value_dic(self):
        return self.name_value_dic

    def search_item_update(self, stock_item):
        name = stock_item.get_item_name()
        value = stock_item.get_item_value()

        self.name_value_dic[name] = str(value)

