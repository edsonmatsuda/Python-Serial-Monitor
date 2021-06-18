from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
import serial
import glob
import io

global serialPort
global openFlag

openFlag = False

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
        self.comboBox_ComPort.setGeometry(QtCore.QRect(290, 10, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ComPort.setFont(font)
        self.comboBox_ComPort.setObjectName("comboBox_ComPort")

        # Button to Open/Close the ComPort communication
        self.btn_OpenClosePort = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenClosePort.setGeometry(QtCore.QRect(640, 10, 131, 41))
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
        self.btn_Send.setDisabled(True)

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

        self.timer = QTimer()
        self.timer.timeout.connect(self.receiveData)

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

        # Connect the click event to the button Open
        self.btn_OpenClosePort.clicked.connect(self.openClicked)

        # Connect the click event to the button Send
        self.btn_Send.clicked.connect(self.sendClicked)

        # Check which ComPorts are available
        for x in self.serial_ports():
            self.comboBox_ComPort.addItem(x)

    # Function when button Open is clicked
    def openClicked(self):
        global openFlag
        global serialPort

        if openFlag == False:
            getComPort = self.comboBox_ComPort.currentText()
            getBaudRate = int(self.comboBox_BaudRate.currentText())
            getDataSize = int(self.comboBox_DataSize.currentText())
            getParity = self.comboBox_Parity.currentText()
            if getParity == "":
                par = "N"
            elif getParity == "Odd":
                par = "O"
            else:
                par = "E"
            serialPort = serial.Serial(port=getComPort, baudrate=getBaudRate, bytesize=getDataSize, parity=par)

            self.timer.start(500)

            # Disable the ComboBoxes
            self.comboBox_ComPort.setDisabled(True)
            self.comboBox_BaudRate.setDisabled(True)
            self.comboBox_DataSize.setDisabled(True)
            self.comboBox_Parity.setDisabled(True)

            # Enable the Send button
            self.btn_Send.setDisabled(False)

            self.btn_OpenClosePort.setText("Close")

            openFlag = True

        else:
            self.timer.stop()
            serialPort.close()
            # Enable the ComboBoxes
            self.comboBox_ComPort.setDisabled(False)
            self.comboBox_BaudRate.setDisabled(False)
            self.comboBox_DataSize.setDisabled(False)
            self.comboBox_Parity.setDisabled(False)

            # Disable the Send button
            self.btn_Send.setDisabled(True)

            self.btn_OpenClosePort.setText("Open")

            openFlag = False


    # Function when button Send is clicked
    def sendClicked(self):
        mytext = self.text_Send.toPlainText()

        if self.checkBox_CR.isChecked() and not self.checkBox_LF.isChecked():
            serialPort.write(mytext.encode())
            serialPort.write(b'\r')
        elif not self.checkBox_CR.isChecked() and self.checkBox_LF.isChecked():
            serialPort.write(mytext.encode())
            serialPort.write(b'\n')
        elif self.checkBox_CR.isChecked() or self.checkBox_LF.isChecked():
            serialPort.write(mytext.encode())
            serialPort.write(b'\r\n')
        else:
            serialPort.write(mytext.encode())


    # Function to show the ComPorts available
    def serial_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    # Function to receive the data
    def receiveData(self):
        if (serialPort.in_waiting > 0):
            #serialString = serialPort.read()
            #print(str(serialString).split("'"))
            serialString = serialPort.readline()
            self.text_Receive.append(str(serialString)[2:-1])

            #serialString = serialPort.readline()
            #self.text_Receive.append(serialString.decode('Ascii'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())