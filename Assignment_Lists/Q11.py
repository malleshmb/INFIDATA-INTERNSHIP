l1 = [ ]
for i in range(6):
    num = int(input("Enter a number to the list:"))
    l1.append(num)
print("Element \t \t Frequency")
for i in l1:
    print(i,end="\t")
    print(l1.count(i))


