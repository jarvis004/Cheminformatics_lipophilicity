import numpy as np
from matplotlib import pyplot as plt

x = np.array([43, 100, 41, 10, 56, 1.2, 96, 19, 44, 56])
y = np.array([-0.052, -0.017, -0.070, -0.432, -0.052, -0.630, -0.213, -0.525, -0.194, -0.308])
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
xp = np.linspace(0, 100, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('% Survival')
plt.ylabel('Rm')
plt.scatter(x, y)