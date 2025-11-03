from pybricks.tools import StopWatch
class timer:
    def __init__(self):
        self.total = StopWatch()
        self.mission = StopWatch()

    def stop(): pass
    
    def time(self):
        return self.total.time()
    
    def start_mission(self):
        self.mission.reset()
    
    def mission_time(self):
        return self.mission.time()
