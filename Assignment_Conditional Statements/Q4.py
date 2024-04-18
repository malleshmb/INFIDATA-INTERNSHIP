per=float(input("enter the percentage"))
if(per>90):
    print("grade A")
elif(per>80 and per<=90):
    print("grade B")
elif(per>=60 and per<=80):
    print("grade C")
elif(per<60):
    print("grade D")