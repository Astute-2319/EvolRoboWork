import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        if str(self.jointName) == "Torso_BackLeg":
            self.amplitude = c.amplitude_back_leg
            self.frequency = c.frequency_back_leg
            self.offset = c.phase_offset_back_leg
            
            self.motorValues = np.linspace(0, c.back_leg_lin_space, c.simulation_steps)
            self.motorValues = self.amplitude * np.sin(self.frequency * self.motorValues + self.offset)

        else:
            self.amplitude = c.amplitude_front_leg
            self.frequency = c.frequency_front_leg
            self.offset = c.phase_offset_front_leg
            
            self.motorValues = np.linspace(0, c.front_leg_lin_space, c.simulation_steps)
            self.motorValues = self.amplitude * np.sin(self.frequency * self.motorValues + self.offset)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName.strip("b'"),
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.torso_back_leg_max_force)
        
    def Save_Values(self):
        jointStr = str(self.jointName)
        np.save("data/" + jointStr + "_Motor.npy", self.motorValues)
