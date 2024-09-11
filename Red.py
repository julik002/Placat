import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import psycopg2


class Ui_Red(object):
    def setupUi(self, Red):
        Red.setObjectName("Red")
        Red.setFixedSize(797, 549)
        Red.setStyleSheet("background-color:   #ffe4c4;")
        Red.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.lineEdit_7 = QtWidgets.QLineEdit(Red)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 290, 331, 31))
        self.lineEdit_7.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Red)
        self.lineEdit_6.setGeometry(QtCore.QRect(420, 230, 331, 31))
        self.lineEdit_6.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.comboBox_3 = QtWidgets.QComboBox(Red)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 350, 331, 31))
        self.comboBox_3.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["Горизонтальная","Вертикальная"])
        
        self.lineEdit_9 = QtWidgets.QLineEdit(Red)
        self.lineEdit_9.setGeometry(QtCore.QRect(420, 350, 331, 31))
        self.lineEdit_9.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_5 = QtWidgets.QLabel(Red)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #355c7d;")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Red)
        self.label_7.setGeometry(QtCore.QRect(50, 326, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #355c7d;")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Red)
        self.label_3.setGeometry(QtCore.QRect(420, 86, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #355c7d;")
        self.label_3.setObjectName("label_3")

        self.comboBox_1 = QtWidgets.QComboBox(Red)
        self.comboBox_1.setGeometry(QtCore.QRect(50, 170, 331, 31))
        self.comboBox_1.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(["Москва Большая Школа", "Издательство 1", "Издательство 2"])

        self.label_9 = QtWidgets.QLabel(Red)
        self.label_9.setGeometry(QtCore.QRect(420, 205, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #355c7d;")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(Red)
        self.lineEdit.setGeometry(QtCore.QRect(50, 110, 331, 31))
        self.lineEdit.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_12 = QtWidgets.QLineEdit(Red)
        self.lineEdit_12.setGeometry(QtCore.QRect(420, 410, 331, 31))
        self.lineEdit_12.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_11 = QtWidgets.QLabel(Red)
        self.label_11.setGeometry(QtCore.QRect(420, 325, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #355c7d;")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(Red)
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

        self.comboBox_2 = QtWidgets.QComboBox(Red)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 290, 331, 31))
        self.comboBox_2.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["A2","A3", "A4", "A5"]) 

        self.label = QtWidgets.QLabel(Red)
        self.label.setGeometry(QtCore.QRect(260, 10, 271, 41))
        self.lineEdit.setValidator(QIntValidator())
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #355c7d;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Red)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 110, 331, 31))
        self.lineEdit_2.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(Red)
        self.label_8.setGeometry(QtCore.QRect(420, 146, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #355c7d;")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Red)
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
        self.label_4 = QtWidgets.QLabel(Red)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #355c7d;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Red)
        self.label_6.setGeometry(QtCore.QRect(50, 270, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #355c7d;")
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(Red)
        self.label_12.setGeometry(QtCore.QRect(50, 389, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #355c7d;")
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(Red)
        self.label_2.setGeometry(QtCore.QRect(50, 86, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #355c7d;")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Red)
        self.label_10.setGeometry(QtCore.QRect(420, 265, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #355c7d;")
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(Red)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 170, 331, 31))
        self.lineEdit_4.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QIntValidator())
        self.lineEdit_11 = QtWidgets.QLineEdit(Red)
        self.lineEdit_11.setGeometry(QtCore.QRect(50, 410, 331, 31))
        self.lineEdit_11.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(Red)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 230, 331, 31))
        self.lineEdit_5.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Red)
        QtCore.QMetaObject.connectSlotsByName(Red)

    def retranslateUi(self, Red):
        _translate = QtCore.QCoreApplication.translate
        Red.setWindowTitle(_translate("Red", "Редактирование"))
        self.label_5.setText(_translate("Red", "Тема"))
        self.label_7.setText(_translate("Red", "Ориентация"))
        self.label_3.setText(_translate("Red", "Код"))
        self.label_9.setText(_translate("Red", "Серия"))
        self.label_11.setText(_translate("Red", "Ссылка на фото"))
        self.label_13.setText(_translate("Red", "Примечание"))
        self.label.setText(_translate("Red", "Редактирование"))
        self.label_8.setText(_translate("Red", "Год"))
        self.pushButton.setText(_translate("Red", "Сохранить"))
        self.pushButton.clicked.connect(self.update_data_in_database)
        self.label_4.setText(_translate("Red", "Издательство"))
        self.label_6.setText(_translate("Red", "Наименование"))
        self.label_12.setText(_translate("Red", "Примечание"))
        self.label_2.setText(_translate("Red", "Номер"))
        self.label_10.setText(_translate("Red", "Формат"))

    def update_data_in_database(self):
        required_fields = [
                self.lineEdit.text(),
                self.lineEdit_2.text(),
                self.comboBox_1.currentText(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text()
        ]

        if any(not field.strip() for field in required_fields):
                QtWidgets.QMessageBox.warning(None, "Внимание", "Поля: Номер, Код, Издательство, Год и Тема обязательны для заполнения.")
                return
                
        data_to_update = [
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
                self.lineEdit_12.text(),
                self.lineEdit.text()
        ]

        try:
                conn = psycopg2.connect(
                user='postgres',
                password='kjGWjiD',
                database='Posters',
                host='localhost'
                )

                cur = conn.cursor()

                update_query = "UPDATE posters SET number = %s, code = %s, publishing_house = %s, year = %s, topic = %s, series = %s, name = %s, format = %s, orientation = %s, link_to_the_photo = %s, note_1 = %s, note_2 = %s WHERE number = %s;"
                cur.execute(update_query, data_to_update)
                conn.commit()

                conn.close()

                QtWidgets.QMessageBox.information(None, "Успех", "Данные успешно обновлены в базе данных.")
                QtWidgets.QApplication.instance().activeWindow().close()  # закрываем активное окно
                
        except (Exception, psycopg2.Error) as error:
                print(f"Ошибка при обновлении данных в базе данных: {error}")
                sys.exit(1)

                        
