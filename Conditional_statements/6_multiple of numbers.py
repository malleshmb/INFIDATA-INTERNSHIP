num = int(input("Enter a number: "))
if(num % 3==0 and num %5==0):
    print(num,"is multiple of 3 and 5")
elif(num %3==0):
    print(num,"is multiple of 3")
elif(num %5==0):
    print(num,"is multiple of 5")
else:
    print("invalid")