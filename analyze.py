import numpy
import matplotlib.pyplot

backLegSensorVals = numpy.load("data/backsensorvals.npy")
frontLegSensorVals = numpy.load("data/frontsensorvals.npy")


print(backLegSensorVals)
print(frontLegSensorVals)


matplotlib.pyplot.plot(backLegSensorVals, linewidth=2, label = "Back leg")
matplotlib.pyplot.plot(frontLegSensorVals, linewidth=4, label = "Front leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()