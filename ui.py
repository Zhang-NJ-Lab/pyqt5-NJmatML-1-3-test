# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 41))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_pandas = QtWidgets.QAction(MainWindow)
        self.action_pandas.setObjectName("action_pandas")
        self.action_heatmap = QtWidgets.QAction(MainWindow)
        self.action_heatmap.setObjectName("action_heatmap")
        self.actionrfe = QtWidgets.QAction(MainWindow)
        self.actionrfe.setObjectName("actionrfe")
        self.menu.addAction(self.action_pandas)
        self.menu.addAction(self.action_heatmap)
        self.menu.addAction(self.actionrfe)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action_pandas.setText(_translate("MainWindow", "打开的文件名可视化pandas数据"))
        self.action_heatmap.setText(_translate("MainWindow", "封装函数特征选择之前heatmap画热图"))
        self.actionrfe.setText(_translate("MainWindow", "rfe特征选择"))
