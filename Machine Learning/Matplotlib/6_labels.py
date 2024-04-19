import matplotlib.pyplot as plt
import  numpy as np

x = np.array([3,5,6,7])
y = np.array([7,8,6,5])

plt.plot(x,y)
plt.xlabel("Average pulse")
plt.ylabel("Calories burn")
plt.title("Sports watch data")
plt.show()