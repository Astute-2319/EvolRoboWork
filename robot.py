import os
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self, simulation_id):
        self.robot = p.loadURDF("body.urdf")
        self.id = simulation_id
        self.nn = NEURAL_NETWORK("brain" + str(simulation_id) + ".nndf")
        os.system("del brain" + str(simulation_id) + ".nndf")
    
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
        
    def Get_Fitness(self):
        state_of_link_zero = p.getLinkState(self.robot, 0)
        position_of_link_zero = state_of_link_zero[0]
        x_coord_of_link_zero = position_of_link_zero[0]
        fitness_file = open("tmp" + str(self.id) + ".txt", 'w')
        fitness_file.write(str(x_coord_of_link_zero))
        fitness_file.close()
        if os.path.exists("fitness" + str(self.id) + ".txt"):
            os.remove("fitness" + str(self.id) + ".txt")
        os.system("rename tmp" + str(self.id) + ".txt fitness" + str(self.id) + ".txt")
        # print(x_coord_of_link_zero)
        # exit()