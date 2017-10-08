import tushare as ts
import pandas as pd

class StockAnalysisModel(object):
    def __init__(self):
        # filter pe return list
        self.all_stock_list = ts.get_stock_basics()

        self.index_list = []
        self.init_index_list()

    def init_index_list(self):
        self.index_list.clear()

        for x in range(len(self.all_stock_list)):
            self.index_list.append(x)

    def get_filter_list(self):
        return self.index_list

    def get_filter_list_size(self):
        return len(self.index_list)

    def get_pe_list(self):
        self.filter_pe_list = []

        all_pe_list = list(self.all_stock_list['pe'])
        for x in range(len(self.index_list)):
            self.filter_pe_list.append(str(all_pe_list[self.index_list[x]]))

        return self.filter_pe_list

    def get_pb_list(self):
        self.filter_pb_list = []

        all_pb_list = list(self.all_stock_list['pb'])
        for x in range(len(self.index_list)):
            self.filter_pb_list.append(str(all_pb_list[self.index_list[x]]))

        return self.filter_pb_list

    def get_name_list(self):
        self.filter_name_list = []

        all_name_list = list(self.all_stock_list['name'])
        for x in range(len(self.index_list)):
            self.filter_name_list.append(all_name_list[self.index_list[x]])

        return self.filter_name_list

    def get_totals_list(self):
        self.filter_totals_list = []

        all_totals_list = list(self.all_stock_list['totals'])
        for x in range(len(self.index_list)):
            self.filter_totals_list.append(all_totals_list[self.index_list[x]])

        return self.filter_totals_list

    def get_total_assets_list(self):
        self.total_assets_list = []

        all_total_assets_list = list(self.all_stock_list['totalAssets'])
        for x in range(len(self.index_list)):
            self.total_assets_list.append(str(all_total_assets_list[self.index_list[x]]))

        return self.total_assets_list

    def get_timeToMarket_list(self):
        self.timeToMarket_list = []

        all_market_time_list = list(self.all_stock_list['timeToMarket'])
        for x in range(len(self.index_list)):
             self.timeToMarket_list.append(all_market_time_list[self.index_list[x]])

        return self.timeToMarket_list

    def get_code_list(self):
        self.code_list = []

        for x in range(len(self.index_list)):
            self.code_list.append(self.all_stock_list.index[self.index_list[x]])

        return self.code_list


    def filter_pe(self, pe):
        new_index_list = []

        all_pe_list = list(self.all_stock_list['pe'])
        for x in range(len(self.index_list)):
            if(float(all_pe_list[self.index_list[x]]) < float(pe)):
                new_index_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = new_index_list


    def filter_pb(self, pb):
        new_index_list = []

        all_pb_list = list(self.all_stock_list['pb'])
        for x in range(len(self.index_list)):
            if(float(all_pb_list[self.index_list[x]]) < float(pb)):
                new_index_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = new_index_list

    def fliter_name(self, name):
        new_index_list = []

        all_name_list = list(self.all_stock_list['name'])
        for x in range(len(self.index_list)):
            if(all_name_list[self.index_list[x]] == name):
                new_index_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = new_index_list


    def filter_totals(self, totals):
        new_index_list = []

        all_totals_list = list(self.all_stock_list['totals'])
        for x in range(len(self.index_list)):
            if(all_totals_list[self.index_list[x]] > float(totals)):
                new_index_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = new_index_list

    
    def filter_total_assets(self, total_assets):
        new_index_list = []

        all_total_assets_list = list(self.all_stock_list['totalAssets'])
        for x in range(len(self.index_list)):
            if(all_total_assets_list[self.index_list[x]] > float(total_assets) * 10000):
                new_index_list.append(self.index_list[x])


        self.index_list.clear()
        self.index_list = new_index_list


    def filter_timeToMarket(self, market_time):
        new_index_list = []

        #need fixed
        all_market_time_list = list(self.all_stock_list['timeToMarket'])
        for x in range(len(self.index_list)):
            if(all_market_time_list[self.index_list[x]] < market_time):
                new_index_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = new_index_list


    def filter_stock_code(self, code):
        stock_code_list = []

        for x in range(len(self.index_list)):
            if(self.all_stock_list.index[self.index_list[x]] == code):
                stock_code_list.append(self.index_list[x])

        self.index_list.clear()
        self.index_list = stock_code_list