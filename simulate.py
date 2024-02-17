import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time as t
import random

pi = np.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robotID = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotID)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAnglesList = np.linspace(0, 2*pi, 1000)
targetAngles = np.sin(targetAnglesList)
# np.save("data/targetAnglesVals.npy", targetAngles)


for x in range(0, 1000):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[x],
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[x],
        maxForce = 500)
    t.sleep(1/60)


np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)


p.disconnect()