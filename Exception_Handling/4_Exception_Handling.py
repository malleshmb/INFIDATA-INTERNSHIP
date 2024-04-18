n1 = int(input("Enter the 1st number:"))
n2 = int(input("Enter the 2nd number:"))
try:
    div = n1/n2
    print("Result of division is:",div)
except ZeroDivisionError as e:
    print("You have trying to divide and integer number by zero")
    print("e value is:",e)
print("End")