import numpy as np

a1 = np.array([1,2,3,4,5,6])
#add 1 to every element
print("Adding 1 to every element:",a1+1)

#multiply each element by 10
print("Multiplying each element bye 10:",a1*10)

#Square each element
print("Squaring each element:",a1**2)

#modiffy exiting array
a1 *=2  #a1=a1*2
print("Doubled each element of original array:",a1)

#transpose of array
a2 = np.array([[1,2,3],[3,4,5],[9,6,0]])
print("\n Original array:\n",a2)
print("Transpose of array:\n",a2.T)
