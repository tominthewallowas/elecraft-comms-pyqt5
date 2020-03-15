class ButtonHolder():
    def __init__(self, button=None, command=None, monitor=None):
        self.button = button
        self.command = command
        self.monitor = monitor

    def setButton(self, button):
        self.button = button

    def getButton(self):
        return self.button

    def setCommand(self, command):
        self.command = command

    def getCommand(self):
        return self.command

    def setMonitor(self, monitor):
        self.monitor = monitor

    def getMonitor(self):
        return self.monitor

    def getId(self):
        return self.button.property('id')
