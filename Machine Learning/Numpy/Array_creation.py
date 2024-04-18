import  numpy as np

#create an array from list with type float
a1=np.array([[1,2,3],[4,5,6]],dtype='float') #creating an array with all float numbers
print("Array contents are: ",a1) #displaying the created array

#create array from tuple
a2=np.array((1,2,3))
print("Array created from tuple is:",a2)

#creating a 16*173 array with all zeros
a3=np.zeros((16,173))
print("\n An Array initialized with all zeros:\n",a3)

#create a 17*17 array with all ones
one = np.ones((17,17))
print("\n An array initialized with all ones:\n",one)

#create a matrix full of number
a4 = np.full((17,17),-24.6782) #order = 17*17, required number = -24.6782
print("\n An array initialized with all 4.78654 is:\n",a4)

#create array with random numbers
a5= np.random.random((3,2))
print("\n  An Random array:\n",a5)

#create a sequence of integers from 0 to 40 with steps of 5
a6 = np.arange(0,40,5) #start value is displayed,end value is
print("\n A Sequential array with steps of 5:\n",a6)

a7 = np.arange(0,40,10)
print( "A sequential array with 10 values between  and 5:\n",a7)


#Flatten array
all = np.array([[1,2,3,],[4,5,6]])

reshaped_array = all.reshape((1,-1))
reshaped_array_2 = all.reshape((-1,1))
print("\ Original array:\n",all)
print("Reshaped array:\n",reshaped_array)
print("Reshaped array:\n",reshaped_array_2)

