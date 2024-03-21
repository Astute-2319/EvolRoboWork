import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, time_stamp):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_stamp)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            jointName = jointName.decode()
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, time_stamp):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                # print(desiredAngle)