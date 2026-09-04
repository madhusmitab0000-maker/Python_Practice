import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
# print(df.head())
print(df.corr(numeric_only=True))        
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()