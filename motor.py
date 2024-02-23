import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude_back_leg
        self.frequency = c.frequency_back_leg
        self.offset = c.phase_offset_back_leg
        
        self.motorValues = np.linspace(0, c.back_leg_lin_space, c.simulation_steps)
        self.motorValues = self.amplitude * np.sin(self.frequency * self.motorValues + self.offset)

    def Set_Value(self, robot, time_stamp):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[time_stamp],
            maxForce = c.torso_back_leg_max_force)
        
    def Save_Values(self):
        np.save("data/" + self.jointName + "_Motor.npy", self.motorValues)
