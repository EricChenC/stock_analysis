from PyQt5 import QtCore, QtGui, QtWidgets

from stock_analysis_controller import stock_analysis_controller


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    controller = stock_analysis_controller()
    
    sys.exit(app.exec_())


    
