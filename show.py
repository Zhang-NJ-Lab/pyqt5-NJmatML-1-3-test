from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from ui import Ui_MainWindow
from NJmatML import dataML
import argparse
import warnings
warnings.filterwarnings("ignore")

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.parser = argparse.ArgumentParser()

        self.action_pandas.triggered.connect(self.one)
        self.action_heatmap.triggered.connect(self.two)
        self.actionrfe.triggered.connect(self.three)



    def one(self):
        dataML.file_name('2DEformationCleaned.csv') #打开csv并存到data中
        dataML.hist()  #画所有列分布的柱状图，例如potential 在0.3 V最多

    def two(self):
        dataML.heatmap_before()  # 画封装函数特征选择之前heatmap热图

    def three(self):
        # 后面四个数字的作用依次是 初始值 最小值 最大值 步幅
        value, ok = QtWidgets.QInputDialog.getInt(self, "输入整数", "请输入希望最后剩余的特征数目:", 37, -10000, 10000, 2)

        dataML.feature_rfe_select1(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()

    ui.show()
    sys.exit(app.exec_())