import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

sns.barplot(x='species', y='sepal_width',color='y',data=df)
plt.show()