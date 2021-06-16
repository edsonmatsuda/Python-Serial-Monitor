from PyQt5 import QtCore, QtGui, QtWidgets
import serial

global serialPort
#serialPort = serial.Serial(port="COM10", baudrate=115200)

# Used to store data coming over UART
global serialString
serialString = ""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ComboBox to ComPort
        self.comboBox_ComPort = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ComPort.setGeometry(QtCore.QRect(190, 10, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ComPort.setFont(font)
        self.comboBox_ComPort.setObjectName("comboBox_ComPort")

        # Button to Open/Close the ComPort communication
        self.btn_OpenClosePort = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenClosePort.setGeometry(QtCore.QRect(740, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_OpenClosePort.setFont(font)
        self.btn_OpenClosePort.setObjectName("btn_OpenClosePort")

        # ComboBox to Baud Rate
        self.comboBox_BaudRate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_BaudRate.setGeometry(QtCore.QRect(970, 90, 121, 31))
        self.comboBox_BaudRate.setObjectName("comboBox_BaudRate")
        self.comboBox_BaudRate.addItem("1200")
        self.comboBox_BaudRate.addItem("2400")
        self.comboBox_BaudRate.addItem("4800")
        self.comboBox_BaudRate.addItem("9600")
        self.comboBox_BaudRate.addItem("57600")
        self.comboBox_BaudRate.addItem("115200")
        self.comboBox_BaudRate.setCurrentIndex(3)

        # ComboBox to Data Size
        self.comboBox_DataSize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_DataSize.setGeometry(QtCore.QRect(970, 170, 121, 31))
        self.comboBox_DataSize.setObjectName("comboBox_DataSize")
        self.comboBox_DataSize.addItem("7")
        self.comboBox_DataSize.addItem("8")
        self.comboBox_DataSize.setCurrentIndex(1)

        # ComboBox to Parity
        self.comboBox_Parity = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Parity.setGeometry(QtCore.QRect(970, 250, 121, 31))
        self.comboBox_Parity.setObjectName("comboBox_Parity")
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.addItem("Odd")
        self.comboBox_Parity.addItem("Even")
        self.comboBox_Parity.setCurrentIndex(0)

        # Button to Send the data
        self.btn_Send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Send.setGeometry(QtCore.QRect(10, 690, 941, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Send.setFont(font)
        self.btn_Send.setObjectName("btn_Send")

        # Field to receive the data
        self.text_Receive = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_Receive.setGeometry(QtCore.QRect(10, 70, 941, 301))
        self.text_Receive.setObjectName("text_Receive")

        # Field to send the data
        self.text_Send = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Send.setGeometry(QtCore.QRect(10, 380, 941, 301))
        self.text_Send.setObjectName("text_Send")

        # CheckBox to Carriage Return
        self.checkBox_CR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_CR.setGeometry(QtCore.QRect(970, 680, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_CR.setFont(font)
        self.checkBox_CR.setObjectName("checkBox_CR")

        # CheckBox to New Line
        self.checkBox_LF = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_LF.setGeometry(QtCore.QRect(970, 710, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_LF.setFont(font)
        self.checkBox_LF.setObjectName("checkBox_LF")

        # Labels
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

        self.comboBox_ComPort.addItem("COM10")

        # Connect the click event to the button Send
        self.btn_Send.clicked.connect(self.sendClicked)



    # Function when button is clicked
    def sendClicked(self):
        mytext = self.text_Send.toPlainText()
        serialPort.write(mytext.encode())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
