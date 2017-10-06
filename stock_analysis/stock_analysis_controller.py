from PyQt5 import QtCore, QtGui, QtWidgets

from ui_stock_analysis import Ui_MainWindow
from stock_analysis_model import StockAnalysisModel

class stock_analysis_controller(object):
    def __init__(self):
        print('controller init')

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)    
        self.MainWindow.show()

        model = StockAnalysisModel()
        pe_list = model.get_stock_list_from_pe(10.0)

        self.ui.listWidget.addItems(pe_list)