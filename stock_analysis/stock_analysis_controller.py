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
        self.model.init_index_list()

        action_name_list = self.view.get_actions_name_list()

        name_value_dic = self.view.get_name_value_dic()
        for index in range(len(action_name_list)):
            if(action_name_list[index] == 'pe'):
                self.model.filter_pe(name_value_dic['pe'])

            if(action_name_list[index] == 'pb'):
                self.model.filter_pb(name_value_dic['pb'])

            #if(action_name_list[index] == 'name'):
            #    self.model.fliter_name(name_value_dic['name'])

            if(action_name_list[index] == 'totals'):
                self.model.filter_totals(name_value_dic['totals'])

            if(action_name_list[index] == 'totalAssets'):
                self.model.filter_total_assets(name_value_dic['totalAssets'])

            if(action_name_list[index] == 'timeToMarket'):
                self.model.filter_timeToMarket(name_value_dic['timeToMarket'])

            #if(action_name_list[index] == 'code'):
            #    self.model.filter_stock_code(name_value_dic['code'])


        row_size = self.model.get_filter_list_size()
        column_size = len(action_name_list)

        self.view.set_stock_table_widget_row_column(row_size, column_size)

        for index in range(len(action_name_list)):
            self.view.set_column_head_name(index, action_name_list[index])

            if(action_name_list[index] == 'pe'):
                self.view.set_column_data_list(index,self.model.get_pe_list())

            if(action_name_list[index] == 'pb'):
                self.view.set_column_data_list(index,self.model.get_pb_list())

            if(action_name_list[index] == 'name'):
                self.view.set_column_data_list(index,self.model.get_name_list())

            if(action_name_list[index] == 'totals'):
                self.view.set_column_data_list(index,self.model.get_totals_list())

            if(action_name_list[index] == 'totalAssets'):
                self.view.set_column_data_list(index,self.model.get_total_assets_list())

            if(action_name_list[index] == 'timeToMarket'):
                self.view.set_column_data_list(index,self.model.get_timeToMarket_list())

            if(action_name_list[index] == 'code'):
                self.view.set_column_data_list(index,self.model.get_code_list())
   
    