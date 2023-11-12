import numpy as np
import matplotlib.pyplot as plt

x_axis = np.linspace(-3 * np.pi, 3 * np.pi, 50, endpoint=True, retstep=True)

print(x_axis)

cos, sin = np.cos(x_axis), np.sin(x_axis)

plt.plot(x_axis, cos)
plt.plot(x_axis, sin)

plt.show()
