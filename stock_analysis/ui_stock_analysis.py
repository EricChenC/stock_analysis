# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SearchTableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.SearchTableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.SearchTableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SearchTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.SearchTableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.SearchTableWidget.setObjectName("SearchTableWidget")
        self.SearchTableWidget.setColumnCount(0)
        self.SearchTableWidget.setRowCount(0)
        self.SearchTableWidget.horizontalHeader().setVisible(False)
        self.SearchTableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.SearchTableWidget)
        self.SearchPushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchPushButton.sizePolicy().hasHeightForWidth())
        self.SearchPushButton.setSizePolicy(sizePolicy)
        self.SearchPushButton.setObjectName("SearchPushButton")
        self.horizontalLayout.addWidget(self.SearchPushButton)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FilterLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.FilterLineEdit.setObjectName("FilterLineEdit")
        self.verticalLayout.addWidget(self.FilterLineEdit)
        self.StockTableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.StockTableWidget.setObjectName("StockTableWidget")
        self.StockTableWidget.setColumnCount(0)
        self.StockTableWidget.setRowCount(0)
        self.StockTableWidget.horizontalHeader().setVisible(True)
        self.StockTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.StockTableWidget)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.menubar.setObjectName("menubar")
        self.menuParament_List = QtWidgets.QMenu(self.menubar)
        self.menuParament_List.setObjectName("menuParament_List")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPE = QtWidgets.QAction(MainWindow)
        self.actionPE.setCheckable(True)
        self.actionPE.setChecked(True)
        self.actionPE.setObjectName("actionPE")
        self.actionPB = QtWidgets.QAction(MainWindow)
        self.actionPB.setCheckable(True)
        self.actionPB.setChecked(True)
        self.actionPB.setObjectName("actionPB")
        self.actionTime = QtWidgets.QAction(MainWindow)
        self.actionTime.setCheckable(True)
        self.actionTime.setChecked(True)
        self.actionTime.setObjectName("actionTime")
        self.actiontotal = QtWidgets.QAction(MainWindow)
        self.actiontotal.setCheckable(True)
        self.actiontotal.setChecked(False)
        self.actiontotal.setObjectName("actiontotal")
        self.actionPrice = QtWidgets.QAction(MainWindow)
        self.actionPrice.setCheckable(True)
        self.actionPrice.setObjectName("actionPrice")
        self.actionindustry = QtWidgets.QAction(MainWindow)
        self.actionindustry.setCheckable(True)
        self.actionindustry.setObjectName("actionindustry")
        self.actionarea = QtWidgets.QAction(MainWindow)
        self.actionarea.setCheckable(True)
        self.actionarea.setObjectName("actionarea")
        self.actionoutstanding = QtWidgets.QAction(MainWindow)
        self.actionoutstanding.setCheckable(True)
        self.actionoutstanding.setObjectName("actionoutstanding")
        self.actiontotalAssets = QtWidgets.QAction(MainWindow)
        self.actiontotalAssets.setCheckable(True)
        self.actiontotalAssets.setChecked(True)
        self.actiontotalAssets.setObjectName("actiontotalAssets")
        self.actionliquidAssets = QtWidgets.QAction(MainWindow)
        self.actionliquidAssets.setCheckable(True)
        self.actionliquidAssets.setObjectName("actionliquidAssets")
        self.actionfixedAssets = QtWidgets.QAction(MainWindow)
        self.actionfixedAssets.setCheckable(True)
        self.actionfixedAssets.setObjectName("actionfixedAssets")
        self.actionreserved = QtWidgets.QAction(MainWindow)
        self.actionreserved.setCheckable(True)
        self.actionreserved.setObjectName("actionreserved")
        self.actionreservedPerShare = QtWidgets.QAction(MainWindow)
        self.actionreservedPerShare.setCheckable(True)
        self.actionreservedPerShare.setObjectName("actionreservedPerShare")
        self.actionesp = QtWidgets.QAction(MainWindow)
        self.actionesp.setCheckable(True)
        self.actionesp.setObjectName("actionesp")
        self.actiontimeToMarket = QtWidgets.QAction(MainWindow)
        self.actiontimeToMarket.setCheckable(True)
        self.actiontimeToMarket.setObjectName("actiontimeToMarket")
        self.actionundp = QtWidgets.QAction(MainWindow)
        self.actionundp.setCheckable(True)
        self.actionundp.setObjectName("actionundp")
        self.actionperundp = QtWidgets.QAction(MainWindow)
        self.actionperundp.setCheckable(True)
        self.actionperundp.setObjectName("actionperundp")
        self.actionrev = QtWidgets.QAction(MainWindow)
        self.actionrev.setCheckable(True)
        self.actionrev.setObjectName("actionrev")
        self.actionprofit = QtWidgets.QAction(MainWindow)
        self.actionprofit.setCheckable(True)
        self.actionprofit.setObjectName("actionprofit")
        self.actiongpr = QtWidgets.QAction(MainWindow)
        self.actiongpr.setCheckable(True)
        self.actiongpr.setObjectName("actiongpr")
        self.actionnpr = QtWidgets.QAction(MainWindow)
        self.actionnpr.setCheckable(True)
        self.actionnpr.setObjectName("actionnpr")
        self.actionholders = QtWidgets.QAction(MainWindow)
        self.actionholders.setCheckable(True)
        self.actionholders.setObjectName("actionholders")
        self.actioneps = QtWidgets.QAction(MainWindow)
        self.actioneps.setCheckable(True)
        self.actioneps.setObjectName("actioneps")
        self.actioncode = QtWidgets.QAction(MainWindow)
        self.actioncode.setCheckable(True)
        self.actioncode.setObjectName("actioncode")
        self.actionname = QtWidgets.QAction(MainWindow)
        self.actionname.setCheckable(True)
        self.actionname.setObjectName("actionname")
        self.actionbvps = QtWidgets.QAction(MainWindow)
        self.actionbvps.setCheckable(True)
        self.actionbvps.setObjectName("actionbvps")
        self.menuParament_List.addAction(self.actioncode)
        self.menuParament_List.addAction(self.actionname)
        self.menuParament_List.addAction(self.actionindustry)
        self.menuParament_List.addAction(self.actionarea)
        self.menuParament_List.addAction(self.actionPE)
        self.menuParament_List.addAction(self.actionoutstanding)
        self.menuParament_List.addAction(self.actiontotal)
        self.menuParament_List.addAction(self.actiontotalAssets)
        self.menuParament_List.addAction(self.actionliquidAssets)
        self.menuParament_List.addAction(self.actionfixedAssets)
        self.menuParament_List.addAction(self.actionreserved)
        self.menuParament_List.addAction(self.actionreservedPerShare)
        self.menuParament_List.addAction(self.actioneps)
        self.menuParament_List.addAction(self.actionbvps)
        self.menuParament_List.addAction(self.actionPB)
        self.menuParament_List.addAction(self.actiontimeToMarket)
        self.menuParament_List.addAction(self.actionundp)
        self.menuParament_List.addAction(self.actionperundp)
        self.menuParament_List.addAction(self.actionrev)
        self.menuParament_List.addAction(self.actionprofit)
        self.menuParament_List.addAction(self.actiongpr)
        self.menuParament_List.addAction(self.actionnpr)
        self.menuParament_List.addAction(self.actionholders)
        self.menubar.addAction(self.menuParament_List.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "stock analysis"))
        self.SearchPushButton.setText(_translate("MainWindow", "Search"))
        self.menuParament_List.setTitle(_translate("MainWindow", "Add"))
        self.actionPE.setText(_translate("MainWindow", "pe"))
        self.actionPE.setToolTip(_translate("MainWindow", "pe"))
        self.actionPE.setStatusTip(_translate("MainWindow", "市盈率"))
        self.actionPB.setText(_translate("MainWindow", "pb"))
        self.actionPB.setStatusTip(_translate("MainWindow", "市净率"))
        self.actionTime.setText(_translate("MainWindow", "Time"))
        self.actiontotal.setText(_translate("MainWindow", "totals"))
        self.actiontotal.setStatusTip(_translate("MainWindow", "总股本（万）"))
        self.actionPrice.setText(_translate("MainWindow", "Price"))
        self.actionindustry.setText(_translate("MainWindow", "industry"))
        self.actionindustry.setStatusTip(_translate("MainWindow", "细分行业"))
        self.actionarea.setText(_translate("MainWindow", "area"))
        self.actionarea.setStatusTip(_translate("MainWindow", "地区"))
        self.actionoutstanding.setText(_translate("MainWindow", "outstanding"))
        self.actionoutstanding.setStatusTip(_translate("MainWindow", "流通股本"))
        self.actiontotalAssets.setText(_translate("MainWindow", "totalAssets"))
        self.actiontotalAssets.setStatusTip(_translate("MainWindow", "总资产（万）"))
        self.actionliquidAssets.setText(_translate("MainWindow", "liquidAssets"))
        self.actionliquidAssets.setStatusTip(_translate("MainWindow", "流动资产"))
        self.actionfixedAssets.setText(_translate("MainWindow", "fixedAssets"))
        self.actionfixedAssets.setStatusTip(_translate("MainWindow", "固定资产"))
        self.actionreserved.setText(_translate("MainWindow", "reserved"))
        self.actionreserved.setStatusTip(_translate("MainWindow", "公积金"))
        self.actionreservedPerShare.setText(_translate("MainWindow", "reservedPerShare"))
        self.actionreservedPerShare.setStatusTip(_translate("MainWindow", "每股公积金"))
        self.actionesp.setText(_translate("MainWindow", "esp"))
        self.actiontimeToMarket.setText(_translate("MainWindow", "timeToMarket"))
        self.actiontimeToMarket.setStatusTip(_translate("MainWindow", "上市日期"))
        self.actionundp.setText(_translate("MainWindow", "undp"))
        self.actionundp.setStatusTip(_translate("MainWindow", "未分配利润"))
        self.actionperundp.setText(_translate("MainWindow", "perundp"))
        self.actionperundp.setStatusTip(_translate("MainWindow", "每股未分配"))
        self.actionrev.setText(_translate("MainWindow", "rev"))
        self.actionrev.setStatusTip(_translate("MainWindow", "收入同比（%）"))
        self.actionprofit.setText(_translate("MainWindow", "profit"))
        self.actionprofit.setStatusTip(_translate("MainWindow", "利润同比(%)"))
        self.actiongpr.setText(_translate("MainWindow", "gpr"))
        self.actiongpr.setStatusTip(_translate("MainWindow", "毛利率(%)"))
        self.actionnpr.setText(_translate("MainWindow", "npr"))
        self.actionnpr.setStatusTip(_translate("MainWindow", "净利润率(%)"))
        self.actionholders.setText(_translate("MainWindow", "holders"))
        self.actionholders.setStatusTip(_translate("MainWindow", "股东人数"))
        self.actioneps.setText(_translate("MainWindow", "esp"))
        self.actioneps.setStatusTip(_translate("MainWindow", "每股收益"))
        self.actioncode.setText(_translate("MainWindow", "code"))
        self.actioncode.setStatusTip(_translate("MainWindow", "股票代码"))
        self.actionname.setText(_translate("MainWindow", "name"))
        self.actionname.setStatusTip(_translate("MainWindow", "股票名称"))
        self.actionbvps.setText(_translate("MainWindow", "bvps"))
        self.actionbvps.setStatusTip(_translate("MainWindow", "每股净资"))

