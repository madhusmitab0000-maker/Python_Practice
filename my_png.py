import matplotlib.pyplot as plt
import numpy as np
# sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# create  scatter plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()    
plt.grid()
plt.show()
# save the plot in png File
plt.savefig('scatter_plot.png')

