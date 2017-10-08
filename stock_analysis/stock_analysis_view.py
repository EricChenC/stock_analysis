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
            
        index = 0
        for row in range(int(row_count)):
            for column in range(self.column_count):
                stock_item = StockItem(action_name_list[index], 10, "billion")
                
                self.ui.SearchTableWidget.setCellWidget(row,column,stock_item.get_item())
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

