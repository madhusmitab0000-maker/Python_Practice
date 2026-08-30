import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution

plt.hist(x,bins=30,color='purple',edgecolor='black')
plt.title("Simple Histogram")
plt.xlabel("Value") 
plt.ylabel("Frequency")
plt.show()