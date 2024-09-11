from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import psycopg2


class Ui_Dod(object):
    def setupUi(self, Dod, main_window):
        Dod.setObjectName("Dod")
        Dod.setFixedSize(800, 551)
        Dod.setStyleSheet("\n"
"background-color:   #ffe4c4;\n"
"")
        Dod.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.main_window = main_window
        self.lineEdit = QtWidgets.QLineEdit(Dod)
        self.lineEdit.setGeometry(QtCore.QRect(50, 110, 331, 31))
        self.lineEdit.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QIntValidator())
        self.label = QtWidgets.QLabel(Dod)
        self.label.setGeometry(QtCore.QRect(290, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #355c7d;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 110, 331, 31))
        self.lineEdit_2.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dod)
        self.label_2.setGeometry(QtCore.QRect(50, 86, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #355c7d;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dod)
        self.label_3.setGeometry(QtCore.QRect(420, 86, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #355c7d;")
        self.label_3.setObjectName("label_3")

        self.comboBox_1 = QtWidgets.QComboBox(Dod)
        self.comboBox_1.setGeometry(QtCore.QRect(50, 170, 331, 31))
        self.comboBox_1.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(["Москва Большая Школа", "Издательство 1", "Издательство 2", "Издательство 3", "Издательство 4", "Издательство 5"])

        self.lineEdit_4 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 170, 331, 31))
        self.lineEdit_4.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QIntValidator())
        self.lineEdit_5 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 230, 331, 31))
        self.lineEdit_5.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_6.setGeometry(QtCore.QRect(420, 230, 331, 31))
        self.lineEdit_6.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 290, 331, 31))
        self.lineEdit_7.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.comboBox_2 = QtWidgets.QComboBox(Dod)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 290, 331, 31))
        self.comboBox_2.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["A2","A3", "A4", "A5"])

        self.label_4 = QtWidgets.QLabel(Dod)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #355c7d;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_9.setGeometry(QtCore.QRect(420, 350, 331, 31))
        self.lineEdit_9.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.comboBox_3 = QtWidgets.QComboBox(Dod)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 350, 331, 31))
        self.comboBox_3.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["Горизонтальная","Вертикальная"])

        self.label_5 = QtWidgets.QLabel(Dod)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #355c7d;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dod)
        self.label_6.setGeometry(QtCore.QRect(50, 270, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #355c7d;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dod)
        self.label_7.setGeometry(QtCore.QRect(50, 326, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #355c7d;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dod)
        self.label_8.setGeometry(QtCore.QRect(420, 146, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #355c7d;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dod)
        self.label_9.setGeometry(QtCore.QRect(420, 205, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #355c7d;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dod)
        self.label_10.setGeometry(QtCore.QRect(420, 265, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #355c7d;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dod)
        self.label_11.setGeometry(QtCore.QRect(420, 325, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #355c7d;")
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_11.setGeometry(QtCore.QRect(50, 410, 331, 31))
        self.lineEdit_11.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dod)
        self.lineEdit_12.setGeometry(QtCore.QRect(420, 410, 331, 31))
        self.lineEdit_12.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_12 = QtWidgets.QLabel(Dod)
        self.label_12.setGeometry(QtCore.QRect(50, 389, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #355c7d;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dod)
        self.label_13.setGeometry(QtCore.QRect(420, 389, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #355c7d;\n"
"")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Dod)
        self.pushButton.setGeometry(QtCore.QRect(310, 470, 181, 51))
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

        self.retranslateUi(Dod)
        QtCore.QMetaObject.connectSlotsByName(Dod)

    def retranslateUi(self, Dod):
        _translate = QtCore.QCoreApplication.translate
        Dod.setWindowTitle(_translate("Dod", "Добавление"))
        self.label.setText(_translate("Dod", "Добавление"))
        self.label_2.setText(_translate("Dod", "Номер"))
        self.label_3.setText(_translate("Dod", "Код"))
        self.label_4.setText(_translate("Dod", "Издательство"))
        self.label_5.setText(_translate("Dod", "Тема"))
        self.label_6.setText(_translate("Dod", "Наименование"))
        self.label_7.setText(_translate("Dod", "Ориентация"))
        self.label_8.setText(_translate("Dod", "Год"))
        self.label_9.setText(_translate("Dod", "Серия"))
        self.label_10.setText(_translate("Dod", "Формат"))
        self.label_11.setText(_translate("Dod", "Ссылка на фото"))
        self.label_12.setText(_translate("Dod", "Примечание"))
        self.label_13.setText(_translate("Dod", "Примечание"))
        self.pushButton.setText(_translate("Dod", "Добавить"))
        self.pushButton.clicked.connect(lambda: self.add_data_to_db(Dod))


    def add_data_to_db(self, window):
        conn = psycopg2.connect(
                user='postgres',
                password='kjGWjiD',
                database='Posters',
                host='localhost'
        )

        cursor = conn.cursor()

        # Проверка обязательных полей
        if not all([self.lineEdit.text(), self.lineEdit_2.text(), self.comboBox_1.currentText(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()]):
                QtWidgets.QMessageBox.critical(None, "Ошибка", "Необходимо заполнить все обязательные поля!\nНомер, Код, Издательство, Год, Тема, Серия")
                return

        sql = "INSERT INTO posters (number, code, publishing_house, year, topic, series, name, format, orientation, link_to_the_photo, note_1, note_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        values = (
                self.lineEdit.text(),
                self.lineEdit_2.text(),
                self.comboBox_1.currentText(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text(),
                self.lineEdit_6.text(),
                self.lineEdit_7.text(),
                self.comboBox_2.currentText(),
                self.comboBox_3.currentText(),
                self.lineEdit_9.text(),
                self.lineEdit_11.text(),
                self.lineEdit_12.text()
        )

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

        QtWidgets.QMessageBox.information(None, "Успех", "Данные успешно сохранены!")

        # Закрыть окно после успешного сохранения данных
        window.close()
        self.main_window.update_table_widget()