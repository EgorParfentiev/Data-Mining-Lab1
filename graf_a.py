import matplotlib.pyplot
import main


arrS = main.spamdict
arrH = main.hamdict


arrSS = {}
arrSH = {}

sGroup = {}
hGroup = {}



def countMax(arr):
    max = 0
    for item in arr:
        if len(item) > max:
            max = len(item)
    return max


def addNCount(someList, outputArr):
    for item in someList:
        if not item in outputArr:
            outputArr[item] = 1
        else:
            outputArr[item] += 1
    return someList


def prepareData(arrIn, arrOut, max):
    for item in range(0, max):
        arrOut[item] = 0
    for key, value in arrIn.items():
        for i in range(0, max):
            if (len(key) == i):
                arrOut[i] += value



def createPlot(arr1, arr2):
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(arr1.keys(), arr1.values(), 'y')
    ax.plot(arr2.keys(), arr2.values(), 'b')
    ax.set_xlabel('Symbols', fontsize=15, color='green')
    ax.set_ylabel('Amount', fontsize=15, color='green')
    matplotlib.pyplot.show()


max = max(countMax(arrH), countMax(arrS))
print(max)

addNCount(arrS, arrSS)
addNCount(arrH, arrSH)
print(arrS)
print(arrSS)

prepareData(arrSS, sGroup, countMax(arrS) + 1)
prepareData(arrSH, hGroup, countMax(arrH) + 1)
print(sGroup)
print(hGroup)

createPlot(sGroup, hGroup)
