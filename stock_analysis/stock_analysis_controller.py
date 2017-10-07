from PyQt5 import QtCore, QtGui, QtWidgets

from stock_analysis_model import stock_analysis_model
from stock_analysis_view import stock_analysis_view

class stock_analysis_controller(object):
    def __init__(self):
        self.model = stock_analysis_model()
        self.view = stock_analysis_view()

        self.view.init_ui()
        self.view.add_stock_list(self.model.get_stock_list_from_pe(10.0))
        self.view.add_search_items()