import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, __object) -> None:
        self.log(__object)
        return super().append(__object)
    
l1 = LoggableList()
l1.append(5)
print(l1)