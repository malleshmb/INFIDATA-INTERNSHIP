n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))
choice = int(input("Enter your choice  1:Add, 2:Sub, 3:Mul, 4:Div, 5:Mod"))
if(choice==1):
    res = n1+n2
    print("Addition of {0} and {1} is {2}".format(n1,n2,res))
elif(choice==2):
    res = n1-n2
    print("Subtraction of {0} and {1} is {2}".format(n1,n2,res))
elif(choice==3):
    res = n1 * n2
    print("Multiplication of {0} and {1} is {2}".format(n1, n2, res))
elif(choice==4):
    res = n1 / n2
    print("Division of {0} and {1} is {2}".format(n1, n2, res))
elif(choice==5):
    res = n1 % n2
    print("Modulus of {0} and {1} is {2}".format(n1, n2, res))
else:
    print("Invalid choice")