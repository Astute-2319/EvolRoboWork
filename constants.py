import numpy as np
# simulation values
std_grav = -9.8
simulation_steps = 1000
pi = np.pi
sleep_length = 1/60

# back leg
amplitude_back_leg = pi/4.0
frequency_back_leg = 10
phase_offset_back_leg = pi
back_leg_lin_space = 2*pi

# front leg
amplitude_front_leg = pi/4.0
frequency_front_leg = 10
phase_offset_front_leg = pi/4
front_leg_lin_space = 2*pi

# joints

# Torso_Back
torso_back_leg_max_force = 500

# Torso_Front
torso_front_leg_max_force = 500
