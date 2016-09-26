import time

class LoggableList(list, Loggable):
    def append(self, data):
        self.log(data)
        super(LoggableList, self).append(data)
