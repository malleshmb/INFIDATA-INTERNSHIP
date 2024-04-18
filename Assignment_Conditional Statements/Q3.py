name=input("enter the name")
id=int(input("enter the id"))
e_bill=int(input("enter units"))
print("name is ",name)
print("id is",id)
if(e_bill<=100):
    print("no charge")
elif(e_bill>100 and e_bill<200):
    res=e_bill*5
    print("charger",res)
elif(e_bill>200):
    res=e_bill*10
    print("charges",res)
else:
    print("ntg")