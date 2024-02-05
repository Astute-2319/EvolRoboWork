import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')

print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.xlim(0, 100)

matplotlib.pyplot.show()