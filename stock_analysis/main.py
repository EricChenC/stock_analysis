from PyQt5 import QtCore, QtGui, QtWidgets

from stock_analysis_controller import StockAnalysisController


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    controller = StockAnalysisController()
    
    sys.exit(app.exec_())


    
