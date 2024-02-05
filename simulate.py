import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time as t

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robotID = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotID)

backLegSensorValues = numpy.zeros(10000)

for x in range(0, 1000):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegSensorValues)
    t.sleep(1/60)
    # print(x)

print(backLegSensorValues)


p.disconnect()