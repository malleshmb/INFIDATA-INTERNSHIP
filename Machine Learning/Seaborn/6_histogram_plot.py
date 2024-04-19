import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sns.histplot(x='species', y='sepal_width', data=data)
plt.show()