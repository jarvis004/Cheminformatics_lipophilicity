import numpy as np
from matplotlib import pyplot as plt

x = np.array([4.59, 4.59, 4.46, 3.78, 5.39, 3.73, 4.31, 4.22, 4.98, 4.85])
y = np.array([-0.052, -0.017, -0.070, -0.432, -0.052, -0.630, -0.213, -0.525, -0.194, -0.308])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(3.5, 5.5, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('CLogP (Web)')
plt.ylabel('Rm')
plt.scatter(x, y)