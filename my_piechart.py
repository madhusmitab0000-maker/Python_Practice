import matplotlib.pyplot as plt
import numpy as np

sizes = [30, 50, 70, 90]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Simple Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()