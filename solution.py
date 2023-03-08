import numpy as np

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

sol = SOLUTION()