import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
# print(df.head())

sns.scatterplot(x="total_bill", y="tip", data=df,hue='size',marker='*',s=100)
plt.show()