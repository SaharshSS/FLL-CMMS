from pybrics.hubs import PrimeHub

class battery():
    def __init__(self):
        self.hub = PrimeHub
    
    def stop(): pass

    def voltage(self):
        return self.hub.battery.voltage()/1000

    def current(self):
        return self.hub.battery.current()/1000
    
    def percentage(self):
        return (round((self.voltage()-6.2)*50))
