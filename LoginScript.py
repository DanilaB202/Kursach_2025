from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox
import sqlite3
from RegistrationScript import Registration_UI  # форма регистрации


# ---------- UI ЛОГИНА ----------
class Login_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Модуль Туристических путёвок")
        Form.resize(635, 466)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(650, 500))
        Form.setStyleSheet("background-color: rgb(70, 70, 70);")

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(191, 191, 191); color: black;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 330, 111, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(191, 191, 191); color: black;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(240, 30, 201, 106))
        font_label = QtGui.QFont()
        font_label.setFamily("Segoe UI Variable Small Semibol")
        font_label.setPointSize(48)
        font_label.setBold(True)
        self.label.setFont(font_label)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 71, 31))
        font_small = QtGui.QFont()
        font_small.setFamily("Microsoft YaHei UI")
        font_small.setPointSize(12)
        self.label_2.setFont(font_small)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 81, 31))
        self.label_3.setFont(font_small)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 160, 391, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(177, 177, 177); color: rgb(83, 83, 83);")
        self.lineEdit.setText("")  # поле пустое
        self.lineEdit.setPlaceholderText("Введите логин...")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 240, 391, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(177, 177, 177); color: rgb(83, 83, 83);")
        self.lineEdit_2.setText("")  # поле пустое
        self.lineEdit_2.setPlaceholderText("Введите пароль...")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _t = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_t("Form", "Модуль Туристических путёвок"))
        self.pushButton.setText(_t("Form", "Нет аккаунта?"))
        self.pushButton_2.setText(_t("Form", "Вход"))
        self.label.setText(_t("Form", "Вход"))
        self.label_2.setText(_t("Form", "Логин"))
        self.label_3.setText(_t("Form", "Пароль"))


# ---------- ОКНО РЕГИСТРАЦИИ ----------
class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Registration_UI()
        self.ui.setupUi(self)

        self.setWindowTitle("Модуль Туристических путёвок")

        # Placeholder'ы и очистка
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_3.setPlaceholderText("Введите имя...")
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setPlaceholderText("Введите логин...")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_2.setPlaceholderText("Введите пароль...")

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
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


# ---------- ОКНО ЛОГИНА ----------
class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login_Ui()
        self.ui.setupUi(self)

        self.setWindowTitle("Модуль Туристических путёвок")

        self.ui.pushButton_2.clicked.connect(self.login)
        self.ui.pushButton.clicked.connect(self.ChangeUI)

    def login(self):
        login = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        db = sqlite3.connect("Baranov308is.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Staff WHERE Login=? AND Password=?", (login, password))
        staff = cursor.fetchone()
        db.close()

        if staff:
            QMessageBox.information(self, "Успех", f"Пользователь {staff[1]} успешно вошёл в систему!")
        elif not login or not password:
            QMessageBox.warning(self, "Ошибка", "Поля не должны быть пустыми!")
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")

    def ChangeUI(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()


# ---------- ЗАПУСК ----------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


