import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import math
KGS = [0.497,0.444,0.419,0.405,0.394,0.385,0.378,0.372,0.368,0.364]
Re = [50000,100000,150000,200000,250000,300000,350000,400000,450000,500000]

def func(x):
    return 1.0955-0.0562*np.log(x)


apr = func(np.linspace(45000,550000,1000))

plt.plot(np.linspace(45000,550000,1000),apr)

plt.scatter(Re,KGS)
plt.show()

