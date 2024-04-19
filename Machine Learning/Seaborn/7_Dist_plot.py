import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sns.displot(data['sepal_width'],color='g')
plt.show()