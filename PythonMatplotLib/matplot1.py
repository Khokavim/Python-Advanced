import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

"""Plot x versus y"""
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')

"""
For every x, y pair of arguments, there is an optional third argument 
which is the format string that indicates the color and line type of the plot
"""
#plt.plot([1,2,3,4], [1,4,9,16], 'g^')

"""
The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
"""
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])

"""
plotting several lines with different format styles in one command using numpy arrays.
"""
t = np.arange(0., 5., 0.2)
 #red dashes, blue squares and green triangles
plt.plot(t, t, 'ro', t, t**2, 'bs', t, t**3, 'g^')

plt.show()
