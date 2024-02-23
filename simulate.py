# import constants as c
# import numpy as np
# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import time as t

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,c.std_grav)
# planeID = p.loadURDF("plane.urdf")
# p.loadSDF("world.sdf")

# robotID = p.loadURDF("body.urdf")

# pyrosim.Prepare_To_Simulate(robotID)

# back_leg_sensor_values = np.zeros(c.simulation_steps)
# front_leg_sensor_values = np.zeros(c.simulation_steps)

# target_angles_list_back_leg = np.linspace(0, c.back_leg_lin_space, c.simulation_steps)
# target_angles_back_leg = c.amplitude_back_leg * np.sin(c.frequency_back_leg * target_angles_list_back_leg + c.phase_offset_back_leg)
# np.save("data/target_angles_values_back.npy", target_angles_back_leg)

# target_angles_list_front_leg = np.linspace(0, c.front_leg_lin_space, c.simulation_steps)
# target_angles_front_leg = c.amplitude_front_leg * np.sin(c.frequency_front_leg * target_angles_list_front_leg + c.phase_offset_front_leg)
# np.save("data/target_angles_values_front.npy", target_angles_front_leg)

# # exit()

# for x in range(0, c.simulation_steps):
#     p.stepSimulation()
#     back_leg_sensor_values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     front_leg_sensor_values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotID,
#         jointName = b"Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = target_angles_back_leg[x],
#         maxForce = c.torso_back_leg_max_force)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotID,
#         jointName = b"Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = target_angles_front_leg[x],
#         maxForce = c.torso_front_leg_max_force)
#     t.sleep(c.sleep_length)


# np.save("data/back_leg_sensor_values.npy", back_leg_sensor_values)
# np.save("data/front_leg_sensor_values.npy", front_leg_sensor_values)


# p.disconnect()

from simulation import SIMULATION

simulation = SIMULATION()

