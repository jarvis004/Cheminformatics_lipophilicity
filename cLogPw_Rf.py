import numpy as np
from matplotlib import pyplot as plt

x = np.array([4.59, 5.39, 3.73, 4.31, 4.22, 4.98, 4.85])
y = np.array([0.95, 0.85, 0.45, 0.68, 0.91, 0.89, 0.89])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(3.5, 5.5, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('CLogP (Web)')
plt.ylabel('Rf')
plt.scatter(x, y)