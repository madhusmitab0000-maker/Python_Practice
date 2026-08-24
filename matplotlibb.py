import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[10,20,25,30,40]

plt.plot(x,y,color='red',linestyle='--',linewidth=2,marker='o',markersize=8,markerfacecolor='blue',markeredgecolor='black')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()