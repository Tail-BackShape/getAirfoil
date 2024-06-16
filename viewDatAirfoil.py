import matplotlib.pyplot as plt
import numpy as np
import sys

# Load data
data03_axis1, data03_value1  = np.loadtxt(sys.argv[-1], skiprows=3, unpack=True)



fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(data03_axis1, data03_value1 , "o-", color="k", label="value1 of data01")
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 0.5)
ax.set_xticks(np.arange(-0.125, 1.125, 0.025))
ax.set_yticks(np.arange(-0.5, 0.525, 0.025))
ax.set_xlabel("axis1")
ax.set_ylabel("value1")
ax.legend(loc="upper left")
plt.show()
