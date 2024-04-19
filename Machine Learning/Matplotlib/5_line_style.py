import matplotlib.pyplot as plt
import  numpy as np

x = np.array([0,6])
ypoints = np.array([0,10])

plt.plot(ypoints,linestyle="dotted",color='red') #linestyle
plt.show()

plt.plot(ypoints,linestyle="dashed",linewidth=5,color='#ffcee0')
plt.show()

plt.plot(ypoints,linestyle="dashdot",lw=10)
plt.show()
plt.plot(ypoints,ls="solid")
plt.show()
