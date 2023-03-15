from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        for i in range(0, c.populationSize):
            thisSolution = SOLUTION()
            self.parents[i] = thisSolution

    def Evolve(self):
        for generation in range(0, c.populationSize):
            self.parents[generation].Evaluate("GUI")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child
    
    def Print(self):
        print("fitness coordinates for this run:")
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")