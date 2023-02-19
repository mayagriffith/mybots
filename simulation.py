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
            self.robot.Sense(iter)
            self.robot.Act(iter)
            time.sleep(1/60)