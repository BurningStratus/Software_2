from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius = 1, fill = 0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')


x_axis_ticks = []
tick = -1.2
while tick < 1:
    tick += 0.2
    x_axis_ticks.append(tick)


plt.xticks(x_axis_ticks)
plt.yticks([-1, 0, 1])

pist_xy = np.array([np.pi/6, np.pi/4])
varit = np.array(['red', 'green'])

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color=varit, marker='X')

plt.annotate(r'$(\frac{\pi}{6})$',
             xy=(np.cos(np.pi/6), np.sin(np.pi/6)), xycoords='data',
             xytext=(+30, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()