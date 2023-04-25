import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from hillclimber import HILL_CLIMBER
import constants as c


for trial in range(1, 11):
    c.numHiddenNeurons = 0
    phcA = PARALLEL_HILL_CLIMBER(trial)
    phcA.Evolve()
    phcA.Show_Best()

    c.numHiddenNeurons = 5
    phcB = PARALLEL_HILL_CLIMBER(trial)
    phcB.Evolve()
    phcB.Show_Best()

    




