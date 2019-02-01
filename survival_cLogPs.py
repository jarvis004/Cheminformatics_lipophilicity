import numpy as np
from matplotlib import pyplot as plt

x = np.array([43, 100, 41, 10, 56, 1.2, 96, 19, 44, 56])
y = np.array([4.20, 4.20, 3.93, 3.24, 4.98, 3.12, 4.60, 3.76, 4.59, 4.32])
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
xp = np.linspace(0, 100, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('% Survival')
plt.ylabel('CLogP (Spartan)')
plt.scatter(x, y)