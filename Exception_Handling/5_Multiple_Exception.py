n1 = int(input("Enter the 1st number:"))
n2 = int(input("Enter the 2nd number:"))
l1 = [4,5,6,7,8]
print("list l1 is:",l1)
try:
    div = n1 / n2
    print("Result of division is:", div)
    print('l1[2]:',l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print("You have trying to divide and integer number by zero")
    print("e value is:",e)
except IndexError as e:
    print("You are trying to acces the wrong index")
    print('e value is:',e)
print("End")
