import numpy
import matplotlib.pyplot

backLegSensorVals = numpy.load("data/backsensorvals.npy")
frontLegSensorVals = numpy.load("data/frontsensorvals.npy")
DataFront = numpy.load("data/arrayDataF.npy")
DataBack = numpy.load("data/arrayDataB.npy")



print(backLegSensorVals)
print(frontLegSensorVals)


matplotlib.pyplot.plot(backLegSensorVals, linewidth=2, label = "Back leg")
matplotlib.pyplot.plot(frontLegSensorVals, linewidth=4, label = "Front leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


matplotlib.pyplot.plot(DataFront, linewidth=1, label = "Front")
matplotlib.pyplot.plot(DataBack, linewidth=3.5, label = "Back")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()