from PyQt5 import QtCore, QtGui, QtWidgets

from ui_stock_analysis import Ui_MainWindow
from stock_analysis_model import Stock_Analysis_Model

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)    
    MainWindow.show()

    mdoel = Stock_Analysis_Model()

    sys.exit(app.exec_())


    
