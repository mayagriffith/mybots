import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.runs)

    def Get_Value(self, linkName, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)

     #Save sensor data to file
    def Save_Values(self):
        numpy.save("data\\" + self.linkName + "SensorValues.npy", self.values)
     