import tushare as ts
import pandas as pd

class StockAnalysisModel(object):
    def __init__(self):
        print('model init')

    def get_stock_list_from_pe(self, pe, total):
        # filter pe return list
        all_stock_list = ts.get_stock_basics()

        all_pe_list = list(all_stock_list['pe'])
        all_name_list = list(all_stock_list['name'])
        all_bvps_list = list(all_stock_list['bvps'])
        all_totalAssets_list = list(all_stock_list['totalAssets'])
       
        self.pe_list = []

        for x in range(len(all_pe_list)):
            if(float(all_pe_list[x]) < pe and float(all_totalAssets_list[x] > (total * 10000))):
               out_str = all_stock_list.index[x] + '  ' + all_name_list[x] + '  ' + str(all_pe_list[x]) + '        ' + str(all_totalAssets_list[x])
               self.pe_list.append(out_str)
               
        return self.pe_list

