import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[4.8 * 3, 6.4 * 3])
fig.suptitle('Sin(x) [punainen] ja Cos(x) [sininen]\n',   
             fontweight ="bold")  

x_axis = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
# print(f'{x_axis}')

cos, sin = np.cos(x_axis), np.sin(x_axis)

colour_1 = 'red'
colour_0 = 'blue'

plt.plot(x_axis, cos, color=colour_0)
plt.plot(x_axis, sin, color=colour_1)

pi = np.pi
x_ticks = [-3*pi, -2*pi, -pi, 0, pi, 2*pi, 3*pi]

x_ticks_labels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']

'''
[r'$-3\pi}$', r'$\frac{-5\pi}{2}$', r'$-2\pi$', r'$\frac{-3\pi}{2}$',
                  r'$-\pi$', r'$\frac{-\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$',
                  r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$']

'''

print(x_ticks, len(x_ticks))
print(x_ticks_labels, len(x_ticks_labels))
# input('breakpoint, press ENTER')

plt.xticks(x_ticks, x_ticks_labels)
plt.grid()
plt.show()
