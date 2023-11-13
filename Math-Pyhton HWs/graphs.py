import numpy as np
import matplotlib.pyplot as plt

x_axis = np.linspace(-3 * np.pi, 3 * np.pi, 50, endpoint=True)
print(x_axis)
cos, sin = np.cos(x_axis), np.sin(x_axis)

colour_0 = 'green'
colour_1 = 'blue'

plt.plot(x_axis, cos, color=colour_0)
plt.plot(x_axis, sin, color=colour_1)

pi = np.pi
x_ticks = [-3*pi, -5*pi/2, -2*pi, -3*pi/2, -pi, -pi/2, 0, pi/2, pi, 3*pi/2, 2*pi, 5*pi/2, 3*pi]

x_ticks_labels = [r'$-3\pi}$', r'$\frac{-5\pi}{2}$', r'$-2\pi$', r'$\frac{-3\pi}{2}$',
                  r'$-\pi$', r'$\frac{-\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$',
                  r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$']


print(x_ticks, len(x_ticks))
print(x_ticks_labels, len(x_ticks_labels))
input('breakpoint')

plt.xticks(x_ticks, x_ticks_labels)

plt.show()
