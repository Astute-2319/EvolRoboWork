# import constants as c
# import numpy as np
# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import time as t

# 
# 

# 
# 
# 

# 

# 

# 
# front_leg_sensor_values = np.zeros(c.simulation_steps)

# target_angles_list_back_leg = np.linspace(0, c.back_leg_lin_space, c.simulation_steps)
# target_angles_back_leg = c.amplitude_back_leg * np.sin(c.frequency_back_leg * target_angles_list_back_leg + c.phase_offset_back_leg)
# np.save("data/target_angles_values_back.npy", target_angles_back_leg)

# target_angles_list_front_leg = np.linspace(0, c.front_leg_lin_space, c.simulation_steps)
# target_angles_front_leg = c.amplitude_front_leg * np.sin(c.frequency_front_leg * target_angles_list_front_leg + c.phase_offset_front_leg)
# np.save("data/target_angles_values_front.npy", target_angles_front_leg)

# # exit()




# np.save("data/back_leg_sensor_values.npy", back_leg_sensor_values)
# np.save("data/front_leg_sensor_values.npy", front_leg_sensor_values)


# 

from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()