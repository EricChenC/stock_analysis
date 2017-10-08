from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject

from stock_analysis_model import StockAnalysisModel
from stock_analysis_view import StockAnalysisView

class StockAnalysisController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.model = StockAnalysisModel()
        self.view = StockAnalysisView()

        self.view.init_ui()
        
        self.view.add_search_items()
        self.view.search_signal.connect(self.refresh_stock_list)

    def refresh_stock_list(self):
        self.view.add_stock_list(self.model.get_stock_list_from_pe(10.0, 10000))
   
