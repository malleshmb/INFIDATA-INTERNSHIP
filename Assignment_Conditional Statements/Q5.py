price=int(input("enter the bike price"))
if(price>100000):
    tax=price+0.15
    print("tax with 15%",tax)
elif(price>50000 and price<=100000):
    tax=price+0.10
    print("tax with 10%", tax)
elif(price<=50000):
    tax=price+0.5
    print("tax with 5%",tax)