# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
# from class_point import Point
# from triangle import *
#
# set_A = []
# set_B = []
#
# # my code
# self.info_btn.clicked.connect(show_info)
# self.add_btn.clicked.connect(lambda: self.addPoint(set_A, set_B))
# self.delete_btn.clicked.connect(lambda: self.deletePoint(set_A, set_B))
# self.change_btn.clicked.connect(lambda: self.changePoint(set_A, set_B))
# self.answer_btn.clicked.connect(lambda: self.print_ans(set_A, set_B))
# self.clean_btn.clicked.connect(lambda: self.clear_all(set_A, set_B))
# self.print_btn.clicked.connect(lambda: self.draw())
# self.plot([1, 2, 3, 4, 5], [10, 20, 30, 44, 321])
#
#
# #my funcs
#
#     def addPoint(self, pointArrA, pointArrB):
#         x = self.add_x_spinbox.value()
#         y = self.add_y_spinbox.value()
#
#         flag = False
#         if self.choose_set.currentText() == "set A":
#             for point in pointArrA:
#                 if point.is_equal(x, y):
#                     flag = True
#                     break
#         elif self.choose_set.currentText() == "set B":
#             for point in pointArrB:
#                 if point.is_equal(x, y):
#                     flag = True
#                     break
#         if not flag:
#             if self.choose_set.currentText() == "set A":
#                 pointArrA.append(Point(x, y))
#                 self.tableWidget.setRowCount(len(pointArrA))
#                 self.tableWidget.setColumnCount(2)
#                 self.tableWidget.setItem(len(pointArrA) - 1, 0, QTableWidgetItem(str(x)))
#                 self.tableWidget.setItem(len(pointArrA) - 1, 1, QTableWidgetItem(str(y)))
#             elif self.choose_set.currentText() == "set B":
#                 pointArrB.append(Point(x, y))
#                 self.tableWidget_2.setRowCount(len(pointArrB))
#                 self.tableWidget_2.setColumnCount(2)
#                 self.tableWidget_2.setItem(len(pointArrB) - 1, 0, QTableWidgetItem(str(x)))
#                 self.tableWidget_2.setItem(len(pointArrB) - 1, 1, QTableWidgetItem(str(y)))
#
#     def deletePoint(self, pointArrA, pointArrB):
#         num = self.number_delete_spinbox.value()
#         if self.choose_set.currentText() == "set A":
#             if num - 1 > len(pointArrA) - 1 or num == 0:
#                 info = QMessageBox()
#                 info.setWindowTitle("error")
#                 info.setText("Incorrect point number!!!")
#                 info.setStandardButtons(QMessageBox.Ok)
#                 info.exec_()
#                 return
#             pointArrA.pop(num - 1)
#             self.tableWidget.removeRow(num - 1)
#         elif self.choose_set.currentText() == "set B":
#             if num - 1 > len(pointArrB) - 1 or num == 0:
#                 info = QMessageBox()
#                 info.setWindowTitle("error")
#                 info.setText("Incorrect point number!!!")
#                 info.setStandardButtons(QMessageBox.Ok)
#                 info.exec_()
#                 return
#             pointArrB.pop(num - 1)
#             self.tableWidget_2.removeRow(num - 1)
#
#     def changePoint(self, pointArrA, pointArrB):
#         num = self.change_number_spinbox.value()
#         x = self.change_x_spinbox.value()
#         y = self.change_y_spinbox.value()
#
#         if self.choose_set.currentText() == "set A":
#             if num > len(pointArrA) or num == 0:
#                 info = QMessageBox()
#                 info.setWindowTitle("error")
#                 info.setText("Incorrect point number!!!")
#                 info.setStandardButtons(QMessageBox.Ok)
#                 info.exec_()
#                 return
#             pointArrA[num - 1] = Point(x, y)
#             self.tableWidget.setItem(num - 1, 0, QTableWidgetItem(str(x)))
#             self.tableWidget.setItem(num - 1, 1, QTableWidgetItem(str(y)))
#
#         elif self.choose_set.currentText() == "set B":
#             if num > len(pointArrB) or num == 0:
#                 info = QMessageBox()
#                 info.setWindowTitle("error")
#                 info.setText("Incorrect point number!!!")
#                 info.setStandardButtons(QMessageBox.Ok)
#                 info.exec_()
#                 return
#             pointArrB[num - 1] = Point(x, y)
#             self.tableWidget_2.setItem(num - 1, 0, QTableWidgetItem(str(x)))
#             self.tableWidget_2.setItem(num - 1, 1, QTableWidgetItem(str(y)))
#
#     def print_ans(self, setA, setB):
#         if len(setA) < 3 or len(setB) < 3:
#             info = QMessageBox()
#             info.setWindowTitle("error")
#             info.setText("Can't find answer, not enough data, enter more dots!!!")
#             info.setStandardButtons(QMessageBox.Ok)
#             info.exec_()
#             return
#
#         ans = find_ans(set_A, set_B)
#         answindow = QMessageBox()
#         answindow.setWindowTitle("answer")
#         answindow.setText("Наибольший угол с осью абсцисс образует прямая, пересекающая вершины при тупых углах треугольников А(({}, {}), ({}, {}), ({}, {}) и В(({}, {}), ({}, {}), ({}, {}).".format(ans[0].A.x, ans[0].A.y, ans[0].B.x, ans[0].B.y, ans[0].C.x, ans[0].C.y, ans[1].A.x, ans[1].A.y, ans[1].B.x, ans[1].B.y, ans[1].C.x, ans[1].C.y))
#         answindow.setStandardButtons(QMessageBox.Ok)
#         answindow.exec_()
#
#     def clear_all(self, setA, setB):
#         for i in range(len(setA), -1, -1):
#             self.tableWidget.removeRow(i)
#         for i in range(len(setB), -1, -1):
#             self.tableWidget_2.removeRow(i)
#         setA.clear()
#         setB.clear()
#
#         #todo clear graph window
#
#     def draw(self):
#         self.graphicsView
#
#
#     #my funcs end
#
#
#
#
# def show_info():
#     info = QMessageBox()
#     info.setWindowTitle("INFO")
#     info.setText("\t\tЛабораторная работа №1\n"
#                  "Задание: На плоскости дано два множества точек.\n"
#                  "На точках первого множества строятся треугольники.\n"
#                  "На точках второго множества тоже строятся треугольники.\n"
#                  "Найти два таких тупоугольных треугольника, у которых прямая,\n"
#                  "соединяющая вершины тупых углов, образует максимальный угол с осью абсцисс.\n")
#
#     info.setDetailedText("Сначала пользователю предлагается выбрать множество с помощью spinbox в левом верхнем углу."
#                  "После пользователь может добавить, удалить или изменить точку в выбранном множестве, введя необходимые"
#                  "данные. Координаты точек задаются вещественным числом, номер точки - целым."
#                  "Также пользователь может вывести ответ, нажав на кнопку 'answer'\n"
#                  "вывести решение графически кнопкой 'print' или очистить оба множества кнопкой 'clean'")
#     info.setStandardButtons(QMessageBox.Ok)
#     info.exec_()