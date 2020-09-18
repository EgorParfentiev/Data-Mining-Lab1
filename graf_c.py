from collections import Counter
import main
import matplotlib.pyplot

spamTop = dict(Counter(main.spamdict).most_common(20))
hamTop = dict(Counter(main.hamdict).most_common(20))


def createPlot(top, info, col):
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(top.keys(), top.values(), 'y', label=info, color=col)
    ax.set_xlabel('Words')
    ax.set_ylabel('Num')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


createPlot(spamTop, 'spam', 'red')
createPlot(hamTop, 'ham', 'blue')