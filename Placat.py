from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QDialog
import psycopg2
from Dob import Ui_Dod
from Red import Ui_Red


class Ui_Placat(object):
    def setupUi(self, Placat):
        Placat.setObjectName("Placat")
        Placat.setFixedSize(1366, 700)
        Placat.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        Placat.showMaximized()
        Placat.setStyleSheet("\n"
"background-color:   #ffe4c4;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Placat)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1344, 511))
        self.tableWidget.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.tableWidget.setObjectName("tableWidget")

        # Размер текста в таблице
        self.tableWidget.setStyleSheet("QTableWidget { font-size: 10pt; }")

        # Размер текста заголовков таблицы
        header = self.tableWidget.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { font-size: 11pt; }")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 1021, 31))
        self.lineEdit.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1130, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: #355c7d;\n"
"background-color:   #ffcc99;\n"
"border-radius: 20px;                     \n"
"border: 2px solid #355c7d;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 630, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: #355c7d;\n"
"background-color:   #ffcc99;\n"
"border-radius: 20px;                     \n"
"border: 2px solid #355c7d;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 630, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: #355c7d;\n"
"background-color:   #ffcc99;\n"
"border-radius: 20px;                     \n"
"border: 2px solid #355c7d;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 630, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: #355c7d;\n"
"background-color:   #ffcc99;\n"
"border-radius: 20px;                     \n"
"border: 2px solid #355c7d;")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #355c7d;\n"
"")
        self.label.setObjectName("label")

        Placat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Placat)
        self.populate_table_widget()
        QtCore.QMetaObject.connectSlotsByName(Placat)

    def populate_table_widget(self):
        try:
            conn = psycopg2.connect(
                user='postgres',
                password='kjGWjiD',
                database='Posters',
                host='localhost'
            )

            cur = conn.cursor()

            cur.execute('SELECT * FROM posters')
            rows = cur.fetchall()
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(12)  # Устанавливаем количество столбцов
            self.tableWidget.setHorizontalHeaderLabels(["Номер","Код", "Издательство", "Год", "Тема", "Серия", "Наименование", "Формат", "Ориентация", "Ссылка на фото", "Примечание", "Примечание"])
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Делаем таблицу нередактируемой

            for row_num, row_data in enumerate(rows):
                for col_num, cell_data in enumerate(row_data):
                        if cell_data is None:  # Проверка значения None
                            item = QtWidgets.QTableWidgetItem("")
                        else:
                            item = QtWidgets.QTableWidgetItem(str(cell_data))
                            self.tableWidget.setItem(row_num, col_num, item)

            column_widths = [50, 80, 170, 20, 200, 350, 350, 100, 100, 150, 200, 200]  # Ширина столбцов
            for col, width in enumerate(column_widths):
                self.tableWidget.setColumnWidth(col, width)

            conn.close()

        except (Exception, psycopg2.Error) as error:
            print("Ошибка при подключении к PostgreSQL:", error)

    def retranslateUi(self, Placat):
        _translate = QtCore.QCoreApplication.translate
        Placat.setWindowTitle(_translate("Placat", "Плакаты"))
        self.pushButton.setText(_translate("Placat", "Добавить"))
        self.pushButton.clicked.connect(self.open_add_dialog)
        self.pushButton_2.setText(_translate("Placat", "Редактировать"))
        self.pushButton_2.clicked.connect(self.open_edit_dialog)
        self.pushButton_3.setText(_translate("Placat", "Удалить"))
        self.pushButton_3.clicked.connect(self.delete_row_from_database)
        self.label.setText(_translate("Placat", "Плакаты"))
        self.pushButton_4.setText(_translate("Placat", "Найти"))
        self.pushButton_4.clicked.connect(self.search_all_fields)
    
    def open_add_dialog(self):
        self.add_dialog = QDialog()
        self.ui_add_dialog = Ui_Dod()
        self.ui_add_dialog.setupUi(self.add_dialog, self)

        self.add_dialog.show()

    def open_edit_dialog(self):
        selected_row = self.tableWidget.currentRow()
        
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите строку для редактирования.")
            return
        
        data_to_edit = []
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(selected_row, col)
            if item:
                data_to_edit.append(item.text())
            else:
                data_to_edit.append("")  # Заполняем пустыми строками, если ячейка пуста

        self.edit_dialog = QtWidgets.QDialog()
        self.ui_edit_dialog = Ui_Red()
        self.ui_edit_dialog.setupUi(self.edit_dialog)
        self.fill_edit_dialog_fields(data_to_edit)  # Передаем данные в окно редактирования
        self.edit_dialog.finished.connect(self.update_table_widget)  # Обновление таблицы при закрытии диалогового окна
        self.edit_dialog.show()

    def fill_edit_dialog_fields(self, data):
        self.ui_edit_dialog.lineEdit.setText(data[0])
        self.ui_edit_dialog.lineEdit_2.setText(data[1])
        self.ui_edit_dialog.comboBox_1.setCurrentText(data[2])
        self.ui_edit_dialog.lineEdit_4.setText(data[3])
        self.ui_edit_dialog.lineEdit_5.setText(data[4])
        self.ui_edit_dialog.lineEdit_6.setText(data[5])
        self.ui_edit_dialog.lineEdit_7.setText(data[6])
        self.ui_edit_dialog.comboBox_2.setCurrentText(data[7])
        self.ui_edit_dialog.comboBox_3.setCurrentText(data[8])
        self.ui_edit_dialog.lineEdit_9.setText(data[9])
        self.ui_edit_dialog.lineEdit_11.setText(data[10])
        self.ui_edit_dialog.lineEdit_12.setText(data[11])

    def update_table_widget(self):
        self.tableWidget.clearContents()
        self.populate_table_widget()  

    def delete_row_from_database(self):
        selected_row = self.tableWidget.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите строку для удаления.")
            return

        number_to_delete = self.tableWidget.item(selected_row, 0).text()  # Номер строки для удаления

        try:
            conn = psycopg2.connect(
                user='postgres',
                password='kjGWjiD',
                database='Posters',
                host='localhost'
            )

            cur = conn.cursor()

            delete_query = "DELETE FROM posters WHERE number = %s;"
            cur.execute(delete_query, (number_to_delete,))
            conn.commit()

            conn.close()

            QtWidgets.QMessageBox.information(None, "Успех", "Запись успешно удалена из базы данных.")
            self.update_table_widget()  # Обновить таблицу после удаления записи

        except (Exception, psycopg2.Error) as error:
            print(f"Ошибка при удалении записи из базы данных: {error}")
            sys.exit(1)  

    def search_all_fields(self):
        search_text = self.lineEdit.text()

        try:
            conn = psycopg2.connect(
                user='postgres',
                password='kjGWjiD',
                database='Posters',
                host='localhost'
            )

            cur = conn.cursor()

            query = """SELECT * FROM posters
                        WHERE number::text ILIKE %s
                        OR code ILIKE %s
                        OR publishing_house ILIKE %s
                        OR year::text ILIKE %s
                        OR topic ILIKE %s
                        OR series ILIKE %s
                        OR name ILIKE %s
                        OR format ILIKE %s
                        OR orientation ILIKE %s
                        OR link_to_the_photo ILIKE %s
                        OR note_1 ILIKE %s
                        OR note_2 ILIKE %s"""

            cur.execute(query, (f'%{search_text}%',) * 12)
            rows = cur.fetchall()

            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(rows))

            for row_num, row_data in enumerate(rows):
                for col_num, cell_data in enumerate(row_data):
                    if cell_data is None:
                        item = QtWidgets.QTableWidgetItem("")
                    else:
                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.tableWidget.setItem(row_num, col_num, item)

            conn.close()

        except (Exception, psycopg2.Error) as error:
            print("Ошибка при поиске в PostgreSQL:", error)