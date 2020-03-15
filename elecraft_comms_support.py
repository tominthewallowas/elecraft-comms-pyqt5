from PyQt5.QtWidgets import (QPushButton)
#import elecraft_comms as ec
from buttonholder import ButtonHolder


def extractSectionInfo(section):
    sectionDictionary = {}
    for key, value in section.items():
        sectionDictionary[key] = value.split('|')
    return sectionDictionary


def fillButtonGrid(ui, buttonHolders, max_buttons_per_row):
    row_pos = 0
    column_pos = 0

    for key, buttonHolder in buttonHolders.items():
        ui.buttonGridLayout.addWidget(buttonHolder.getButton(), row_pos, column_pos)
        column_pos += 1
        if column_pos >= max_buttons_per_row:
            column_pos = 0
            row_pos += 1


def createButtonHolders(ec, buttonInfoList):
    buttonHolderDictionary = {}
    buttonId = 2000
    for buttonLabel, buttonData in buttonInfoList.items():
        if buttonData[0] == True:
            button = QPushButton(buttonLabel)
            '''On the fly Dynamic Property in Qt parlance. Used to match a button to the desired command.'''
            button.setProperty('id', buttonId)
            button.clicked.connect(ec.methodDirector)
            bh = ButtonHolder(button, buttonData[2], buttonData[3])
            buttonHolderDictionary[buttonId] = bh
            buttonId += 1
    return buttonHolderDictionary

