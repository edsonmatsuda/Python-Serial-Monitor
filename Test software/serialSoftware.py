from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox_ComPort = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ComPort.setGeometry(QtCore.QRect(190, 10, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ComPort.setFont(font)
        self.comboBox_ComPort.setObjectName("comboBox_ComPort")

        self.btn_OpenClosePort = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenClosePort.setGeometry(QtCore.QRect(740, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_OpenClosePort.setFont(font)
        self.btn_OpenClosePort.setObjectName("btn_OpenClosePort")

        self.text_Receive = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_Receive.setGeometry(QtCore.QRect(10, 70, 941, 301))
        self.text_Receive.setObjectName("text_Receive")

        self.text_Send = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Send.setGeometry(QtCore.QRect(10, 380, 941, 301))
        self.text_Send.setObjectName("text_Send")

        self.comboBox_BaudRate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_BaudRate.setGeometry(QtCore.QRect(970, 90, 121, 31))
        self.comboBox_BaudRate.setObjectName("comboBox_BaudRate")

        self.comboBox_DataSize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_DataSize.setGeometry(QtCore.QRect(970, 170, 121, 31))
        self.comboBox_DataSize.setObjectName("comboBox_DataSize")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(970, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(970, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(970, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox_Parity = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Parity.setGeometry(QtCore.QRect(970, 250, 121, 31))
        self.comboBox_Parity.setObjectName("comboBox_Parity")

        self.checkBox_CR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_CR.setGeometry(QtCore.QRect(970, 680, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_CR.setFont(font)
        self.checkBox_CR.setObjectName("checkBox_CR")

        self.checkBox_LF = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_LF.setGeometry(QtCore.QRect(970, 710, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_LF.setFont(font)
        self.checkBox_LF.setObjectName("checkBox_LF")

        self.btn_Send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Send.setGeometry(QtCore.QRect(10, 690, 941, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Send.setFont(font)
        self.btn_Send.setObjectName("btn_Send")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_OpenClosePort.setText(_translate("MainWindow", "Open"))
        self.label_3.setText(_translate("MainWindow", "Baudrate"))
        self.label_4.setText(_translate("MainWindow", "Data Size"))
        self.label_5.setText(_translate("MainWindow", "Parity"))
        self.checkBox_CR.setText(_translate("MainWindow", "+CR"))
        self.checkBox_LF.setText(_translate("MainWindow", "+LF"))
        self.btn_Send.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
