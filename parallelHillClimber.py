from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            thisSolution = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
            self.parents[i] = thisSolution

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
  
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
       for i in self.parents:
            if (self.parents[i].fitness > self.children[i].fitness):
                self.parents[i] = self.children[i]

    
    def Print(self):
        print("")
        for i in self.parents:
            print(self.parents[i].fitness, self.children[i].fitness)
        print("")

    def Show_Best(self):
        bestFitness = self.parents[0].fitness
        bestFitnessID = 0
        for i in range(len(self.parents)-1):
            if (bestFitness > self.parents[i+1].fitness):
                bestFitness = self.parents[i+1].fitness
                bestFitnessID = i+1        
        
        self.parents[bestFitnessID].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()