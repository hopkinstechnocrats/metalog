import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 14)
xs = np.linspace(0,1, 500)

y = [
    [-1.25, 0.16],
    [7.5, 0.5],
    [10.5, -2.5],
    [7.5, -4.5],
    [4.5, -2.5],
    [7.5, 0.5],
    [15, -0],
    [17, 2.5],
    [15, 5.5],
    [12, 2.5],
    [20, -5.5],
    [23, -2.5],
    [17, 0],
    [-1.64, 0],
]

markers = [
    [7.5,-2.5],
    [15, 2.5],
    [20,-2.5]
]
y=np.array(y)
markers = np.array(markers)

cs = CubicSpline(x,y, bc_type=[(1, [1, 0]), (1, [-1, 0])])

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_title("AutoNav - Barrel Racer Path")
ax.plot(cs(xs)[:, 0], cs(xs)[:, 1], label='spline')
ax.plot(y[:,0],y[:,1], 'o', label='waypoints')

ax.plot(markers[:,0], markers[:, 1], 'ro', label='obstacles')
ax.axes.set_aspect('equal')
ax.legend(loc='upper left')
plt.show()
