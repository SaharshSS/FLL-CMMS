from pybrics.parameters import Port, Direction
from pybrics.pupdevices import Motor

class arm:
    def __init__(self, Port1, Port2):
        try:
            self.armMid = Motor(Port1)
            self.armBase = Motor(Port2, Direction.COUNTERCLOCKWISE)
        except OSError:
            print("Incorrect arm ports")
    
    def stop(self):
        self.armMid.stop()
        self.armBase.stop()

    def turn(self, midAngle, baseAngle, mode = 0, speed = 1750):
        if not mode:
            self.armMid.run_target(speed, midAngle, wait = False)
            self.armBase.run_target(speed, baseAngle)
        elif mode == 1:
            self.armMid.run_target(speed, midAngle)
            self.armBase.run_target(speed, baseAngle)
        elif mode == 2:
            self.armBase.run_target(speed, midAngle)
            self.armMid.run_target(speed, baseAngle)
        else:
            self.armBase.run_target(speed, midAngle, wait = False)
            self.armMid.run_target(speed, baseAngle, wait = False)

    def reset(self): self.turn(0, 90, 1, 2500)
    def up(self): self.turn(90, 90, 1, 2500)
    def hook(self): self.turn(45, -45, 2, 2500)
