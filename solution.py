import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random

class SOLUTION:
    def __init__(self):
        self.weights = (np.random.rand(3, 2)) * 2 - 1
    
    def Evaluate(self):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py")
        fitness_file = open("fitness.txt", 'r')
        self.fitness = float(fitness_file.read())
        fitness_file.close()

    def Mutate(self):
        new_sensor = random.randint(0, 2)
        new_motor = random.randint(0, 1)
        self.weights[new_sensor, new_motor] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        for current_row in range(0, 3):
            for current_col in range (0, 2):
                pyrosim.Send_Synapse(sourceNeuronName = current_row, targetNeuronName = current_col+3, weight = self.weights[current_row][current_col])

        pyrosim.End()
