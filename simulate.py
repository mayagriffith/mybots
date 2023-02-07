import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-90.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for iter in range(0,100):
    p.stepSimulation()
    time.sleep(1/60)
    backLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = ..., maxForce = ...)






# print(backLegSensorValues)



p.disconnect()

with open('data/frontsensorvals.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backsensorvals.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)

