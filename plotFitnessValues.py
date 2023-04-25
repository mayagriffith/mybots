import numpy
import matplotlib.pyplot
import constants as c

# A is without any hidden neurons
# B is with 5 hidden neurons

import numpy
import matplotlib.pyplot

def main():
    plot_all_best()
    plot_trial(4)

def plot_all_best():
    A_mins = [0] * c.numTrials
    B_mins = [0] * c.numTrials

    trials = []

    for i in range (0, c.numTrials):
        trials.append(i)

    for i in range(0,c.numTrials):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")

        i = int(i)

        A_mins [i-1] = A.min()
        B_mins [i-1] = B.min()

    matplotlib.pyplot.plot(trials, A_mins, color="blue", label = "No Hidden Neurons")
    matplotlib.pyplot.plot(trials, B_mins, color="yellow", label = "5 Hidden Neurons")
    matplotlib.pyplot.legend(loc="upper left")

    matplotlib.pyplot.title("Best Fitness")
    matplotlib.pyplot.xlabel("Trial")
    matplotlib.pyplot.ylabel("Fitness Value")



    matplotlib.pyplot.show()




    print(A_mins)
    print(B_mins)

    i = int(i)

def plot_all_means():
    for i in range(0,c.numTrials):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")
        A = numpy.mean(A, axis = 0)
        B = numpy.mean(B, axis = 0)

        if i == "1":
            matplotlib.pyplot.plot(A, color = "yellow", label = "No Hidden Nuerons")
            matplotlib.pyplot.plot(B, color = "blue", label = "5 Hidden Nuerons")

        else:
            matplotlib.pyplot.plot(A, color = "yellow")
            matplotlib.pyplot.plot(B, color = "blue")
        print(i)


    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot All Means")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()
    i = int(i)


def plot_mean():

    A1 = numpy.load("matrixA1.npy")
    A2 = numpy.load("matrixA2.npy")
    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)


    A = numpy.mean(numpy.array([A1, A2], dtype=object), axis=0)


    B1 = numpy.load("matrixB1.npy")
    B2 = numpy.load("matrixB2.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)

    B = numpy.mean(numpy.array([B1, B2], dtype=object), axis=0)

    sA = numpy.std(A)
    sB = numpy.std(B)

    matplotlib.pyplot.plot(A+sA, color = "blue", label = "No Hidden Neurons stdev")
    matplotlib.pyplot.plot(A, color = "blue", label = "No Hidden Neurons")
    matplotlib.pyplot.plot(A-sA, color = "blue")
 
    matplotlib.pyplot.plot(B+sB, color = "yellow", label = "5 Hidden Neurons stdev")    
    matplotlib.pyplot.plot(B, color = "yellow", label = "5 Hidden Neurons")
    matplotlib.pyplot.plot(B-sB, color = "yellow")



    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot Mean of all Trials")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


def plot_trial(i):
    i = str(i)
    none = numpy.load("matrixA" + i + ".npy")
    five = numpy.load("matrixB" + i + ".npy")

    none = numpy.mean(none, axis = 0)
    five = numpy.mean(five, axis = 0)

    s2 = numpy.std(none)
    s4 = numpy.std(five)



    matplotlib.pyplot.plot(none-s2, color = "blue", label = "No Hidden Nuerons std")
    matplotlib.pyplot.plot(none, color = "blue", label = "No Hidden Nuerons")
    matplotlib.pyplot.plot(none+s2, color = "blue")

    matplotlib.pyplot.plot(five-s4, color = "yellow", label = "5 Hidden Nuerons std")
    matplotlib.pyplot.plot(five, color = "yellow", label = "5 Hidden Nuerons")
    matplotlib.pyplot.plot(five+s4, color = "yellow")


    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Trial " + i)
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


main()