import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI) 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity) 
        self.world = WORLD()
        self.robot = ROBOT()


    def __del__(self):
        p.disconnect()

    def Run(self):
        for iter in range(0,c.runs):
            # scaled_value = -c.pi/2 + (random.random() * (c.pi/2 - -c.pi/2))
            p.stepSimulation()
            # time.sleep(1/60)
            # backLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[iter], maxForce = 500)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[iter], maxForce = 500)
            print(iter)
            time.sleep(1/60)