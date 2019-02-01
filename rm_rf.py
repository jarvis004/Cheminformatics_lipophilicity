import numpy as np
from matplotlib import pyplot as plt

x = np.array([-0.052, -0.052, -0.630, -0.213, -0.525, -0.194, -0.308])
y = np.array([0.95, 0.85, 0.45, 0.68, 0.91, 0.89, 0.89])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(-0.7, 0, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('Rm')
plt.ylabel('Rf')
plt.scatter(x, y)