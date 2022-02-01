# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Creating dataset
np.random.seed(10)
data = np.array([13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25,
                25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70])

print(data.mean())
print(np.median(data))
print(stats.mode(data))

fig = plt.figure(figsize = (10, 7))

# Creating plot
plt.boxplot(data)

# show plot
#plt.show()