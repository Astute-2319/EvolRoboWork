import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.simulation_steps)

    def Get_Value(self, time_stamp):
        self.values[time_stamp] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if time_stamp == 999:
            print(self.values)