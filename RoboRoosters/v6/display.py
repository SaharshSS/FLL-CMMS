from pybrics.parameters import Icon
from pybrics.hubs import PrimeHub

class display:
    def __init__(self):
        self.hub = PrimeHub()
    
    def char(self, char):
        self.hub.display.char(str(char))
    
    def number(slef, displayVal, displayOn = False):
        if displayOn:
            self.hub.display.off()
            displayOn = False
        else:
            displayOn = True
            if isinstance(displayval, int):
                if displayVal < 10 and displayVal >= 0:
                    self.char(displayVal)
                else:
                    self.hub.display.number(int(displayVal))
            else: self.char(displayVal)
        return displayOn
