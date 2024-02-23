import pybullet as p
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.sensor = {}
        self.motor = {}
        self.robotID = p.loadURDF("body.urdf")