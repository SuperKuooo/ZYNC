import sys
import socket_wrapper as sw
from Qt_thread_aux.ServerConnection import ServerConnectionThread
from PyQt5 import QtCore, QtGui, QtWidgets

server = sw.Server()
current_row = None
LIB_PATH = 'C:/Users/user/Documents/Unity_Build_Library'


class UiFrmServerTerminal(object):
    def __init__(self, frm_server_terminal):
        # Declaring variables
        self.connection = ServerConnectionThread(server)
        self.connection.set_sig(self.refresh_list_of_conn)
        self.connection.start()

        self.setupUi(frm_server_terminal)
        # self.retranslateUi(frmServerTerminal)
        self.other_settings(frm_server_terminal)
        # QtCore.QMetaObject.connectSlotsByName(frmServerTerminal)

        # bind actions
        self.clicked_binding(frm_server_terminal)
        self.menu_actions()

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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 275, 721, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 300, 251, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnStartServer = QtWidgets.QPushButton(self.layoutWidget)
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
        self.lblInputIP = QtWidgets.QLabel(self.layoutWidget)
        self.lblInputIP.setObjectName("lblInputIP")
        self.horizontalLayout_5.addWidget(self.lblInputIP)
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.linInputIP = QtWidgets.QLineEdit(self.layoutWidget)
        self.linInputIP.setObjectName("linInputIP")
        self.horizontalLayout_5.addWidget(self.linInputIP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPort = QtWidgets.QLabel(self.layoutWidget)
        self.lblPort.setObjectName("lblPort")
        self.horizontalLayout_4.addWidget(self.lblPort)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.linPort = QtWidgets.QLineEdit(self.layoutWidget)
        self.linPort.setObjectName("linPort")
        self.horizontalLayout_4.addWidget(self.linPort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.txtDetails = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDetails.setGeometry(QtCore.QRect(560, 40, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtDetails.setFont(font)
        self.txtDetails.setReadOnly(True)
        self.txtDetails.setObjectName("txtDetails")
        self.gpbOptions = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbOptions.setEnabled(False)
        self.gpbOptions.setGeometry(QtCore.QRect(560, 190, 251, 81))
        self.gpbOptions.setObjectName("gpbOptions")
        self.rdbTimed = QtWidgets.QRadioButton(self.gpbOptions)
        self.rdbTimed.setGeometry(QtCore.QRect(30, 20, 82, 17))
        self.rdbTimed.setObjectName("rdbTimed")
        self.rdbChanged = QtWidgets.QRadioButton(self.gpbOptions)
        self.rdbChanged.setGeometry(QtCore.QRect(140, 20, 101, 17))
        self.rdbChanged.setObjectName("rdbChanged")
        self.spbxTimedSeconds = QtWidgets.QSpinBox(self.gpbOptions)
        self.spbxTimedSeconds.setGeometry(QtCore.QRect(31, 40, 71, 22))
        self.spbxTimedSeconds.setObjectName("spbxTimedSeconds")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(184, 40, 361, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstTargetDirs = QtWidgets.QListWidget(self.layoutWidget1)
        self.lstTargetDirs.setDragEnabled(True)
        self.lstTargetDirs.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lstTargetDirs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.lstTargetDirs.setObjectName("lstTargetDirs")
        self.verticalLayout_2.addWidget(self.lstTargetDirs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnRemove = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnRemove.setFont(font)
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout.addWidget(self.btnRemove)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(14, 42, 166, 229))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstListOfConn = QtWidgets.QListWidget(self.layoutWidget2)
        self.lstListOfConn.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstListOfConn.setObjectName("lstListOfConn")
        self.verticalLayout.addWidget(self.lstListOfConn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRefresh = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout_2.addWidget(self.btnRefresh)
        self.btnKick = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnKick.setFont(font)
        self.btnKick.setObjectName("btnKick")
        self.horizontalLayout_2.addWidget(self.btnKick)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(15, 10, 631, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblListOfConnection = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblListOfConnection.setFont(font)
        self.lblListOfConnection.setObjectName("lblListOfConnection")
        self.horizontalLayout_3.addWidget(self.lblListOfConnection)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lblTargetDirectories = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblTargetDirectories.setFont(font)
        self.lblTargetDirectories.setObjectName("lblTargetDirectories")
        self.horizontalLayout_3.addWidget(self.lblTargetDirectories)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.lblDetails = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.horizontalLayout_6.addWidget(self.lblDetails)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.btnConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirm.setGeometry(QtCore.QRect(700, 10, 113, 32))
        self.btnConfirm.setObjectName("btnConfirm")
        frmServerTerminal.setCentralWidget(self.centralwidget)
        self.mnuBar = QtWidgets.QMenuBar(frmServerTerminal)
        self.mnuBar.setGeometry(QtCore.QRect(0, 0, 823, 22))
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
        self.actionSave_Log = QtWidgets.QAction(frmServerTerminal)
        self.actionSave_Log.setObjectName("actionSave_Log")
        self.mnuFile.addAction(self.actionClear_Log)
        self.mnuFile.addAction(self.actionHelp)
        self.mnuFile.addAction(self.actionSave_Log)
        self.mnuFile.addAction(self.actionClose)
        self.menuSettings.addAction(self.actionBase_Path)
        self.menuSettings.addAction(self.actionReconnection)
        self.mnuBar.addAction(self.mnuFile.menuAction())
        self.mnuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(frmServerTerminal)
        self.lstTargetDirs.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(frmServerTerminal)

    def retranslateUi(self, frmServerTerminal):
        _translate = QtCore.QCoreApplication.translate
        frmServerTerminal.setWindowTitle(_translate("frmServerTerminal", "Server Terminal"))
        self.lblStatusLog.setText(_translate("frmServerTerminal", "Status Log:"))
        self.btnStartServer.setText(_translate("frmServerTerminal", "START"))
        self.btnStartServer.setShortcut(_translate("frmServerTerminal", "Enter"))
        self.lblInputIP.setText(_translate("frmServerTerminal", "IP Address"))
        self.linInputIP.setText(_translate("frmServerTerminal", "192.168.1.118"))
        self.lblPort.setText(_translate("frmServerTerminal", "Port Number"))
        self.linPort.setText(_translate("frmServerTerminal", "8000"))
        self.gpbOptions.setTitle(_translate("frmServerTerminal", "Trigger Options"))
        self.rdbTimed.setText(_translate("frmServerTerminal", "Time Based"))
        self.rdbChanged.setText(_translate("frmServerTerminal", "Change Based"))
        self.btnBrowse.setText(_translate("frmServerTerminal", "BROWSE"))
        self.btnBrowse.setShortcut(_translate("frmServerTerminal", "."))
        self.btnRemove.setText(_translate("frmServerTerminal", "REMOVE"))
        self.btnRemove.setShortcut(_translate("frmServerTerminal", "Del"))
        self.btnRefresh.setText(_translate("frmServerTerminal", "REFRESH"))
        self.btnRefresh.setShortcut(_translate("frmServerTerminal", "R"))
        self.btnKick.setText(_translate("frmServerTerminal", "KICK"))
        self.lblListOfConnection.setText(_translate("frmServerTerminal", "List of Connections"))
        self.lblTargetDirectories.setText(_translate("frmServerTerminal", "Target Directories"))
        self.lblDetails.setText(_translate("frmServerTerminal", "Item Details"))
        self.btnConfirm.setText(_translate("frmServerTerminal", "CONFIRM"))
        self.mnuFile.setTitle(_translate("frmServerTerminal", "File"))
        self.menuSettings.setTitle(_translate("frmServerTerminal", "Settings"))
        self.actionHelp.setText(_translate("frmServerTerminal", "Help"))
        self.actionReset.setText(_translate("frmServerTerminal", "Reset"))
        self.actionClose.setText(_translate("frmServerTerminal", "Close"))
        self.actionSettigns.setText(_translate("frmServerTerminal", "Settings"))
        self.actionReconnection.setText(_translate("frmServerTerminal", "Reconnection"))
        self.actionAuto_Sleep.setText(_translate("frmServerTerminal", "Auto Sleep"))
        self.actionClear_Log.setText(_translate("frmServerTerminal", "Clear Status Log"))
        self.actionBase_Path.setText(_translate("frmServerTerminal", "Base Path"))
        self.actionSave_Log.setText(_translate("frmServerTerminal", "Save Log"))

    # For settings that I can't find in PyQt GUI designer
    def other_settings(self, frm_server_terminal):
        frm_server_terminal.setFixedSize(823, 464)

    def menu_actions(self):
        self.actionClear_Log.triggered.connect(self.menu_clear_log)
        self.actionBase_Path.triggered.connect(self.menu_base_path)
        self.actionClose.triggered.connect(self.exit)
        self.actionHelp.triggered.connect(self.help_menu)
        self.actionSave_Log.triggered.connect(self.save_log)

    def clicked_binding(self, frm_server_terminal):
        # Form
        frm_server_terminal.closeEvent = self.close_gui

        # Buttons
        self.btnStartServer.clicked.connect(self.set_server_for_ui)
        self.btnBrowse.clicked.connect(self.browse_directory)
        self.btnRemove.clicked.connect(self.remove_directory)
        self.btnRefresh.clicked.connect(self.refresh_list_of_conn)
        self.btnKick.clicked.connect(self.kick_connection)
        self.btnConfirm.clicked.connect(self.confirm_detection_method)

        # Lists
        self.lstTargetDirs.clicked.connect(self.directory_details)
        self.lstListOfConn.clicked.connect(self.conn_details)

        # Radio Buttons
        self.rdbChanged.toggled.connect(self.change_detection_method)

    def save_log(self):
        # TODO(Jerry): Add feature
        print('Save Log')
        print('I have not implemented the help menu yet lmao')
        print('Go on github to ask questions. Sorry. :P')
        print('Or you could email me at jerrykuo820@gmail.com')
        print('I will try to update this as I go along')
        print('~~~~~~~~~~~')

    def help_menu(self):
        # TODO(Jerry): Add feature
        print('Help Menu')
        print('I have not implemented the help menu yet lmao')
        print('Go on github to ask questions. Sorry. :P')
        print('Or you could email me at jerrykuo820@gmail.com')
        print('I will try to update this as I go along')
        print('~~~~~~~~~~~')

    def exit(self):
        self.close_gui(self, )
        sys.exit(0)

    def close_gui(self, e):
        server.close()
        self.connection.end()

    def confirm_detection_method(self):
        global current_row
        observer = server.get_list_of_observer(current_row)
        if observer.get_mode() == 0:
            observer.resume()

        self.gpbOptions.setDisabled(True)
        self.btnConfirm.setDisabled(True)

    # This require tremendous amount of effort to do actually. Because of how I designed it.
    # TODO: Big feature. Not yet implemented.
    def change_detection_method(self):
        global current_row
        observer = server.get_list_of_observer(current_row)

        # 0 is change based, 1 is time based
        if observer.get_mode() == 0:
            observer.set_mode(1)
            self.spbxTimedSeconds.setDisabled(True)

        elif observer.get_mode() == 1:
            observer.set_mode(0)
            self.spbxTimedSeconds.setDisabled(False)
        else:
            print('Error: Not implemented yet')
        return 0

    def directory_details(self):
        global current_row
        current_row = self.lstTargetDirs.currentRow()
        self.txtDetails.clear()
        observer = server.get_list_of_observer(current_row)
        mode = observer.get_mode()
        details = observer.handler.get_details()
        self.gpbOptions.setDisabled(False)
        self.btnConfirm.setDisabled(False)
        if mode == 0:
            self.rdbChanged.toggle()
        elif mode == 1:
            self.rdbTimed.toggle()
        self.txtDetails.append('{:25s}{}'.format('Track Mode:', 'Changes'))
        self.txtDetails.append('{:25s}{}'.format('Last Success:', details[0]))
        self.txtDetails.append('{:25s}{}'.format('Last Attempt:', details[1]))
        self.txtDetails.append('{:25s}{}'.format('Total Attempts:', details[2]))
        self.txtDetails.append('{:25s}{}'.format('Archive Directory:', details[3]))

    # TODO: Show connection details
    def conn_details(self):
        pass

    def kick_connection(self):
        # TODO: need to take a look at this. Cannot kick right now
        row = self.lstListOfConn.currentRow()
        server.set_list_of_connection(operation=2, index=row)
        self.refresh_list_of_conn()
        return 0

    def remove_directory(self):
        row = self.lstTargetDirs.currentRow()
        if row < 0:
            return 1
        item = self.lstTargetDirs.takeItem(row)
        server.set_list_of_observer(operation=2, index=row)
        self.txtStatusUpdate.append('Deleted ' + item.text())
        del item
        return 0

    def browse_directory(self):
        global server
        if not server:
            self.txtStatusUpdate.append(
                "Error: No server set yet. Please set a server before adding a directory.")
            return 1
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a Directory', LIB_PATH, QtWidgets.QFileDialog.ShowDirsOnly)
        if dir_name:
            self.txtStatusUpdate.append('Folder selected: ' + dir_name)
            obs = sw.Observer(server, LIB_PATH, dir_name)
            obs.start_observe()
            self.txtStatusUpdate.append(
                'Start observing on the directory: ' + dir_name)
            server.set_list_of_observer(obs)
            self.refresh_directory()

    def set_server_for_ui(self):
        global server
        self.txtStatusUpdate.append('Initializing Server...')
        try:
            input_ip = self.linInputIP.text()
            input_port = int(self.linPort.text())
        except ValueError:
            self.txtStatusUpdate.append('Error: Bad Input')
            return

        if server.set_server_connection(input_ip, input_port, 3) == 1:
            self.txtStatusUpdate.append("Error: Failed to start server")
            return 1

        self.txtStatusUpdate.append(
            "Server set at IP: " + str(input_ip) + " Port: " + str(input_port))
        self.btnStartServer.setDisabled(True)
        self.btnStartServer.setText('SERVER ON')
        self.linInputIP.setDisabled(True)
        self.linPort.setDisabled(True)

        self.connection.resume()

    def menu_base_path(self):
        global LIB_PATH

        temp = QtWidgets.QInputDialog.getText(
            None, 'Select Base Directory', 'Type the location of the directory', text=LIB_PATH)[0]
        if temp:
            self.txtStatusUpdate.append('New base directory at: ' + temp)
            LIB_PATH = temp
        else:
            self.txtStatusUpdate.append(
                'Error: Failed to change base directory')

    def menu_clear_log(self):
        return self.txtStatusUpdate.clear()

    def refresh_directory(self):
        self.lstTargetDirs.clear()
        if not server or not server.get_list_of_observer():
            return 1
        for observer in server.get_list_of_observer():
            row = self.lstTargetDirs.currentRow()
            self.lstTargetDirs.insertItem(row, observer.get_target_path())
        self.txtStatusUpdate.append(
            'Number of Directories: {}'.format(server.get_num_of_observer()))
        return 0

    def refresh_list_of_conn(self):
        self.lstListOfConn.clear()
        if not server or not server.get_list_of_connection():
            return 1
        for conn in server.get_list_of_connection():
            row = self.lstTargetDirs.currentRow()
            val = QtWidgets.QListWidgetItem(str(conn.getpeername()))
            val.setTextAlignment(QtCore.Qt.AlignCenter)
            self.lstListOfConn.insertItem(row, val)
        return 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ServerTerminal = QtWidgets.QMainWindow()
    ui = UiFrmServerTerminal(ServerTerminal)
    ServerTerminal.show()

    app.exec_()
    sys.exit(0)
