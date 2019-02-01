import numpy as np
from matplotlib import pyplot as plt

x = np.array([4.59, 4.59, 4.46, 3.78, 5.39, 3.73, 4.31, 4.22, 4.98, 4.85])
y = np.array([4.20, 4.20, 3.93, 3.24, 4.98, 3.12, 4.60, 3.76, 4.59, 4.32])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(3.5, 5.5, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('CLogP (Web)')
plt.ylabel('CLogP (Sparton)')
plt.scatter(x, y)