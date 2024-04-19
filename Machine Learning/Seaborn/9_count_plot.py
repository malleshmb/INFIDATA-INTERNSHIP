import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

sns.countplot(x='sepal_length', hue="species",data=df,palette='Set2')
plt.show()