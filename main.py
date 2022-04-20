import matplotlib.pyplot as plt
from Header import FruitClass, testing
from mpl_toolkits import mplot3d

fruit = ["Apple", "Pear", "Orange"]
Apple = FruitClass()
Apple.lists(fruit[0], 1, 31, "noshow")
appleSize = len(Apple.extent)

Pear = FruitClass()
Pear.lists(fruit[1], 1, 31, "noshow")
pearSize = len(Pear.extent)

Orange = FruitClass()
Orange.lists(fruit[2], 1, 31, "noshow")
orangeSize = len(Orange.extent)

redmean = []
redmean.extend(Apple.redmean)
redmean.extend(Pear.redmean)
redmean.extend(Orange.redmean)

greenmean = []
greenmean.extend(Apple.greenmean)
greenmean.extend(Pear.greenmean)
greenmean.extend(Orange.greenmean)

circularity = []
circularity.extend(Apple.circularity)
circularity.extend(Pear.circularity)
circularity.extend(Orange.circularity)

applePlace = appleSize
pearPlace = appleSize+pearSize
orangePlace = appleSize+pearSize+orangeSize
fruitInterval = [applePlace, pearPlace, orangePlace]
show3dplot = 0
if show3dplot == 1:
    # Creating figure
    fig = plt.figure("your mom")
    ax = plt.axes(projection="3d")
    # Creating plot
    ax.scatter3D(Apple.redmean, Apple.greenmean, Apple.circularity, color="green")
    ax.scatter3D(Pear.redmean, Pear.greenmean, Pear.circularity, color="yellow")
    ax.scatter3D(Orange.redmean, Orange.greenmean, Orange.circularity, color="orange")
    plt.title("simple 3D scatter plot")
    ax.set_xlabel('Red intensity', fontweight ='bold')
    ax.set_ylabel('Green intensity', fontweight ='bold')
    ax.set_zlabel('Circularity', fontweight ='bold')
    # show plot
    plt.show()

showPlot = 0
if showPlot == 1:
    plt.figure(1)
    plt.scatter(Apple.aspect, Apple.extent, marker='x', label="Apple")
    plt.scatter(Orange.aspect, Orange.extent, marker='s', label="Orange")
    plt.scatter(Pear.aspect, Pear.extent, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("Extent")
    plt.ylabel("Aspect ratio")
    plt.legend(loc='upper left')
    plt.figure(2)
    plt.scatter(Apple.aspect, Apple.meanint, marker='x', label="apple")
    plt.scatter(Orange.aspect, Orange.meanint, marker='s', label="Orange")
    plt.scatter(Pear.aspect, Pear.meanint, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("Aspect Ratio")
    plt.ylabel("Mean intensity")
    plt.legend(loc='upper left')
    plt.figure(3)
    plt.scatter(Apple.extent, Apple.meanint, marker='x', label="apple")
    plt.scatter(Orange.extent, Orange.meanint, marker='s', label="Orange")
    plt.scatter(Pear.extent, Pear.meanint, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("Extent")
    plt.ylabel("Mean intensity")
    plt.figure(4)
    plt.scatter(Apple.redmean, Apple.greenmean, marker='x', label="apple")
    plt.scatter(Orange.redmean, Orange.greenmean, marker='s', label="Orange")
    plt.scatter(Pear.redmean, Pear.greenmean, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("red intensity")
    plt.ylabel("green intensity")
    plt.figure(5)
    plt.scatter(Apple.bluemean, Apple.circularity, marker='x', label="apple")
    plt.scatter(Orange.bluemean, Orange.circularity, marker='s', label="Orange")
    plt.scatter(Pear.bluemean, Pear.circularity, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("blue intensity")
    plt.ylabel("circularity")
    plt.figure(6)
    plt.scatter(Apple.meanint, Apple.circularity, marker='x', label="apple")
    plt.scatter(Orange.meanint, Orange.circularity, marker='s', label="Orange")
    plt.scatter(Pear.meanint, Pear.circularity, marker=r'$\clubsuit$', label="Pear")
    plt.xlabel("mean intensity")
    plt.ylabel("circularity")
    plt.legend(loc='upper left')
    plt.show()

AppleTrain = FruitClass()
AppleTrain.lists(fruit[0], 32, 41,"noshow")
AppleTrainsize = len(AppleTrain.extent)

PearTrain = FruitClass()
PearTrain.lists(fruit[1], 32, 41,"noshow")
Peartrainsize = len(PearTrain.extent)

OrangeTrain = FruitClass()
OrangeTrain.lists(fruit[2], 32, 41,"noshow")
Orangetrainsize = len(OrangeTrain.extent)

print("test of apples")
testing(3, redmean, greenmean, circularity, AppleTrain.redmean, AppleTrain.greenmean, AppleTrain.circularity, AppleTrainsize,  fruit, fruitInterval)
print("test of oranges")
testing(3, redmean, greenmean, circularity, OrangeTrain.redmean, OrangeTrain.meanint, OrangeTrain.circularity, Orangetrainsize, fruit, fruitInterval)
print("test of pears")
testing(3, redmean, greenmean, circularity,  PearTrain.redmean, PearTrain.greenmean, PearTrain.circularity, Peartrainsize, fruit, fruitInterval)
