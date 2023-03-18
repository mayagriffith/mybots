import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os



class ROBOT:
    def __init__(self, solutionID):
        #loading robot
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        os.system("rm brain" + solutionID + ".nndf")



    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

        
    def Sense(self, t):
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(linkName, t)
    
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,t):
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desiredAngle = self.nn.Get_Value_Of(neuronName)
                    # print(jointName)
                    # print(self.motors[jointName])
                    jointName = str(jointName)
                    self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                    # print(neuronName, jointName, desiredAngle)
            # for i in self.motors:
            #     self.motors[i].Set_Value(self.robotId, i, t)
            

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordindateOfLinkZero = positionOfLinkZero[0]
        file = open("tmp" + solutionID + ".txt", "w")
        file.write(str(xCoordindateOfLinkZero))
        file.close()
        os.system("mv tmp"+ str(solutionID) + ".txt" + " fitness" + str(solutionID)+ ".txt")