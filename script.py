import matplotlib

import matplotlib.pyplot as plt


matplotlib.use('Agg')

xAxis = list(range(-20,20))


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

plt.axis([-10, 10, 0, 100])

filename = 'graph.png'

plt.savefig(filename)