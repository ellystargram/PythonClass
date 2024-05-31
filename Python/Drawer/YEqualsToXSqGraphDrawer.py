import matplotlib.pyplot as plt
import numpy as np

# resolution of the graph
# 4k
plt.figure(figsize=(3840 / 96, 2160 / 96), dpi=96)
# modify text size of the graph
plt.rc('font', size=40)
# modify graph line width
plt.rc('lines', linewidth=4)
# modify text size of the legend
plt.rc('legend', fontsize=40)
# modify grid line width
plt.rc('grid', linewidth=2)
# remove background color
plt.rc('axes', facecolor='none')

# draw grid
plt.grid(True)

# draw x^2
x = np.linspace(-10, 10, 100)
y = x ** 2
plt.plot(x, y, '-r', label='y=x^2')

plt.title('y=x^2')
plt.legend(loc='upper left')
plt.show()
