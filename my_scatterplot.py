import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[10,20,25,30,40]  
plt.scatter(x,y,color='blue',marker='*',s=500,edgecolor='black')
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()