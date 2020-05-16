import matplotlib

import matplotlib.pyplot as plt


matplotlib.use('Agg')

xAxis = list(range(0,64))


def parabola(xValues):

  yValues = []

  for x in xValues:

    y = x*x

    yValues.append(y)

  return yValues


yAxis = parabola(xAxis)

sliceXAxis  = xAxis[5:35]

sliceYAxis  = yAxis[5:35]

style = 'ro'

plt.plot(sliceXAxis , sliceYAxis , style)

plt.axis([ 0, 6.4, -1, 1])


filename = 'graph.png'

plt.savefig(filename)