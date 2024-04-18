l = int(input("Enter length:"))
b = int(input("Enter breadth:"))
h = int(input("Enter height:"))
while(True):
    choice = int(input("Enter your choice 1.Area, 2.Volume, 3.Exit:"))
    if(choice==1):
        area=l*b
        print("Area of the rectangle is:",area)
    elif(choice==2):
        vol = l*b*h
        print("Volume of the rectangle is:",vol)
    elif(choice==3):
        exit(0)
    else:
        print("Invalid choice")