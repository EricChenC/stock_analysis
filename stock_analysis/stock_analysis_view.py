from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

from ui_stock_analysis import Ui_MainWindow

class stock_analysis_view(object):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)    
        self.MainWindow.show()

    def init_ui(self):
        self.column_count = 4

        self.ui.SearchTableWidget.setColumnCount(self.column_count)
        self.ui.SearchTableWidget.resizeColumnsToContents()
        self.ui.SearchTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for column in range(self.column_count):
            self.ui.SearchTableWidget.setColumnWidth(column, 200)
        
        self.ui.SearchPushButton.clicked.connect(self.start_search)

    def add_stock_list(self, stock_list):
        self.ui.StockListWidget.addItems(stock_list)

    def add_search_items(self):
        action_name_list = self.get_actions_name_list()
        row_count = len(action_name_list) / self.column_count

        if(row_count < 1):
            row_count = 1

        self.ui.SearchTableWidget.setRowCount(row_count)
            
        index = 0
        for row in range(int(row_count)):
            for column in range(self.column_count):
                item = QtWidgets.QTableWidgetItem()
                item.setText(action_name_list[index])

                self.ui.SearchTableWidget.setItem(row,column,item)
                index += 1

    def start_search(self):
        print('start search')

    def get_actions_name_list(self):
        action_list = self.ui.menuParament_List.actions()

        name_list = []

        for index in range(len(action_list)) :
            if(action_list[index].isChecked()):
                name_list.append(action_list[index].text())

        return name_list

