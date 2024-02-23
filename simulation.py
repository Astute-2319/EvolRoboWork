import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time as t
from world import WORLD

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.std_grav)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotID)
    
    def Run(self):
        for x in range(0, c.simulation_steps):
            print(x)
            p.stepSimulation()
            # back_leg_sensor_values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # front_leg_sensor_values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotID,
            #     jointName = b"Torso_BackLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = target_angles_back_leg[x],
            #     maxForce = c.torso_back_leg_max_force)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotID,
            #     jointName = b"Torso_FrontLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = target_angles_front_leg[x],
            #     maxForce = c.torso_front_leg_max_force)
            t.sleep(c.sleep_length)
    
    def __del__(self):
        p.disconnect()