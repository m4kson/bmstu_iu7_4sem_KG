# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pyqtgraph import PlotWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from class_point import Point
from triangle import *

set_A = []
set_B = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 731)
        MainWindow.setMinimumSize(QtCore.QSize(1293, 731))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1020, 80, 271, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(40, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setObjectName("add_btn")
        self.add_x_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.add_x_spinbox.setGeometry(QtCore.QRect(50, 140, 61, 31))
        self.add_x_spinbox.setDecimals(3)
        self.add_x_spinbox.setMinimum(-99999999.0)
        self.add_x_spinbox.setMaximum(99999999.0)
        self.add_x_spinbox.setObjectName("add_x_spinbox")
        self.number_delete_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.number_delete_spinbox.setGeometry(QtCore.QRect(40, 260, 141, 31))
        self.number_delete_spinbox.setMaximum(1000000)
        self.number_delete_spinbox.setObjectName("number_delete_spinbox")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(40, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setObjectName("delete_btn")
        self.info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.info_btn.setGeometry(QtCore.QRect(550, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.info_btn.setFont(font)
        self.info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_btn.setObjectName("info_btn")
        self.change_number_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.change_number_spinbox.setGeometry(QtCore.QRect(20, 390, 61, 31))
        self.change_number_spinbox.setMaximum(1000)
        self.change_number_spinbox.setObjectName("change_number_spinbox")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(20, 420, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.change_btn.setFont(font)
        self.change_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_btn.setObjectName("change_btn")
        self.answer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.answer_btn.setGeometry(QtCore.QRect(40, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.answer_btn.setFont(font)
        self.answer_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_btn.setObjectName("answer_btn")
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(40, 600, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.print_btn.setFont(font)
        self.print_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.print_btn.setObjectName("print_btn")
        self.clean_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clean_btn.setGeometry(QtCore.QRect(40, 650, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.clean_btn.setFont(font)
        self.clean_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clean_btn.setObjectName("clean_btn")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 80, 771, 551))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 110, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 230, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 350, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 350, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 350, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.add_y_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.add_y_spinbox.setGeometry(QtCore.QRect(120, 140, 61, 31))
        self.add_y_spinbox.setDecimals(3)
        self.add_y_spinbox.setMinimum(-99999999.0)
        self.add_y_spinbox.setMaximum(99999999.0)
        self.add_y_spinbox.setObjectName("add_y_spinbox")
        self.change_x_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.change_x_spinbox.setGeometry(QtCore.QRect(90, 390, 61, 31))
        self.change_x_spinbox.setDecimals(3)
        self.change_x_spinbox.setMinimum(-99999999.0)
        self.change_x_spinbox.setMaximum(99999999.0)
        self.change_x_spinbox.setObjectName("change_x_spinbox")
        self.change_y_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.change_y_spinbox.setGeometry(QtCore.QRect(160, 390, 61, 31))
        self.change_y_spinbox.setDecimals(3)
        self.change_y_spinbox.setMinimum(-99999999.0)
        self.change_y_spinbox.setMaximum(99999999.0)
        self.change_y_spinbox.setObjectName("change_y_spinbox")
        self.choose_set = QtWidgets.QComboBox(self.centralwidget)
        self.choose_set.setGeometry(QtCore.QRect(70, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.choose_set.setFont(font)
        self.choose_set.setMaxVisibleItems(2)
        self.choose_set.setObjectName("choose_set")
        self.choose_set.addItem("")
        self.choose_set.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.choose_set.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my code
        self.info_btn.clicked.connect(show_info)
        self.add_btn.clicked.connect(lambda: self.addPoint(set_A, set_B))
        self.delete_btn.clicked.connect(lambda: self.deletePoint(set_A, set_B))
        self.change_btn.clicked.connect(lambda: self.changePoint(set_A, set_B))
        self.answer_btn.clicked.connect(lambda: self.print_ans(set_A, set_B))
        self.clean_btn.clicked.connect(lambda: self.clear_all(set_A, set_B))

    # my funcs

    def addPoint(self, pointArrA, pointArrB):
        x = self.add_x_spinbox.value()
        y = self.add_y_spinbox.value()

        flag = False
        if self.choose_set.currentText() == "set A":
            for point in pointArrA:
                if point.is_equal(x, y):
                    flag = True
                    break
        elif self.choose_set.currentText() == "set B":
            for point in pointArrB:
                if point.is_equal(x, y):
                    flag = True
                    break
        if not flag:
            if self.choose_set.currentText() == "set A":
                pointArrA.append(Point(x, y))
                self.tableWidget.setRowCount(len(pointArrA))
                self.tableWidget.setColumnCount(2)
                self.tableWidget.setItem(len(pointArrA) - 1, 0, QTableWidgetItem(str(x)))
                self.tableWidget.setItem(len(pointArrA) - 1, 1, QTableWidgetItem(str(y)))
            elif self.choose_set.currentText() == "set B":
                pointArrB.append(Point(x, y))
                self.tableWidget_2.setRowCount(len(pointArrB))
                self.tableWidget_2.setColumnCount(2)
                self.tableWidget_2.setItem(len(pointArrB) - 1, 0, QTableWidgetItem(str(x)))
                self.tableWidget_2.setItem(len(pointArrB) - 1, 1, QTableWidgetItem(str(y)))

    def deletePoint(self, pointArrA, pointArrB):
        num = self.number_delete_spinbox.value()
        if self.choose_set.currentText() == "set A":
            if num - 1 > len(pointArrA) - 1 or num == 0:
                info = QMessageBox()
                info.setWindowTitle("error")
                info.setText("Incorrect point number!!!")
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()
                return
            pointArrA.pop(num - 1)
            self.tableWidget.removeRow(num - 1)
        elif self.choose_set.currentText() == "set B":
            if num - 1 > len(pointArrB) - 1 or num == 0:
                info = QMessageBox()
                info.setWindowTitle("error")
                info.setText("Incorrect point number!!!")
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()
                return
            pointArrB.pop(num - 1)
            self.tableWidget_2.removeRow(num - 1)

    def changePoint(self, pointArrA, pointArrB):
        num = self.change_number_spinbox.value()
        x = self.change_x_spinbox.value()
        y = self.change_y_spinbox.value()

        if self.choose_set.currentText() == "set A":
            if num > len(pointArrA) or num == 0:
                info = QMessageBox()
                info.setWindowTitle("error")
                info.setText("Incorrect point number!!!")
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()
                return
            pointArrA[num - 1] = Point(x, y)
            self.tableWidget.setItem(num - 1, 0, QTableWidgetItem(str(x)))
            self.tableWidget.setItem(num - 1, 1, QTableWidgetItem(str(y)))

        elif self.choose_set.currentText() == "set B":
            if num > len(pointArrB) or num == 0:
                info = QMessageBox()
                info.setWindowTitle("error")
                info.setText("Incorrect point number!!!")
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()
                return
            pointArrB[num - 1] = Point(x, y)
            self.tableWidget_2.setItem(num - 1, 0, QTableWidgetItem(str(x)))
            self.tableWidget_2.setItem(num - 1, 1, QTableWidgetItem(str(y)))

    def print_ans(self, setA, setB):
        if len(setA) < 3 or len(setB) < 3:
            info = QMessageBox()
            info.setWindowTitle("error")
            info.setText("Can't find answer, not enough data, enter more dots!!!")
            info.setStandardButtons(QMessageBox.Ok)
            info.exec_()
            return

        ans = find_ans(set_A, set_B)
        answindow = QMessageBox()
        answindow.setWindowTitle("answer")
        answindow.setText(
            "Наибольший угол с осью абсцисс образует прямая, пересекающая вершины при тупых углах треугольников А(({}, {}), ({}, {}), ({}, {}) и В(({}, {}), ({}, {}), ({}, {}).".format(
                ans[0].A.x, ans[0].A.y, ans[0].B.x, ans[0].B.y, ans[0].C.x, ans[0].C.y, ans[1].A.x, ans[1].A.y,
                ans[1].B.x, ans[1].B.y, ans[1].C.x, ans[1].C.y))
        answindow.setStandardButtons(QMessageBox.Ok)
        answindow.exec_()

    def clear_all(self, setA, setB):
        for i in range(len(setA), -1, -1):
            self.tableWidget.removeRow(i)
        for i in range(len(setB), -1, -1):
            self.tableWidget_2.removeRow(i)
        setA.clear()
        setB.clear()

        # todo clear graph window


    # my funcs end

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lab 1 kg"))
        self.label.setText(_translate("MainWindow", "Множество А"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.label_2.setText(_translate("MainWindow", "Множество В"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.delete_btn.setText(_translate("MainWindow", "DELETE"))
        self.info_btn.setToolTip(_translate("MainWindow", "fff"))
        self.info_btn.setText(_translate("MainWindow", "INFO"))
        self.change_btn.setText(_translate("MainWindow", "CHANGE"))
        self.answer_btn.setText(_translate("MainWindow", "ANSWER"))
        self.print_btn.setText(_translate("MainWindow", "PRINT"))
        self.clean_btn.setText(_translate("MainWindow", "CLEAN"))
        self.label_3.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "Y:"))
        self.label_5.setText(_translate("MainWindow", "№:"))
        self.label_6.setText(_translate("MainWindow", "X:"))
        self.label_7.setText(_translate("MainWindow", "Y:"))
        self.label_8.setText(_translate("MainWindow", "№:"))
        self.choose_set.setItemText(0, _translate("MainWindow", "set A"))
        self.choose_set.setItemText(1, _translate("MainWindow", "set B"))
        self.label_9.setText(_translate("MainWindow", "SET"))


def show_info():
    info = QMessageBox()
    info.setWindowTitle("INFO")
    info.setText("\t\tЛабораторная работа №1\n"
                 "Задание: На плоскости дано два множества точек.\n"
                 "На точках первого множества строятся треугольники.\n"
                 "На точках второго множества тоже строятся треугольники.\n"
                 "Найти два таких тупоугольных треугольника, у которых прямая,\n"
                 "соединяющая вершины тупых углов, образует максимальный угол с осью абсцисс.\n")

    info.setDetailedText("Сначала пользователю предлагается выбрать множество с помощью spinbox в левом верхнем углу."
                 "После пользователь может добавить, удалить или изменить точку в выбранном множестве, введя необходимые"
                 "данные. Координаты точек задаются вещественным числом, номер точки - целым."
                 "Также пользователь может вывести ответ, нажав на кнопку 'answer'\n"
                 "вывести решение графически кнопкой 'print' или очистить оба множества кнопкой 'clean'")
    info.setStandardButtons(QMessageBox.Ok)
    info.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
