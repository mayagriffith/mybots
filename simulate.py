import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math

pi = math.pi

runs = 100



physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-90.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)


backLegSensorValues = numpy.zeros(runs)
frontLegSensorValues = numpy.zeros(runs)

numsArray = 2*pi*(numpy.arange(runs) / runs)
targetAngles = (pi/4)*numpy.sin(numsArray)


for iter in range(0,runs):
    scaled_value = -pi/2 + (random.random() * (pi/2 - -pi/2))
    p.stepSimulation()
    time.sleep(1/60)
    backLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = scaled_value, maxForce = 500)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = scaled_value, maxForce = 500)







# print(backLegSensorValues)



p.disconnect()

with open('data/frontsensorvals.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backsensorvals.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)

