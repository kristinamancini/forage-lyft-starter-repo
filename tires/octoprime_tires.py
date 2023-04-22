from tires.tires import Tires
from array import *


class OctoprimeTires(Tires):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        if sum(self.sensors) >= 3:
            return True
        else:
            return False