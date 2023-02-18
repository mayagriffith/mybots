import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
<<<<<<< HEAD
import random
import math
import constants as c
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
=======
import constants as c
>>>>>>> 9751369 (deleting anyways)


# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())

<<<<<<< HEAD
# p.setGravity(0,0, c.gravity)
=======


p.setGravity(0,0, c.gravity)
>>>>>>> 9751369 (deleting anyways)

# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# planeId = p.loadURDF("plane.urdf")

# robotId = p.loadURDF("body.urdf")



# backLegSensorValues = numpy.zeros(c.runs)
# frontLegSensorValues = numpy.zeros(c.runs)

# numsArray = 2*c.pi*(numpy.arange(c.runs) / c.runs)
# # targetAngles = (pi/4)*numpy.sin(numsArray)


# targetAnglesFront = c.amplitudeFront*numpy.sin(c.frequencyFront * numsArray + c.phaseOffsetFront)
# targetAnglesBack = c.amplitudeBack*numpy.sin(c.frequencyBack * numsArray + c.phaseOffsetBack)


# for iter in range(0,c.runs):
#     scaled_value = -c.pi/2 + (random.random() * (c.pi/2 - -c.pi/2))
#     p.stepSimulation()
#     time.sleep(1/60)
#     backLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[iter], maxForce = 500)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[iter], maxForce = 500)


# p.disconnect()

# with open('data/frontsensorvals.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues)

# with open('data/backsensorvals.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues)

# with open('data/arrayDataF.npy', 'wb') as f:
#     numpy.save(f, targetAnglesFront)

# with open('data/arrayDataB.npy', 'wb') as f:
#     numpy.save(f, targetAnglesBack)


