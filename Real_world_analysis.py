import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1,11)
sales_in_cr = np.array([2,5,3.0,4.2,5.1,6.0,7.5,8.0,9.0,10.0])
plt.figure(figsize=(10,5))
plt.style.use('fast')
plt.plot(days, sales_in_cr, marker='o', color='blue', label='Sales in Cr')
plt.title("Sales Trend Over 10 Days")
plt.xlabel("Days")
plt.ylabel("Sales in Cr")   
plt.xticks(days)
plt.grid(True)
plt.savefig("sales_trend.png",format='png')
plt.show()
