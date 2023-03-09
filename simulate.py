import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math
import constants as c
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
