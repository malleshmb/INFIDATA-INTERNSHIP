import numpy as np

four_by_five=np.array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]])
print(four_by_five[0])
print(four_by_five[-1])
print(four_by_five[2,3])
print(four_by_five[:, 0])
print(four_by_five[:, 3:])
print(four_by_five[1:3, -2:])


