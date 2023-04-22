from tires.tires import Tires
from array import *


class CarriganTires(Tires):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        for i in self.sensors:
            if i >= 0.9:
                return True
            else:
                continue
        return False
