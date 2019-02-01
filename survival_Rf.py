import numpy as np
from matplotlib import pyplot as plt

x = np.array([43, 56, 1.2, 96, 19, 44, 56])
y = np.array([0.95, 0.85, 0.45, 0.68, 0.91, 0.89, 0.89])
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
xp = np.linspace(0, 100, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('% Survival')
plt.ylabel('Rf')
plt.scatter(x, y)