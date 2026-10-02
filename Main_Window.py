from PyQt6 import QtCore, QtGui, QtWidgets


class MTT_Main_Window(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(856, 706)
        Form.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 50, 201, 661))
        self.frame.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(19)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButton.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setStyleSheet("background-color: rgb(125, 125, 125);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 201, 61))
        self.frame_2.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"\n"
"border: 2px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main Window"))
        self.pushButton.setText(_translate("Form", "Личный Кабинет"))
        self.pushButton_3.setText(_translate("Form", "Заказы"))
        self.pushButton_2.setText(_translate("Form", "Платежи"))
        self.pushButton_4.setText(_translate("Form", "Клиенты"))
        self.pushButton_5.setText(_translate("Form", "Туры"))
        self.pushButton_6.setText(_translate("Form", "Отзывы"))
        self.pushButton_9.setText(_translate("Form", "Сотрудники"))
        self.pushButton_7.setText(_translate("Form", "Настройки"))


# ---------- ЗАПУСК ----------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MTT_Main_Window()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
