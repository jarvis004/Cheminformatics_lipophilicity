import numpy as np
from matplotlib import pyplot as plt

x = np.array([43, 100, 41, 10, 56, 1.2, 96, 19, 44, 56])
y = np.array([4.59, 4.59, 4.46, 3.78, 5.39, 3.73, 4.31, 4.22, 4.98, 4.85])
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
xp = np.linspace(0, 100, 100)
_ = plt.plot(x, y, '.', xp, p(xp) )
plt.xlabel('% Survival')
plt.ylabel('CLogP (Web)')
plt.scatter(x, y)