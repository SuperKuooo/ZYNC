from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket_wrapper as sw
from Qt_thread_aux import ClientConnection as cc

# TODO(Jerry): July 24th, 2019
#  Standardize all messages. Right now, the titles are all different.


client = sw.Client()

class Ui_frmClient(object):
    def __init__(self, frmClientTerminal):
        self.auto_reconn = True

        self.connection = cc.ClientConnectionThread(client)
        self.connection.sig.connect(self.update_messages)

        self.setupUi(frmClientTerminal)
        self.retranslateUi(frmClientTerminal)
        self.button_clicked(frmClientTerminal)
        self.menu_actions()

    def setupUi(self, frmClientTerminal):
        frmClientTerminal.setObjectName("frmClientTerminal")
        frmClientTerminal.resize(823, 464)
        self.centralwidget = QtWidgets.QWidget(frmClientTerminal)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 641, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblListOfConnection = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblListOfConnection.setFont(font)
        self.lblListOfConnection.setObjectName("lblListOfConnection")
        self.horizontalLayout_11.addWidget(self.lblListOfConnection)
        spacerItem = QtWidgets.QSpacerItem(
            138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.lblDetails = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.horizontalLayout_11.addWidget(self.lblDetails)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 265, 721, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(570, 290, 241, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnStartClient = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(22)
        self.btnStartClient.setFont(font)
        self.btnStartClient.setAutoFillBackground(False)
        self.btnStartClient.setObjectName("btnStartClient")
        self.verticalLayout_9.addWidget(self.btnStartClient)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblInputIP = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblInputIP.setObjectName("lblInputIP")
        self.horizontalLayout_12.addWidget(self.lblInputIP)
        spacerItem1 = QtWidgets.QSpacerItem(
            38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.linInputIP = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.linInputIP.setObjectName("linInputIP")
        self.horizontalLayout_12.addWidget(self.linInputIP)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblPort = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblPort.setObjectName("lblPort")
        self.horizontalLayout_13.addWidget(self.lblPort)
        spacerItem2 = QtWidgets.QSpacerItem(
            28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.linPort = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.linPort.setObjectName("linPort")
        self.horizontalLayout_13.addWidget(self.linPort)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.txtDetails = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDetails.setGeometry(QtCore.QRect(570, 30, 241, 231))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtDetails.setFont(font)
        self.txtDetails.setReadOnly(True)
        self.txtDetails.setObjectName("txtDetails")
        self.lblStatusLog = QtWidgets.QLabel(self.centralwidget)
        self.lblStatusLog.setGeometry(QtCore.QRect(10, 265, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblStatusLog.setFont(font)
        self.lblStatusLog.setObjectName("lblStatusLog")
        self.txtStatusUpdate = QtWidgets.QTextEdit(self.centralwidget)
        self.txtStatusUpdate.setGeometry(QtCore.QRect(10, 290, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtStatusUpdate.setFont(font)
        self.txtStatusUpdate.setReadOnly(True)
        self.txtStatusUpdate.setObjectName("txtStatusUpdate")
        self.lstTransferredFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lstTransferredFiles.setGeometry(QtCore.QRect(12, 32, 541, 231))
        self.lstTransferredFiles.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.lstTransferredFiles.setObjectName("lstTransferredFiles")
        frmClientTerminal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmClientTerminal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        frmClientTerminal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmClientTerminal)
        self.statusbar.setObjectName("statusbar")
        frmClientTerminal.setStatusBar(self.statusbar)
        self.actionAuto_Reconnect = QtWidgets.QAction(frmClientTerminal)
        self.actionAuto_Reconnect.setObjectName("actionAuto_Reconnect")
        self.actionTimeout = QtWidgets.QAction(frmClientTerminal)
        self.actionTimeout.setObjectName("actionTimeout")
        self.actionReconnect_Time = QtWidgets.QAction(frmClientTerminal)
        self.actionReconnect_Time.setObjectName("actionReconnect_Time")
        self.actionHelp = QtWidgets.QAction(frmClientTerminal)
        self.actionHelp.setObjectName("actionHelp")
        self.actionClose = QtWidgets.QAction(frmClientTerminal)
        self.actionClose.setObjectName("actionClose")
        self.actionReset = QtWidgets.QAction(frmClientTerminal)
        self.actionReset.setObjectName("actionReset")
        self.actionSave_Directory = QtWidgets.QAction(frmClientTerminal)
        self.actionSave_Directory.setObjectName("actionSave_Directory")
        self.actionSave_Log = QtWidgets.QAction(frmClientTerminal)
        self.actionSave_Log.setObjectName("actionSave_Log")
        self.menuFile.addAction(self.actionSave_Log)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionHelp)
        self.menuSettings.addAction(self.actionAuto_Reconnect)
        self.menuSettings.addAction(self.actionReconnect_Time)
        self.menuSettings.addAction(self.actionTimeout)
        self.menuSettings.addAction(self.actionSave_Directory)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(frmClientTerminal)
        QtCore.QMetaObject.connectSlotsByName(frmClientTerminal)

    def retranslateUi(self, frmClientTerminal):
        _translate = QtCore.QCoreApplication.translate
        frmClientTerminal.setWindowTitle(_translate(
            "frmClientTerminal", "Client Terminal"))
        self.lblListOfConnection.setText(_translate(
            "frmClientTerminal", "Transferred Files"))
        self.lblDetails.setText(_translate(
            "frmClientTerminal", "Item Details"))
        self.btnStartClient.setText(_translate("frmClientTerminal", "START"))
        self.lblInputIP.setText(_translate("frmClientTerminal", "IP Address"))
        self.linInputIP.setText(_translate(
            "frmClientTerminal", "192.168.1.118"))
        self.lblPort.setText(_translate("frmClientTerminal", "Port Number"))
        self.linPort.setText(_translate("frmClientTerminal", "8000"))
        self.lblStatusLog.setText(_translate(
            "frmClientTerminal", "Status Log:"))
        self.menuFile.setTitle(_translate("frmClientTerminal", "File"))
        self.menuSettings.setTitle(_translate("frmClientTerminal", "Settings"))
        self.actionAuto_Reconnect.setText(
            _translate("frmClientTerminal", "Auto Reconnect"))
        self.actionTimeout.setText(_translate("frmClientTerminal", "Timeout"))
        self.actionReconnect_Time.setText(
            _translate("frmClientTerminal", "Reconnect Time"))
        self.actionHelp.setText(_translate("frmClientTerminal", "Help"))
        self.actionClose.setText(_translate("frmClientTerminal", "Close"))
        self.actionReset.setText(_translate("frmClientTerminal", "Reset"))
        self.actionSave_Directory.setText(
            _translate("frmClientTerminal", "Save Location"))
        self.actionSave_Log.setText(
            _translate("frmClientTerminal", "Save Log"))

    def button_clicked(self, frmClientTerminal):
        frmClientTerminal.closeEvent = self.close_gui
        self.btnStartClient.clicked.connect(self.set_client_for_ui)

    def menu_actions(self):
        self.actionAuto_Reconnect.triggered.connect(self.auto_reconnect)
        self.actionSave_Directory.triggered.connect(self.change_save_location)
        # self.actionReset.triggered.hconnect(partial(self.reset_client, True))

    def auto_reconnect(self):
        box = QtWidgets.QMessageBox()
        box.setText('Do you want the client to auto reconnect?')
        box.setWindowTitle('Set Auto Connect')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes |
                               QtWidgets.QMessageBox.No)
        box.setIcon(QtWidgets.QMessageBox.Question)

        retval = box.exec_()
        if retval == QtWidgets.QMessageBox.Yes:
            self.auto_reconn = True
        else:
            self.auto_reconn = False

    def change_save_location(self):
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a Directory')

        if dir_name:
            self.txtStatusUpdate.append(
                'Save location changed to: ' + dir_name)

    def close_gui(self, e):
        global client

        client = None
        return self.connection.end()

    def update_messages(self):
        global client

        if not self.connection.get_messages():
            return 1
        for message in self.connection.get_messages():
            splt_message = message.split()
            if splt_message[0] == 'RESET':
                print('Connection Lost')
                self.connection.pause_communication()
                self.set_client_for_ui()
                break
            elif splt_message[0] == 'BUTTON':
                self.btnStartClient.setText(splt_message[1])
                continue
            elif splt_message[0] == 'FILE':
                # TODO(Jerry): July 22, 2019
                # Find the right name for splt message
                row = self.lstTransferredFiles.currentRow()
                self.lstTransferredFiles.insertItem(row, splt_message[1])

            self.txtStatusUpdate.append(message)
        self.connection.set_messages()

    def set_client_for_ui(self):
        global client

        self.txtStatusUpdate.append(sw.time_stamp(
            dates=False) + 'Initializing client...')
        try:
            input_ip = self.linInputIP.text()
            input_port = int(self.linPort.text())
            self.connection.set_ip_port(input_ip, input_port)
        except ValueError:
            self.txtStatusUpdate.append(
                sw.time_stamp(dates=False) + 'Error: Bad Input')
            return 1

        self.txtStatusUpdate.append(sw.time_stamp(
            dates=False) + 'Attempting to connect to server')
        self.txtStatusUpdate.append(sw.time_stamp(
            dates=False) + 'Do not close window')

        self.btnStartClient.setDisabled(True)
        self.btnStartClient.setText('Connecting')
        self.linInputIP.setDisabled(True)
        self.linPort.setDisabled(True)

        self.connection.start_connection()
        self.connection.resume_connection()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ClientTerminal = QtWidgets.QMainWindow()
    ui = Ui_frmClient(ClientTerminal)

    ClientTerminal.show()
    sys.exit(app.exec_())
