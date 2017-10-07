from PyQt5 import QtCore, QtGui, QtWidgets

from stock_analysis_model import StockAnalysisModel
from stock_analysis_view import StockAnalysisView

class StockAnalysisController(object):
    def __init__(self):
        self.model = StockAnalysisModel()
        self.view = StockAnalysisView()

        self.view.init_ui()
        self.view.add_stock_list(self.model.get_stock_list_from_pe(10.0, 10000))
        self.view.add_search_items()

   