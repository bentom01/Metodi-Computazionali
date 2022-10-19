import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1, 16)
y = np.array([0,3,5,6,8,12,15,19,22,27,34,40,48,57,69])

plt.plot(x, y, 'o-', color='pink')
plt.xlabel('numeri naturali')
plt.ylabel('numeri crescenti')

plt.show()
