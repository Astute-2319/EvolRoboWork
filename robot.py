import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.motor = {}
        self.robotID = p.loadURDF("body.urdf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, time_stamp):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_stamp)