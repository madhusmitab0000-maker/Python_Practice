import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[10,20,25,30,40]

plt.bar(x,y,color='green',edgecolor='black')
plt.title("Simple Bar Plot")    
plt.xlabel("X-axis")
plt.ylabel("Y-axis")        
plt.show()