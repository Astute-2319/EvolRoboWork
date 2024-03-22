import pyrosim.pyrosim as pyrosim
from simulation import SIMULATION
import sys

pyrosim.Start_SDF("world.sdf")
pyrosim.End()

pyrosim.Start_URDF("body.urdf")

pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])

pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

pyrosim.End()

direct_or_gui = sys.argv[1]
solution_id = sys.argv[2]

simulation = SIMULATION(direct_or_gui, solution_id)
simulation.Run()