
# def add_point(point_arr):
#     x = Ui_MainWindow.add_x_spinbox.value()
#     y = Ui_MainWindow.add_y_spinbox.value()

#     flag = False
#     for point in point_arr:
#         if point.is_equal(x, y):
#             flag = True
#             break

#     if not flag:
#         point_arr.append(Point(x, y))
#         #todo insert in set


def add_point(self, point_arr_A, point_arr_B):
    x = self.add_x_spinbox.value()
    y = self.add_y_spinbox.value()

    flag = False
    if self.choose_set.currentText() == "set A":
        for point in point_arr_A:
            if point.is_equal(x, y):
                flag = True
                break
    elif self.choose_set.currentText() == "set B":
        for point in point_arr_B:
            if point.is_equal(x, y):
                flag = True
                break

    if not flag:

        if self.choose_set.currentText() == "set A":
            point_arr_A.append(Point(x, y))
            item = QtWidgets.QTreeWidgetItem(self.setA)
            item.setText(0, str(len(point_arr_A)))
            item.setText(1, str(x))
            item.setText(2, str(y))

        elif self.choose_set.currentText() == "set B":
            point_arr_B.append(Point(x, y))
            item = QtWidgets.QTreeWidgetItem(self.setB)
            item.setText(0, str(len(point_arr_B)))
            item.setText(1, str(x))
            item.setText(2, str(y))


def delete_point(self, set_A, set_B):
    number = self.number_delete_spinbox.value()
    if self.choose_set.currentText() == "set A":
        item = QtWidgets.QTreeWidget.invisibleRootItem(self.setA).takeChild(self.setA.currentIndex().row())
        QtWidgets.QTreeWidget.invisibleRootItem(self.setA).removeChild(item)

        # set_A.pop(number - 1)
        # item = QtWidgets.QTreeWidgetItem(self.setA)
        # print(number)
        # item.takeChild(number)


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