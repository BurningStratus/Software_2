import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt, patches
from fractions import Fraction as fr


degrees_list = [0, 45, 60, 90, 120, 150, 180, 270]
rads = []

for degs in degrees_list:
    radians = np.deg2rad(degs)
    print(radians)
    rads.append(radians)



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


x_axis_ticks, y_axis_ticks = [], []
tick = -1.2
while tick < 1:
    tick += 0.2
    x_axis_ticks.append(tick)
    y_axis_ticks.append(tick)


plt.xticks(x_axis_ticks)
plt.yticks(y_axis_ticks)

pist_xy = np.array(rads)
varit = np.array(['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'])

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color=varit, marker='o')

x_txt = 5
y_txt = 5

annotation_list = [f'0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$',
                   r'$\pi$', r'$\frac{3\pi}{2}$']
for radian, annotation in zip(rads, annotation_list):

    plt.annotate(f'{annotation}',
             xy=(np.cos(radian), np.sin(radian)), xycoords='data',
             xytext=(x_txt, y_txt), textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=0"))

plt.show()