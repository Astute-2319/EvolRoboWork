import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetAnglesValuesBack = np.load('data/targetAnglesValuesBack.npy')
targetAnglesValuesFront = np.load('data/targetAnglesValuesFront.npy')

# print(backLegSensorValues)

# pyplot.plot(backLegSensorValues, linewidth = 5, label="Back Leg")

# pyplot.plot(frontLegSensorValues, label = "Front Leg")

# pyplot.legend()

pyplot.plot(targetAnglesValuesBack, label = "Target Values Back")

pyplot.plot(targetAnglesValuesFront, label = "Target Values Front")

pyplot.legend()

pyplot.show()