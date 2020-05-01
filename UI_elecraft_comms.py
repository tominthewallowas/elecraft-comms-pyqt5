# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_elecraft_comms.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 117)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbSendCommand = QtWidgets.QPushButton(self.centralwidget)
        self.pbSendCommand.setObjectName("pbSendCommand")
        self.horizontalLayout_2.addWidget(self.pbSendCommand)
        self.cmbRig = QtWidgets.QComboBox(self.centralwidget)
        self.cmbRig.setObjectName("cmbRig")
        self.horizontalLayout_2.addWidget(self.cmbRig)
        self.leCommand = QtWidgets.QLineEdit(self.centralwidget)
        self.leCommand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.leCommand.setObjectName("leCommand")
        self.horizontalLayout_2.addWidget(self.leCommand)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonGridLayout = QtWidgets.QGridLayout()
        self.buttonGridLayout.setObjectName("buttonGridLayout")
        self.verticalLayout.addLayout(self.buttonGridLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbQuit = QtWidgets.QPushButton(self.centralwidget)
        self.pbQuit.setObjectName("pbQuit")
        self.horizontalLayout.addWidget(self.pbQuit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elecraft Comms"))
        self.pbSendCommand.setText(_translate("MainWindow", "&Send"))
        self.pbQuit.setText(_translate("MainWindow", "&Quit"))
