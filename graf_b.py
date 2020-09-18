import matplotlib.pyplot
import main

sArr = main.spamdict
hArr = main.hamdict

sGroup = {}
hGroup = {}


def countAvg(arr):
    tLen = 0
    tVal = 0
    for key, value in arr.items():
        tLen += len(key) * value
        tVal += value
    return tLen / tVal


def countMax(arr):
    max = 0
    for key, value in arr.items():
        if len(key) > max:
            max = len(key)
    return max


def prepareData(arrIn, arrOut, max):
    for item in range(0, max):
        arrOut[item] = 0

    for key, value in arrIn.items():
        for i in range(0, max):
            if (len(key) == i):
                arrOut[i] += value


maxS = countMax(sArr)
maxH = countMax(hArr)
print('avg for spam: ', countAvg(sArr))
print('avg for ham : ', countAvg(hArr))

prepareData(sArr, sGroup, maxS)
prepareData(hArr, hGroup, maxH)

fig, ax = matplotlib.pyplot.subplots()

ax.plot(sGroup.keys(), sGroup.values(), 'y')
ax.plot(hGroup.keys(), hGroup.values(), 'b')

ax.set_xlabel('Count', fontsize=15, color='green')
ax.set_ylabel('Freq', fontsize=15, color='green')

matplotlib.pyplot.show()

