from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Placat import Ui_Placat

USERS_DB = {
    "1": "1",
}

class Ui_Avtoriz(object):
    def setupUi(self, Avtoriz):
        Avtoriz.setObjectName("Avtoriz")
        Avtoriz.setFixedSize(1366, 700)
        Avtoriz.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        Avtoriz.showMaximized()
        Avtoriz.setStyleSheet("background-color:   #ffe4c4;")
        self.centralwidget = QtWidgets.QWidget(Avtoriz)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(515, 280, 331, 31))
        self.lineEdit.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(575, 180, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #355c7d;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(515, 360, 331, 31))
        self.lineEdit_2.setStyleSheet("background-color:#faeedd;\n"
"border: 2px solid #355c7d;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #355c7d;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #355c7d;")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 440, 181, 51))
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
        Avtoriz.setCentralWidget(self.centralwidget)

        self.retranslateUi(Avtoriz)
        QtCore.QMetaObject.connectSlotsByName(Avtoriz)

    def retranslateUi(self, Avtoriz):
        _translate = QtCore.QCoreApplication.translate
        Avtoriz.setWindowTitle(_translate("Avtoriz", "Авторизация"))
        self.label.setText(_translate("Avtoriz", "Авторизация"))
        self.label_4.setText(_translate("Avtoriz", "Логин"))
        self.label_5.setText(_translate("Avtoriz", "Пароль"))
        self.pushButton.setText(_translate("Avtoriz", "Войти"))
        self.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username in USERS_DB and USERS_DB[username] == password:
            QtWidgets.QMessageBox.information(None, "Авторизация успешна", "Добро пожаловать!")

            # Открытие окна "Плакаты" после успешной авторизации
            self.close_window(Avtoriz)
            self.open_placat_window()

        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка авторизации", "Неверные учетные данные")

    def close_window(self, window):
        window.close()

    def open_placat_window(self):
        self.placat_window = QMainWindow()
        self.placat_ui = Ui_Placat()
        self.placat_ui.setupUi(self.placat_window)
        self.placat_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Avtoriz = QMainWindow()
    ui = Ui_Avtoriz()
    ui.setupUi(Avtoriz)
    Avtoriz.show()
    sys.exit(app.exec_())