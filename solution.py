import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c


length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.sensorToHidden = np.random.random((c.numSensorNeurons,c.numHiddenNeurons))
        self.sensorToHidden = self.sensorToHidden* 2 - 1
        self.hiddenToMotor = np.random.random((c.numHiddenNeurons,c.numMotorNeurons))
        self.hiddenToMotor = self.hiddenToMotor * 2 - 1

    
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.readline())
        print(self.fitness)
        fitnessFile.close()
        os.system("rm fitness" + str(self.myID) + ".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        pyrosim.Send_Joint( name= "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube( name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        
        pyrosim.Send_Joint( name= "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube( name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[.2,1,.2])

        pyrosim.Send_Joint( name= "FrontLeg_FrontLowerLeg", parent = "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube( name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint( name= "BackLeg_BackLowerLeg", parent = "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube( name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint( name= "LeftLeg_LeftLowerLeg", parent = "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube( name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint( name= "RightLeg_RightLowerLeg", parent = "RightLeg", child = "RightLowerLeg", type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube( name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightLowerLeg")

        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name = c.numSensorNeurons+i)
        

        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 1, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 2, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 3, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 4, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 5, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 6, jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons + c.numHiddenNeurons + 7, jointName = "RightLeg_RightLowerLeg")
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons+c.numMotorNeurons , weight = self.sensorToHidden[currentRow][currentColumn])
        
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow+c.numSensorNeurons+c.numMotorNeurons, targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.hiddenToMotor[currentRow][currentColumn])

        pyrosim.End()


    def Mutate(self):
        self.sensorToHidden[random.randint(0,c.numSensorNeurons-1),random.randint(0,c.numHiddenNeurons-1)] = random.random()*2-1
        self.hiddenToMotor[random.randint(0,c.numHiddenNeurons-1),random.randint(0,c.numMotorNeurons-1)] = random.random()*2-1
        

    def Set_ID(self):
        return self.myID + 1


    

