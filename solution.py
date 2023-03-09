import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os


length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self):
        randWeight1 = np.random.rand()
        randWeight2 = np.random.rand()
        matrix = np.array([[randWeight1, randWeight2]])
        for i in range(2):
            randWeight1 = np.random.rand()
            randWeight2 = np.random.rand()
            add_row = np.array([[randWeight1, randWeight2]])
            matrix = np.concatenate((matrix, add_row), axis=0)
        self.weights = matrix
        self.weights = self.weights* 2 - 1

    
    def Evaluate(self):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[length,width,height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")


        for currentRow in range(3):
                for currentColumn in range(2):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow ,
                                        targetNeuronName = currentColumn + 3 ,
                                        weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    

