from Displays import *
from Button import *

"""
This is a counter that will implement a basic increment reset 
counter and show the count display.
"""



class counter:
    def __init__(self):
        print("Counter: Constructor")
        self._number = 0
        self._display = display = LCDDisplay(sda=20, scl=21, i2cid=0)

        self._greenButton = Button(17, "increase", buttonhandler = self, lowActive = True)
        self._reButton = Button(16, "reset", buttonhandler = self, lowActive = True)

    def increment (self):
        print("Counter: Incrementing")
        self._number = self._number + 1

    def reset(self):
        print("I should be reseting")
        self._number = 0
        self._display.reset()

    def buttonPressed(self, name):
        if name == "increase":
            self.increment()
        elif name == "reset":
            self.reset()

    def buttonReleased (self, name):
        pass
    
    def show(self):
        while True:
            self._display.showNumber(self._number)
            time.sleep(0.1)
            
