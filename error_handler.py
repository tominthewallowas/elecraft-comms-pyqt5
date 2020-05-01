#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# error_handler.py

'''
A class that is passed to any another class that will respond
to an error with an appropriate message.
'''

from datetime import datetime


class ErrorHandler:
    '''
    ErrorHandler class to receive errors from any part of the program
    that chooses to use it. The class object is created in the main
    program (during __init__) and passed as parm when other classes
    are created.
    '''

    def __init__(self, ui):
        '''Let the class know about the ui.'''
        self.ui = ui

    def handle_error(self, err):
        '''Receive an error object from another function and then
           hand it off to the display function.
        '''
        message = None

        print(type(err))
        if isinstance(err, KeyError):
            message = f"A Key Error occurred at {datetime.now():%H:%m:%S}. Check your keys."
        if message:
            self.ui.statusBar.showMessage(message)
