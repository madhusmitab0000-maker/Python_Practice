import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)  # Generate 100 random numbers from a normal distribution
plt.boxplot(x)
plt.show()