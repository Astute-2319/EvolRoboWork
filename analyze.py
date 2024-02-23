import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load('data/back_leg_sensor_values.npy')
frontLegSensorValues = np.load('data/front_leg_sensor_values.npy')
targetAnglesValuesBack = np.load('data/target_angles_values_back.npy')
targetAnglesValuesFront = np.load('data/target_angles_values_front.npy')

# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues, linewidth = 5, label="Back Leg")

# pyplot.plot(frontLegSensorValues, label = "Front Leg")

# pyplot.legend()

pyplot.plot(targetAnglesValuesBack, label = "Target Values Back")

pyplot.plot(targetAnglesValuesFront, label = "Target Values Front")

pyplot.legend()

pyplot.show()