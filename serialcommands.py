#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# serialcommands.py

import logging
# 9/17/2019 Spooky situation with serial. Threw exception not found error.  By serendipity
# I found pyserial.  Installed it and the app.  Uninstalled both pyserial and serial
# and then reinstalled pyserial.  So what the hell is serial?
import serial

logger = logging.getLogger('SERIALCOMMANDS')
logger.setLevel(logging.ERROR)
log_format = '%(asctime)s:%(lineno)s:%(levelname)s:%(name)s:%(message)s'
formatter = logging.Formatter(log_format)
file_handler = logging.FileHandler('serialcommands.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class SerialCommands(object):
    '''
    SerialCommands caches a dictionary of active ports for use by other
    programming objects to send and retrieve serial data.
    '''

    def __init__(self, ports=None):
        '''
        Given a dictionary of device names containing a pipe delimited
        string of port name and baud rate the  will attempt to open the ports and place in a dictionary.
        '''
        self.openports = {}
        if ports:
            self.openPorts(ports)

    def openPorts(self, ports):
        '''
        Given a dictionary of device names containing a pipe delimited
        string of port name and baud rate function will attempt to open the ports
        and place the port reference in a dictionary.
        '''
        for device, port_config in ports.items():
            self.openPort(device, port_config[0], port_config[1])

    def openPort(self, device, port, baudrate):
        '''
        Given a single device name, port and baud rate, attempt to open it and place
        it in the openports dictionary. If successful, return
        true, if not, return false.
        '''
        try:
            ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        except serial.SerialException:
            logger.exception('SerialException')
        else:
            self.openports[device] = ser
            return True

    def checkPort(self, port=None):
        '''
        Assumes the ports that are open are contained within
        the self.openports list.  If not raises exception.
        Otherwise checks if the port is open.
        '''
        serialport = self.openports.get(port, None)
        if serialport:
            return serialport.is_open
        else:
            return False

    def checkPorts(self):
        '''
        Check the status on all ports in the openports dictionary
        and return each port status as a list of tuples.
        '''
        portsstatus = []
        for portname, port in self.openports.items():
            portsstatus.append((portname, port.is_open))
        return portsstatus

    def closePorts(self):
        '''
        Close ports stored in openports dictionary, and destroy
        the objects.
        '''
        for portname, port in self.openports.items():
            port.close()
        self.openports.clear()

    def runCommand(self, command):
        '''
        Given a list containing a named comm port and a command
        write to the port and return the result.
        '''
        return self.openports[command[0]].write(str.encode(command[1]))

    def readPort(self, command, howmany=40):
        '''
        Given a list containing a named comm port and command,
        read the number of characters requested. Defaults to 40.
        '''
        #response = self.runCommand(command)
        self.openports[command[0]].reset_input_buffer()
        return self.openports[command[0]].read(howmany)


if __name__ == '__main__':
    #import elecraft
    print('__main__')
    commands = {
        'DATAMODE': 'COM13|MD6;',
        'POWER50': 'COM13|PC050;',
        'DATASUBMODEA': 'COM13|DT0;',
        'WWV': 'COM13|FA00010000000;',
        'TESTTOGGLE': 'COM13|SWH18;',
        'VOX': 'COM13|SWH09;'
    }
    command_sequences = {
        'SETDATAMODE': 'DATAMODE|DATASUBMODEA|POWER50',
        'WWV': 'WWV',
        'VOX': 'VOX',
        'TESTTOGGLE': 'TESTTOGGLE'
    }
    logger.debug('In Main')
    #sc = SerialCommands({'COM13':38400, 'COM4':38400, 'COM6':38400})
    sc = SerialCommands({'/dev/ttyUSB2': [38400]})
    #command = ['COM13', 'PC001;']
    #command = ['COM13', 'MD;']
    command = ['/dev/ttyUSB2', 'SWH18;']
    sc.runCommand(command)
    #response = sc.readPort(command)
    #status = elecraft.listifyHexstring(response)
    # print(status)
    sc.closePorts()
