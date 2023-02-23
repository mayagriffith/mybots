import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        # self.motorValues = numpy.zeros(c.runs)
        # self.Prepare_To_Act()

    # def Prepare_To_Act(self):
    #     self.amplitude = c.amplitude
    #     self.phaseOffset = c.phaseOffset
    #     self.frequency = c.frequency
    #     name = str(self.jointName)

    #     if ("Front" in name):
    #        self.phaseOffset = c.pi/2
    #        print('yes')
    
    #     numsArray = 2*c.pi*(numpy.arange(c.runs) / c.runs)
    #     # targetAngles = (c.pi/4)*numpy.sin(numsArray)
    #     self.motorValues = self.amplitude*numpy.sin(self.frequency * numsArray + self.phaseOffset)

    def Set_Value(self,robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= self.jointName,
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= desiredAngle,
                                maxForce = c.maxforce)


    def Save_Values(self):
        numpy.save("data\\" + self.jointName + "SensorValues.npy", self.motorValues)
        

        