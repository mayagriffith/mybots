import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        
    def Set_Value(self,robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= self.jointName,
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= desiredAngle,
                                maxForce = c.maxforce)


    def Save_Values(self):
        numpy.save("data\\" + self.jointName + "SensorValues.npy", self.motorValues)
        

        