import numpy
import matplotlib.pyplot

# A is without any hidden neurons
# B is with 5 hidden neurons

import numpy
M = numpy.load("matrixB.npy")
import matplotlib.pyplot


for i in range(10):
    row = M[i,:]
    matplotlib.pyplot.plot(row)

matplotlib.pyplot.show()