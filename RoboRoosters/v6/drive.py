from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

class drive():
    def __init__(self, portl, portr):
        try:
            self.left = Motor(portl, Direction.COUNTERCLOCKWISE)
            self.right = Motor(Port.B)
            try self.drive = DriveBase(self.left, self.right, wheel_diameter = 62.4, axle_track = 127)
        except OSError:
            print("Incorrect drive ports")

    def wait(self):
        while not self.drive.done():
            wait(10)

    def straight(self, distance, then = Stop.HOLD, wait = True speed = 750):
        if wait: self.wait()
        self.drive.settings(straight_speed = speed)
        self.drive.straight(distance, then, wait)

    def stop(self):
        if wait: self.wait()
        self.drive.stop
    
    def curve(self, radius, angle, then = Stop.HOLD, wait = True, speed = 500):
        if wait: self.wait()
        self.drive.settings(straight_speed = speed, turn_rate = speed)
        self.drive.curve(radius, angle, then, wait)

    def turn(self, angle, then = Stop.HOLD, wait = True, speed = 750):
        if wait: self.wait()
        self.drive.settings(turn_rate = speed)
        self.drive.turn(angle, then, wait)
    
    def back(self, distance, then = Stop.HOLD, wait = True, speed = 750):
        self.straight(-distance, then, wait, speed)
    
    def back_square(self):
        self.straight(-125, then=Stop.COAST, speed = 125)
    
    def front_square(self):
        self.straight(125, then=Stop.COAST, speed = 125)
