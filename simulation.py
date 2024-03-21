import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time as t
from world import WORLD

class SIMULATION:
    def __init__(self, direct_or_gui):
        self.direct_or_gui = direct_or_gui
        if self.direct_or_gui == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        elif self.direct_or_gui == 'GUI':
            self.physicsClient = p.connect(p.GUI)
        else:
            raise Exception ("Unexpected simulation type", self.direct_or_gui)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.std_grav)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robot)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
    
    def Run(self):
        for x in range(0, c.simulation_steps):
            # print(x)
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
            self.Get_Fitness()
            if self.direct_or_gui == 'GUI':
                t.sleep(c.sleep_length)

        for sensor in self.robot.sensors:
            self.robot.sensors[sensor].Save_Values()
        
        for motor in self.robot.motors:
            self.robot.motors[motor].Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
