import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load('data/BackLeg_Sensor.npy')
frontLegSensorValues = np.load('data/FrontLeg_Sensor.npy')
targetAnglesValuesBack = np.load('data/Torso_BackLeg_Motor.npy')
targetAnglesValuesFront = np.load('data/Torso_FrontLeg_Motor.npy')

# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues, linewidth = 5, label="Back Leg")

# pyplot.plot(frontLegSensorValues, label = "Front Leg")

# pyplot.legend()

pyplot.xlabel("Iteration")
pyplot.ylabel("Target Value")

pyplot.plot(targetAnglesValuesBack, label = "Target Values Back")

pyplot.plot(targetAnglesValuesFront, label = "Target Values Front")

pyplot.legend()

pyplot.show()