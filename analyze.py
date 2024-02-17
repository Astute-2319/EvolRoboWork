import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetAnglesValues = np.load('data/targetAnglesVals.npy')

# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues, linewidth = 5, label="Back Leg")

# pyplot.plot(frontLegSensorValues, label = "Front Leg")

# pyplot.legend()

pyplot.plot(targetAnglesValues, label = "Target Values")


pyplot.show()