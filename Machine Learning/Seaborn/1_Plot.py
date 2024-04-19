import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
print(df)

sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#setting the title using matplotlib
plt.title('lineplot on iris')
plt.show()