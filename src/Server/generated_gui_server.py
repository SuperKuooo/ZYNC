# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File Transfer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmServerTerminal(object):
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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 541, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstListOfConn = QtWidgets.QListWidget(self.layoutWidget)
        self.lstListOfConn.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstListOfConn.setObjectName("lstListOfConn")
        self.verticalLayout.addWidget(self.lstListOfConn)
        self.btnKick = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnKick.setFont(font)
        self.btnKick.setObjectName("btnKick")
        self.verticalLayout.addWidget(self.btnKick)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstTargetDirs = QtWidgets.QListWidget(self.layoutWidget)
        self.lstTargetDirs.setDragEnabled(True)
        self.lstTargetDirs.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lstTargetDirs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.lstTargetDirs.setObjectName("lstTargetDirs")
        self.verticalLayout_2.addWidget(self.lstTargetDirs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnRemove = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.btnRemove.setFont(font)
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout.addWidget(self.btnRemove)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 641, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblListOfConnection = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblListOfConnection.setFont(font)
        self.lblListOfConnection.setObjectName("lblListOfConnection")
        self.horizontalLayout_3.addWidget(self.lblListOfConnection)
        spacerItem = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblTargetDirectories = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblTargetDirectories.setFont(font)
        self.lblTargetDirectories.setObjectName("lblTargetDirectories")
        self.horizontalLayout_3.addWidget(self.lblTargetDirectories)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lblDetails = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.horizontalLayout_3.addWidget(self.lblDetails)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(570, 300, 241, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnStartServer = QtWidgets.QPushButton(self.layoutWidget2)
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
        self.lblInputIP = QtWidgets.QLabel(self.layoutWidget2)
        self.lblInputIP.setObjectName("lblInputIP")
        self.horizontalLayout_5.addWidget(self.lblInputIP)
        spacerItem2 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.linInputIP = QtWidgets.QLineEdit(self.layoutWidget2)
        self.linInputIP.setObjectName("linInputIP")
        self.horizontalLayout_5.addWidget(self.linInputIP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPort = QtWidgets.QLabel(self.layoutWidget2)
        self.lblPort.setObjectName("lblPort")
        self.horizontalLayout_4.addWidget(self.lblPort)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.linPort = QtWidgets.QLineEdit(self.layoutWidget2)
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
        frmServerTerminal.setWindowTitle(_translate("frmServerTerminal", "Server Terminal"))
        self.lblStatusLog.setText(_translate("frmServerTerminal", "Status Log:"))
        self.btnKick.setText(_translate("frmServerTerminal", "KICK"))
        self.btnBrowse.setText(_translate("frmServerTerminal", "BROWSE"))
        self.btnRemove.setText(_translate("frmServerTerminal", "REMOVE"))
        self.lblListOfConnection.setText(_translate("frmServerTerminal", "List of Connections"))
        self.lblTargetDirectories.setText(_translate("frmServerTerminal", "Target Directories"))
        self.lblDetails.setText(_translate("frmServerTerminal", "Item Details"))
        self.btnStartServer.setText(_translate("frmServerTerminal", "START"))
        self.lblInputIP.setText(_translate("frmServerTerminal", "IP Address"))
        self.linInputIP.setText(_translate("frmServerTerminal", "192.168.1.118"))
        self.lblPort.setText(_translate("frmServerTerminal", "Port Number"))
        self.linPort.setText(_translate("frmServerTerminal", "8000"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmServerTerminal = QtWidgets.QMainWindow()
    ui = Ui_frmServerTerminal()
    ui.setupUi(frmServerTerminal)
    frmServerTerminal.show()
    sys.exit(app.exec_())
