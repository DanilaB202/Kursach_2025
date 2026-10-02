from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sqlite3


# ---------- UI ----------
class Registration_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 464)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(650, 500))
        Form.setStyleSheet("background-color: rgb(67, 67, 67);")

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 391, 106))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 160, 391, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(177, 177, 177); color: rgb(83, 83, 83);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 230, 391, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(177, 177, 177); color: rgb(83, 83, 83);")
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 300, 391, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(177, 177, 177); color: rgb(83, 83, 83);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(191, 191, 191); color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(191, 191, 191); color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Модуль Туристических путёвок"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_4.setText(_translate("Form", "Имя:"))
        self.label_2.setText(_translate("Form", "Юзернейм:"))
        self.label_3.setText(_translate("Form", "Пароль:"))
        self.pushButton.setText(_translate("Form", "Регистрация"))
        self.pushButton_2.setText(_translate("Form", "Есть Аккаунт?"))


# ---------- ЛОГИКА ----------
class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Registration_UI()
        self.ui.setupUi(self)

        self.setWindowTitle("Модуль Туристических путёвок")

        # Подсказки и очистка
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_3.setPlaceholderText("Введите ваше реальное имя...")
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setPlaceholderText("Введите юзернейм...")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_2.setPlaceholderText("Введите пароль...")

        # Скрытие пароля
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Кнопки
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.go_to_login)

    def register(self):
        name = self.ui.lineEdit_3.text().strip()
        login = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not name or not login or not password:
            QMessageBox.warning(self, "Ошибка", "Все поля обязательны для заполнения!")
            return

        # Запрещённые имена
        forbidden_names = [
            "админ", "admin", "administrator","менеджер","manager",
            "гитлер", "hitler", "гиммлер", "бандера",
            "нигга", "ниггер", "nigger", "nigga",
            "fuck", "shit", "bitch", "ass", "dick", "pussy", "cock",
            "хуй", "гондон", "сука", "ублюдок", "мразь",
        ]

        if len(name) < 2 or name.lower() in forbidden_names:
            QMessageBox.warning(self, "Ошибка", "Данное имя пользователя недопустимо!")
            return

        if len(password) < 4:
            QMessageBox.warning(self, "Ошибка", "Пароль слишком короткий, придумайте более сложный пароль!")
            return

        db = sqlite3.connect("Baranov308is.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Staff WHERE Login=?", (login,))
        if cursor.fetchone():
            QMessageBox.warning(self, "Ошибка", "Такой логин уже существует!")
            db.close()
            return

        cursor.execute("INSERT INTO Staff (Name, Login, Password) VALUES (?, ?, ?)", (name, login, password))
        db.commit()
        db.close()

        QMessageBox.information(self, "Успех", f"Пользователь {name} зарегистрирован и вошёл в систему!")
        self.close()

    def go_to_login(self):
        QMessageBox.information(self, "Переход", "Переход на окно входа (LoginWindow).")
        self.close()


# ---------- ЗАПУСК ----------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())



