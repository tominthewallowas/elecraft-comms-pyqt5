#!/usr/bin/env python3

import sys
import os

from PyQt5.QtWidgets import (QMainWindow, QApplication, QButtonGroup,
                             QPushButton, QLineEdit, QLayout,
                             QDesktopWidget, QDialog, QTableWidgetItem,)
from UI_elecraft_comms import *

import elecraft_comms_support as ecs
from serialcommands import SerialCommands
from error_handler import ErrorHandler
import yaml


class ElecraftComms(QMainWindow):
    def __init__(self):
        '''Sets various widgets on and off and sets up some initial objects.'''
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        eh = ErrorHandler(self.ui)
        config_data = self.loadConfiguration()
        self.buttonHolders = ecs.createButtonHolders(self, config_data['Button Labels'])
        ecs.fillButtonGrid(self.ui, self.buttonHolders, config_data['Misc']['max_buttons_per_row'])
        self.command_sequences = config_data['Command Sequences']
        self.devices_and_commands = config_data['Commands']
        self.loadRigCombo(config_data['Ports'])
        self.ui.pbSendCommand.clicked.connect(self.sendAdHocCommand)
        self.ui.leCommand.returnPressed.connect(self.sendAdHocCommand)
        self.sc = SerialCommands(error_handler=eh)
        self.ui.pbQuit.clicked.connect(self.close)
        self.openPorts(config_data['Ports'], self.sc)
        self.show()

    def sendAdHocCommand(self):
        self.sc.runCommand([self.ui.cmbRig.currentText(), self.ui.leCommand.text()])

    def loadRigCombo(self, rigs):
        self.ui.cmbRig.addItems([rig for rig, _ in rigs.items()])

    def openPorts(self, port_config, sc):
        for device_name, device_data in port_config.items():
            sc.openPort(device_name, device_data[0], device_data[1])

    def getButtonData(self, config_data):
        button_data = config_data['Button Labels']
        return button_data

    def loadConfiguration(self):
        config_data = None
        with open('comms.yaml') as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)
        return config_data

    # def loadCommandsIntoGrid(self):
        # print('Yorgi')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def methodDirector(self):
        command_sequence_name = self.buttonHolders[self.sender().property('id')].getCommand()
        commands = self.command_sequences[command_sequence_name]
        for command in commands:
            self.sc.runCommand(self.devices_and_commands[command])


if __name__ == "__main__":
    app = QApplication([])
    w = ElecraftComms()
    w.show()
    sys.exit(app.exec_())
