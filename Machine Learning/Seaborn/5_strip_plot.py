import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

sns.stripplot(x='species', y='sepal_width',color='blue',data=df)
plt.show()