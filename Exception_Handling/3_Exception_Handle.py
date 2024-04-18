l1 =[ 2,3,4,5,6]
print("l1 is:",l1)
try:
    print('l1[2]:',l1[2])
    print('l1[3]:',l1[3])
    print('l1[4]:',l1[4])
except IndexError as e:
    print("You are trying to acces the wrong index")
    print('e value is:',e)
print("End")