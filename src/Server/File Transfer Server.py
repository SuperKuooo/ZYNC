import sys
import os
import threading
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmServerTerminal(object):
    def __init__(self, frmServerTerminal):
        self.setupUi(frmServerTerminal)
        # self.retranslateUi(frmServerTerminal)
        self.btn_clicked()
        self.menu_actions()
        # QtCore.QMetaObject.connectSlotsByName(frmServerTerminal)

    def setupUi(self, frmServerTerminal):
        frmServerTerminal.setObjectName("frmServerTerminal")
        frmServerTerminal.setEnabled(True)
        frmServerTerminal.resize(823, 464)
        frmServerTerminal.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(frmServerTerminal)
        self.centralwidget.setObjectName("centralwidget")
        self.txtStatusUpdate = QtWidgets.QTextEdit(self.centralwidget)
        self.txtStatusUpdate.setGeometry(QtCore.QRect(10, 300, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtStatusUpdate.setFont(font)
        self.txtStatusUpdate.setReadOnly(True)
        self.txtStatusUpdate.setObjectName("txtStatusUpdate")
        self.lblStatusLog = QtWidgets.QLabel(self.centralwidget)
        self.lblStatusLog.setGeometry(QtCore.QRect(10, 275, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblStatusLog.setFont(font)
        self.lblStatusLog.setObjectName("lblStatusLog")
        self.txtDetails = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDetails.setGeometry(QtCore.QRect(570, 40, 241, 231))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtDetails.setFont(font)
        self.txtDetails.setReadOnly(True)
        self.txtDetails.setObjectName("txtDetails")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 275, 721, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 541, 231))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstListOfConn = QtWidgets.QListWidget(self.widget)
        self.lstListOfConn.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.lstListOfConn.setObjectName("lstListOfConn")
        self.verticalLayout.addWidget(self.lstListOfConn)
        self.btnKick = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnKick.setFont(font)
        self.btnKick.setObjectName("btnKick")
        self.verticalLayout.addWidget(self.btnKick)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstTargetDirs = QtWidgets.QListWidget(self.widget)
        self.lstTargetDirs.setDragEnabled(True)
        self.lstTargetDirs.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.lstTargetDirs.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectItems)
        self.lstTargetDirs.setObjectName("lstTargetDirs")
        self.verticalLayout_2.addWidget(self.lstTargetDirs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnRemove = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnRemove.setFont(font)
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout.addWidget(self.btnRemove)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 641, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblListOfConnection = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblListOfConnection.setFont(font)
        self.lblListOfConnection.setObjectName("lblListOfConnection")
        self.horizontalLayout_3.addWidget(self.lblListOfConnection)
        spacerItem = QtWidgets.QSpacerItem(
            138, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblTargetDirectories = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblTargetDirectories.setFont(font)
        self.lblTargetDirectories.setObjectName("lblTargetDirectories")
        self.horizontalLayout_3.addWidget(self.lblTargetDirectories)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lblDetails = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.horizontalLayout_3.addWidget(self.lblDetails)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(570, 300, 241, 131))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnStartServer = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(22)
        self.btnStartServer.setFont(font)
        self.btnStartServer.setAutoFillBackground(False)
        self.btnStartServer.setObjectName("btnStartServer")
        self.verticalLayout_4.addWidget(self.btnStartServer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblInputIP = QtWidgets.QLabel(self.widget2)
        self.lblInputIP.setObjectName("lblInputIP")
        self.horizontalLayout_5.addWidget(self.lblInputIP)
        spacerItem2 = QtWidgets.QSpacerItem(
            38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.linInputIP = QtWidgets.QLineEdit(self.widget2)
        self.linInputIP.setObjectName("linInputIP")
        self.horizontalLayout_5.addWidget(self.linInputIP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPort = QtWidgets.QLabel(self.widget2)
        self.lblPort.setObjectName("lblPort")
        self.horizontalLayout_4.addWidget(self.lblPort)
        spacerItem3 = QtWidgets.QSpacerItem(
            28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.linPort = QtWidgets.QLineEdit(self.widget2)
        self.linPort.setObjectName("linPort")
        self.horizontalLayout_4.addWidget(self.linPort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        frmServerTerminal.setCentralWidget(self.centralwidget)
        self.mnuBar = QtWidgets.QMenuBar(frmServerTerminal)
        self.mnuBar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.mnuBar.setObjectName("mnuBar")
        self.mnuFile = QtWidgets.QMenu(self.mnuBar)
        self.mnuFile.setObjectName("mnuFile")
        self.menuSettings = QtWidgets.QMenu(self.mnuBar)
        self.menuSettings.setObjectName("menuSettings")
        frmServerTerminal.setMenuBar(self.mnuBar)
        self.actionHelp = QtWidgets.QAction(frmServerTerminal)
        self.actionHelp.setObjectName("actionHelp")
        self.actionReset = QtWidgets.QAction(frmServerTerminal)
        self.actionReset.setObjectName("actionReset")
        self.actionClose = QtWidgets.QAction(frmServerTerminal)
        self.actionClose.setObjectName("actionClose")
        self.actionSettigns = QtWidgets.QAction(frmServerTerminal)
        self.actionSettigns.setObjectName("actionSettigns")
        self.actionReconnection = QtWidgets.QAction(frmServerTerminal)
        self.actionReconnection.setObjectName("actionReconnection")
        self.actionAuto_Sleep = QtWidgets.QAction(frmServerTerminal)
        self.actionAuto_Sleep.setObjectName("actionAuto_Sleep")
        self.actionClear_Log = QtWidgets.QAction(frmServerTerminal)
        self.actionClear_Log.setObjectName("actionClear_Log")
        self.actionBase_Path = QtWidgets.QAction(frmServerTerminal)
        self.actionBase_Path.setObjectName("actionBase_Path")
        self.mnuFile.addAction(self.actionClear_Log)
        self.mnuFile.addAction(self.actionReset)
        self.mnuFile.addAction(self.actionHelp)
        self.mnuFile.addAction(self.actionClose)
        self.menuSettings.addAction(self.actionBase_Path)
        self.menuSettings.addAction(self.actionReconnection)
        self.menuSettings.addAction(self.actionAuto_Sleep)
        self.mnuBar.addAction(self.mnuFile.menuAction())
        self.mnuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(frmServerTerminal)
        self.lstTargetDirs.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(frmServerTerminal)

    def retranslateUi(self, frmServerTerminal):
        _translate = QtCore.QCoreApplication.translate
        frmServerTerminal.setWindowTitle(_translate(
            "frmServerTerminal", "Server Terminal"))
        self.lblStatusLog.setText(_translate(
            "frmServerTerminal", "Status Log:"))
        self.btnKick.setText(_translate("frmServerTerminal", "KICK"))
        self.btnBrowse.setText(_translate("frmServerTerminal", "BROWSE"))
        self.btnRemove.setText(_translate("frmServerTerminal", "REMOVE"))
        self.lblListOfConnection.setText(_translate(
            "frmServerTerminal", "List of Connections"))
        self.lblTargetDirectories.setText(_translate(
            "frmServerTerminal", "Target Directories"))
        self.lblDetails.setText(_translate(
            "frmServerTerminal", "Item Details"))
        self.btnStartServer.setText(_translate("frmServerTerminal", "START"))
        self.lblInputIP.setText(_translate("frmServerTerminal", "IP Address"))
        self.linInputIP.setText(_translate(
            "frmServerTerminal", "192.168.1.118"))
        self.lblPort.setText(_translate("frmServerTerminal", "Port Number"))
        self.linPort.setText(_translate("frmServerTerminal", "8000"))
        self.mnuFile.setTitle(_translate("frmServerTerminal", "File"))
        self.menuSettings.setTitle(_translate("frmServerTerminal", "Settings"))
        self.actionHelp.setText(_translate("frmServerTerminal", "Help"))
        self.actionReset.setText(_translate("frmServerTerminal", "Reset"))
        self.actionClose.setText(_translate("frmServerTerminal", "Close"))
        self.actionSettigns.setText(
            _translate("frmServerTerminal", "Settings"))
        self.actionReconnection.setText(
            _translate("frmServerTerminal", "Reconnection"))
        self.actionAuto_Sleep.setText(
            _translate("frmServerTerminal", "Auto Sleep"))
        self.actionClear_Log.setText(_translate(
            "frmServerTerminal", "Clear Status Log"))
        self.actionBase_Path.setText(
            _translate("frmServerTerminal", "Base Path"))

    def menu_actions(self):
        self.actionClear_Log.triggered.connect(self.menu_clear_log)
        self.actionBase_Path.triggered.connect(self.menu_Base_Path)
        self.actionReset.triggered.connect(self.menu_reset)

    def btn_clicked(self):
        self.btnStartServer.clicked.connect(self.set_server_for_ui)
        self.btnBrowse.clicked.connect(self.browse_directory)
        self.btnRemove.clicked.connect(self.remove_directory)

    def remove_directory(self):
        row = self.lstTargetDirs.currentRow()
        if row < 0:
            return
        item = self.lstTargetDirs.takeItem(row)
        self.txtStatusUpdate.append('Deleted ' + item.text())
        del item

    def add_connection(self, name):
        row = self.lstListOfConn.currentRow()
        self.lstListOfConn.insertItem(row, name)

    def browse_directory(self):
        global server
        if not server:
            self.txtStatusUpdate.append(
                "No server set yet. Please set a server before adding a directory.")
            return 1
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a Directory', LIB_PATH, QtWidgets.QFileDialog.ShowDirsOnly)
        if dir_name:
            obs = sw.Observer(server, LIB_PATH, TARGET_PATH)
            self.txtStatusUpdate.append('Folder selected: ' + dir_name)
            server.set_list_of_observer(obs)
            self.refresh_directory()

    def set_server_for_ui(self):
        global server, RUN

        try:
            input_ip = self.linInputIP.text()
            input_port = int(self.linPort.text())
        except ValueError:
            self.txtStatusUpdate.append('Error: Bad Input')
            return
        self.txtStatusUpdate.append('Initializing Server...')
        server = sw.Server()
        if server.set_server_connection(input_ip, input_port, 3) == 1:
            self.txtStatusUpdate.append("Error: Failed to start server")
            return 1
        RUN = True
        self.txtStatusUpdate.append(
            "Server set at IP: " + str(input_ip) + " Port: " + str(input_port))
        self.btnStartServer.setDisabled(True)
        self.btnStartServer.setText('Server On')

        t1.start()
        t3.start()

    def menu_reset(self):
        global server, RUN

        box = QtWidgets.QMessageBox()
        box.setText('Are you sure to reset connection?')
        box.setStandardButtons(QtWidgets.QMessageBox.Ok |
                               QtWidgets.QMessageBox.Cancel)
        retval = box.exec_()
        if not server:
            self.txtStatusUpdate.append('Note: No server to reset')
            return 1

        if retval == QtWidgets.QMessageBox.Ok:
            self.menu_clear_log()
            RUN = False
            server.close()
            t1.join()
            t3.join()
            server = None
            self.btnStartServer.setDisabled(False)
            self.btnStartServer.setText('START')

    def menu_Base_Path(self):
        global LIB_PATH

        temp = QtWidgets.QInputDialog.getText(
            None, 'Select Base Directory', 'Type the location of the directory', text=LIB_PATH)[0]
        if temp:
            self.txtStatusUpdate.append('New base directory at: ' + temp)
            LIB_PATH = temp
        else:
            self.txtStatusUpdate.append(
                'Note: Failed to change base directory')

    def menu_clear_log(self):
        self.txtStatusUpdate.clear()

    def refresh_directory(self):
        self.lstTargetDirs.clear()
        for observer in server.list_of_observer:
            row = self.lstTargetDirs.currentRow()
            self.lstTargetDirs.insertItem(row, observer.get_target_path())
        self.txtStatusUpdate.append(
            'Number of Directories: {}'.format(server.get_num_of_observer()))

    def refresh_list_of_conn(self):
        self.txtStatusUpdate.append(
            'Number of Connections: {}'.format(server.get_num_of_connection()))


def connection_loop():
    while RUN:
        try:
            server.listen(MAX_CONNECTION)
            conn, addr = server.accept()
        except OSError:
            return 1 # Terminating the server

        print("Connection Address:" + str(addr) +
              " " + str(datetime.datetime.now()))
        server.echo_connection(conn, conn.recv(BUFFER_SIZE))
        ui.add_connection(str(addr))
    return 0


def alive_message_loop():
    while RUN:
        if sw.check_connection(server.get_list_of_connection()):
            ui.txtStatusUpdate.append('Someone got kicked out')
        time.sleep(0.5)
    return 0


if __name__ == "__main__":
    sys.path.append(os.getcwd())
    import lib.socket_wrapper as sw
    server = None
    RUN = False
    LIB_PATH = 'C:/Users/user/Documents/Unity_Build_Library'
    TARGET_PATH = 'Univrse-Core/Windows'
    MAX_CONNECTION = 5
    BUFFER_SIZE = 4096

    t1 = threading.Thread(target=connection_loop, name='connection_loop')
    # t2 = threading.Thread(target=communication_loop, name='communication_loop')
    t3 = threading.Thread(target=alive_message_loop, name='alive_message_loop')

    app = QtWidgets.QApplication(sys.argv)
    ServerTerminal = QtWidgets.QMainWindow()
    ui = Ui_frmServerTerminal(ServerTerminal)
    ServerTerminal.show()

    sys.exit(app.exec_())
